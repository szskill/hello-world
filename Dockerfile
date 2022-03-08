FROM python
WORKDIR /app
COPY . .
CMD ["python", "main.py"]
