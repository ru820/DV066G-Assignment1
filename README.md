# DV066G Assignment 1

## Models Used
- qwen2.5:0.5b
- tinyllama

## Requirements
- Python 3.12
- Ollama

## Installation

### Install Ollama
https://ollama.com/install.ps1 

### Pull the models
```bash
ollama pull qwen2.5:0.5b
ollama pull tinyllama
```

### Install Python package
pip install ollama

## Run
python main.py

## Output
The program sends the same prompt to two different language models and stores the answers in a CSV file.

## Observations
Both models ran locally without using external APIs.

qwen2.5:0.5b generated longer and more detailed responses.

tinyllama generated shorter responses and was faster.

Local models are free and provide better privacy, but their quality is generally lower than commercial models such as ChatGPT.


