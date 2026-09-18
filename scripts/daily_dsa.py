import json
import os
from pathlib import Path
from datetime import date


ROOT = Path(__file__).resolve().parent.parent
QUESTIONS_FILE = ROOT / "questions" / "questions.json"
SOLUTIONS_DIR = ROOT / "solutions"
README_FILE = ROOT / "README.md"


def load_questions():
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def get_completed_ids():
    completed = set()

    if not SOLUTIONS_DIR.exists():
        return completed

    for folder in SOLUTIONS_DIR.iterdir():
        if folder.is_dir():
            try:
                question_id = int(folder.name.split("_")[0])
                completed.add(question_id)
            except ValueError:
                pass

    return completed


def create_solution(question):
    folder_name = f"{question['id']:03d}_{question['title'].replace(' ', '_')}"
    folder = SOLUTIONS_DIR / folder_name

    folder.mkdir(parents=True, exist_ok=True)

    problem_file = folder / "problem.md"
    solution_file = folder / "solution.cpp"

    problem_content = f"""# {question['title']}

**Topic:** {question['topic']}  
**Difficulty:** {question['difficulty']}

## Problem

{question['problem']}

## Example

"""

    for example in question["examples"]:
        problem_content += f"""### Input
`{example['input']}`

### Output
`{example['output']}`

"""

    problem_content += f"""## Approach

{question['approach']}

## Complexity

- Time: `{question['time_complexity']}`
- Space: `{question['space_complexity']}`

## Interview Tip

{question['interview_tip']}
"""

    with open(problem_file, "w", encoding="utf-8") as f:
        f.write(problem_content)

    with open(solution_file, "w", encoding="utf-8") as f:
        f.write(question["solution"])

    return folder_name


def update_readme(question, folder_name):
    if not README_FILE.exists():
        content = "# DSA Daily Practice\n\n"
    else:
        with open(README_FILE, "r", encoding="utf-8") as f:
            content = f.read()

    today = date.today().isoformat()

    new_entry = f"""
## {today} — #{question['id']} {question['title']}

- **Topic:** {question['topic']}
- **Difficulty:** {question['difficulty']}
- **Solution:** [`solution.cpp`](solutions/{folder_name}/solution.cpp)

"""

    marker = "## Daily Problems"

    if marker not in content:
        content += f"\n{marker}\n"

    content += new_entry

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    questions = load_questions()
    completed_ids = get_completed_ids()

    remaining = [
        q for q in questions
        if q["id"] not in completed_ids
    ]

    if not remaining:
        print("All DSA questions have been completed.")
        return

    question = remaining[0]

    print(f"Adding: {question['title']}")

    folder_name = create_solution(question)
    update_readme(question, folder_name)

    print("DSA problem added successfully.")


if __name__ == "__main__":
    main()