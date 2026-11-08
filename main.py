import ollama
import csv

prompt = "What are the advantages of AI in software engineering?"

models = [
    "qwen2.5:0.5b",
    "tinyllama"
]

results = []

for model in models:
    print(f"Running {model}...")

    response = ollama.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response["message"]["content"]

    results.append([
        model,
        answer
    ])

with open(
        "results.csv",
        "w",
        newline="",
        encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "Model",
        "Response"
    ])

    writer.writerows(results)

print("Results saved to results.csv")