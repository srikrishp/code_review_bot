import subprocess

def run_static_analysis(file_path):
    pylint_result = subprocess.getoutput(f"pylint {file_path}")
    bandit_result = subprocess.getoutput(f"bandit -r {file_path}")

    return {
        "pylint": pylint_result,
        "bandit": bandit_result
    }
