import os
import fitz  # PyMuPDF
import nltk
import os
import pickle
from nltk.tokenize.punkt import PunktSentenceTokenizer

# Custom offline tokenizer function
def sent_tokenize(text):
    punkt_path = "/root/nltk_data/tokenizers/punkt/english.pickle"
    with open(punkt_path, "rb") as f:
        tokenizer = pickle.load(f)
    return tokenizer.tokenize(text)


def load_documents(input_dir):
    docs = {}
    for file in os.listdir(input_dir):
        if file.endswith(".pdf"):
            path = os.path.join(input_dir, file)
            with fitz.open(path) as doc:
                text = ""
                for page in doc:
                    text += page.get_text()
                docs[file] = text
    return docs

def extract_relevant_sections(documents, persona):
    job_keywords = persona["job"].lower().split()
    results = []

    for doc_name, content in documents.items():
        sections = []
        sentences = sent_tokenize(content)
        for i, sentence in enumerate(sentences):
            score = sum(1 for word in job_keywords if word in sentence.lower())
            if score >= 3:
                sections.append({
                    "document": doc_name,
                    "page_number": (i // 20) + 1,  # rough estimate
                    "section_title": sentence[:80] + "...",
                    "importance_rank": score
                })
        results.extend(sections[:5])
    return results
