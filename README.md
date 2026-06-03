# ⚙️ Task 03: Prompting for Task Automation
![Header](https://github.com/user-attachments/assets/02bbd33e-f3df-42bb-bfc5-e6919bce2faa
)
![Data Extraction](https://img.shields.io/badge/Skill-Data_Extraction-red?style=for-the-badge)
![JSON Output](https://img.shields.io/badge/Format-Strict_JSON-yellow?style=for-the-badge)

## 🎯 Objective
To design a robust prompt that consistently extracts unstructured customer review text and transforms it into structured JSON data for an automated pipeline.

---

## 🛠️ The Prompt Engine

**Instruction:**
> You are a data extraction assistant. Analyze the provided customer review. Extract the information into a strict JSON format with the following keys:
> - `sentiment` (String: "Positive", "Negative", or "Neutral")
> - `core_issue` (String: 3-word summary of the main point)
> - `urgency_level` (Integer: 1-5, where 5 is highly urgent/angry)
> 
> **CRITICAL:** Do NOT output any other text, markdown formatting, or explanations outside the JSON block.

---

## 🧪 Input-Output Testing

| Review Text (Input) | Extracted JSON (Output) |
| :--- | :--- |
| "I ordered the blue headphones last week. They arrived yesterday but the left ear cup is shattered. Refund immediately!" | `{"sentiment": "Negative", "core_issue": "Shattered left earcup", "urgency_level": 5}` |
| "The software update is okay. I like the new dark mode, but the battery drains slightly faster now." | `{"sentiment": "Neutral", "core_issue": "Faster battery drain", "urgency_level": 2}` |
| "Absolutely phenomenal service! The barista remembered my complicated order perfectly. Made my week." | `{"sentiment": "Positive", "core_issue": "Phenomenal customer service", "urgency_level": 1}` |

---

## 🐛 Debugging & Reflection
*Initial attempts resulted in the LLM adding conversational filler like "Here is the JSON you requested:". This broke the automated parsing. By adding the explicit negative constraint ("Do NOT output any other text..."), the model's reliability reached 100%.*

---
*Created as part of the SkillCraft Technology Prompt Engineering Internship*
