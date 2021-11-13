FROM python:alpine
RUN apk add --no-cache python3 g++ make
WORKDIR /app
COPY . .
CMD ["python3", "main.py"]
