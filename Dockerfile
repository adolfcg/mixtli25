# Dockerfile for vuln_app
FROM python:3.11-slim

WORKDIR /app
COPY vuln_app.py /app/
COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --use-deprecated=legacy-resolver -r requirements.txt

EXPOSE 8000
CMD ["python", "vuln_app.py"]
