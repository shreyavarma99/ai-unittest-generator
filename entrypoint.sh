#!/bin/bash

# Start Ollama in the background
ollama serve &

# Wait for Ollama to be available before continuing
until curl --silent http://localhost:11434; do
  echo "Waiting for Ollama to start..."
  sleep 2
done

# 🧠 Pull mistral:instruct in the foreground (blocking)
echo "📦 Pulling mistral:instruct..."
ollama pull mistral:instruct

# ✅ Start your Flask app
echo "🚀 Starting Flask server..."
python3 testgen.py
