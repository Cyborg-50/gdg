import google.generativeai as genai

# Set up your Gemini API key
API_KEY = "AIzaSyC4RfSMGmwqDsV6JsZO47CEEVL3d_pIYSo"
genai.configure(api_key=API_KEY)

def get_gemini_response(prompt):
    """Sends the user prompt to Gemini and returns the response."""
    try:
        model = genai.GenerativeModel("gemini-pro")  # Use "gemini-pro" or another model if needed
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("Gemini AI Chatbot. Type 'exit' to quit.\n")
    
    while True:
        user_prompt = input("You: ")
        
        if user_prompt.lower() in ["exit", "quit", "bye"]:
            print("Goodbye! 👋")
            break
        
        response = get_gemini_response(user_prompt)
        print("\nGemini: ", response, "\n")
