#!/bin/sh

# Start Ollama server in background
ollama serve &

# Wait for server to start
echo "Waiting for Ollama to start..."
until curl -s http://localhost:11434 > /dev/null; do
  sleep 1
done

# Automatically pull the model (if not already pulled)
echo "Pulling mistral:instruct model..."
ollama pull mistral:instruct

# Keep container alive
wait
