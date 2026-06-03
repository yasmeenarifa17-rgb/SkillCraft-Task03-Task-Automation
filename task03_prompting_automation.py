import json
from textwrap import dedent

task_title = "Task 03: Prompting for Task Automation"

system_instruction = dedent("""
You are a data extraction assistant. Analyze the provided customer review.
Extract the information into a strict JSON format with the following keys:
- sentiment (String: "Positive", "Negative", or "Neutral")
- core_issue (String: 3-word summary of the main point)
- urgency_level (Integer: 1-5, where 5 is highly urgent/angry)

CRITICAL: Do NOT output any other text, markdown formatting, or explanations outside the JSON block.
""").strip()

test_cases = [
    {
        "input": "I ordered the blue headphones last week. They arrived yesterday but the left ear cup is shattered. Refund immediately!",
        "expected_output": {
            "sentiment": "Negative",
            "core_issue": "Shattered left earcup",
            "urgency_level": 5
        }
    },
    {
        "input": "The software update is okay. I like the new dark mode, but the battery drains slightly faster now.",
        "expected_output": {
            "sentiment": "Neutral",
            "core_issue": "Faster battery drain",
            "urgency_level": 2
        }
    },
    {
        "input": "Absolutely phenomenal service! The barista remembered my complicated order perfectly. Made my week.",
        "expected_output": {
            "sentiment": "Positive",
            "core_issue": "Phenomenal customer service",
            "urgency_level": 1
        }
    }
]

def format_prompt(review_text):
    return dedent(f"""
    {system_instruction}

    Customer Review:
    {review_text}

    Return only valid JSON.
    """).strip()

def main():
    print("=" * 70)
    print(task_title)
    print("=" * 70)
    print("
Prompt Template:
")
    print(system_instruction)

    print("
" + "=" * 70)
    print("Input-Output Testing")
    print("=" * 70)

    for i, case in enumerate(test_cases, start=1):
        print(f"
Test Case {i}")
        print("Input Review:")
        print(case["input"])
        print("
Expected JSON Output:")
        print(json.dumps(case["expected_output"], ensure_ascii=False))

    print("
" + "=" * 70)
    print("Prompt Example")
    print("=" * 70)
    print(format_prompt(test_cases[0]["input"]))

if __name__ == "__main__":
    main()
