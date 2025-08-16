FROM python:3.11

WORKDIR /tarotAI

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
