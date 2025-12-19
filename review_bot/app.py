from analyzer.static_analyzer import run_static_analysis
from analyzer.llm_reviewer import review_code

file_path = "samples/sample_code.py"

static_results = run_static_analysis(file_path)
combined_report = static_results["pylint"] + "\n" + static_results["bandit"]

ai_suggestions = review_code(combined_report)

print("===== STATIC ANALYSIS =====")
print(combined_report)

print("\n===== AI REVIEW =====")
print(ai_suggestions)
