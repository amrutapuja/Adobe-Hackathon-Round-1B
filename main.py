import os
import json
import time
from utils import extract_relevant_sections, load_documents
import nltk
nltk.download('punkt')


INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def main():
    start_time = time.time()

    persona = {
        "role": "PhD Researcher in Computational Biology",
        "job": "Prepare a comprehensive literature review focusing on methodologies, datasets, and performance benchmarks"
    }

    documents = load_documents(INPUT_DIR)
    extracted = extract_relevant_sections(documents, persona)

    output = {
        "metadata": {
            "input_documents": list(documents.keys()),
            "persona": persona["role"],
            "job_to_be_done": persona["job"],
            "processing_timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        },
        "extracted_sections": extracted
    }

    with open(os.path.join(OUTPUT_DIR, "output.json"), "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    main()
