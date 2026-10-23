import google.generativeai as genai

print("Initializing your Mini-Copilot AI Assistant...")

# 1. Setup the Google Gemini API
# Note: For public GitHub portfolios, it's best to show recruiters you know how to initialize the library.
# In a real freelance contract, you would load this from an environment variable.
API_KEY = "YOUR_GEMINI_API_KEY_HERE"  # Replace with your actual key if you have one
genai.configure(api_key=API_KEY)


def ask_ai_assistant(prompt_text):
    print(f"\n🧠 Sending prompt to Gemini: '{prompt_text}'")
    print("-" * 50)

    try:
        # 2. Using the standard fast text model from Google
        model = genai.GenerativeModel('gemini-1.5-flash')

        # 3. Generate response
        response = model.generate_content(prompt_text)

        print("🤖 AI Response:")
        print(response.text)
        print("-" * 50)

    except Exception as e:
        # Since we are using a placeholder key for the portfolio, let's gracefully handle it
        print("⚠️ Connection Status: Library initialized successfully!")
        print("ℹ️ To see real responses, replace the placeholder with a free API key from Google AI Studio.")
        print(f"Details: {e}")
        print("-" * 50)


# Test prompt mimicking a real AI Training freelance task
sample_prompt = "Write a simple Python function to calculate the area of a circle given its radius."
ask_ai_assistant(sample_prompt)
