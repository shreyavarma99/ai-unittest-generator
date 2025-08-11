FROM ollama/ollama

RUN apt-get update && apt-get install -y curl python3-pip python3-venv

COPY requirements.txt requirements.txt
RUN pip install --break-system-packages --no-cache-dir -r requirements.txt

COPY . /app
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /app
EXPOSE 11434 5002

ENTRYPOINT ["/entrypoint.sh"]
