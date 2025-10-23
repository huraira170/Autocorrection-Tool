# main.py
from textblob import TextBlob
import language_tool_python
from openai import OpenAI
import os

# ---------- OFFLINE MODE ----------

def basic_autocorrect(text):
    """Fix simple spelling mistakes"""
    return str(TextBlob(text).correct())

def grammar_correct(text):
    """Fix grammar using LanguageTool"""
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    corrected = language_tool_python.utils.correct(text, matches)
    return corrected

# ---------- ONLINE (AI) MODE ----------

def gpt_ai_correction(text):
    """Context-aware correction using OpenAI GPT"""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Correct grammar and spelling: {text}"}]
    )
    return response.choices[0].message.content.strip()

# ---------- MAIN FUNCTION ----------

def autocorrect_text(text, mode="offline"):
    if mode == "offline":
        print("\n🔹 Spelling Correction (TextBlob):")
        print(basic_autocorrect(text))
        print("\n🔹 Grammar Correction (LanguageTool):")
        print(grammar_correct(text))

    elif mode == "online":
        print("\n🔹 GPT-based AI Correction:")
        print(gpt_ai_correction(text))


if __name__ == "__main__":
    text = input("Enter text to correct: ")
    choice = input("Use online AI model? (y/n): ").strip().lower()
    mode = "online" if choice == "y" else "offline"
    autocorrect_text(text, mode)
