from transformers import pipeline

reviewer = pipeline(
    "text-generation",
    model="google/flan-t5-small",
    max_new_tokens=200
)

def review_code(static_report):
    prompt = f"""
You are an expert software reviewer.
Analyze the following static analysis report and give improvement suggestions.

{static_report}
"""
    response = reviewer(prompt)
    return response[0]["generated_text"]
