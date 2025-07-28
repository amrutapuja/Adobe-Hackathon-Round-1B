# Adobe Hackathon Round 1B – Intelligent Persona-Based Extraction

## Objective
Analyze multiple PDFs and extract key insights based on a given persona and their task (job-to-be-done).

## Input
- Folder with 3–10 PDFs
- Persona & job defined in code (can be adapted to read from JSON)

## Output
A JSON with:
- Metadata
- Extracted sections and importance scores

## Run with Docker

### Build
```bash
docker build --platform linux/amd64 -t adobe-r1b:tag .
```

### Run
```bash
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none adobe-r1b:tag
```

## Dependencies
- PyMuPDF
- NLTK
