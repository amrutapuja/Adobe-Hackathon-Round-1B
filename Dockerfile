FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app

COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt
COPY nltk_data/ /root/nltk_data/

COPY . .

ENTRYPOINT ["python", "main.py"]
