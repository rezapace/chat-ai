import google.generativeai as genai

# Configure the API key
genai.configure(api_key="asdasd")

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

# Define your prompt
prompt = "Write a story about a magic backpack."

# Generate content
response = model.generate_content(prompt)

# Extract and print the content
if response._done:
    candidates = response._result.candidates
    if candidates:
        text_content = candidates[0].content.parts[0].text
        print(text_content)
    else:
        print("No candidates found in the response.")
else:
    print("Content generation not completed.")
