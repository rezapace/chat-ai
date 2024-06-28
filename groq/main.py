import os
from groq import Groq

# Set API key (biasanya disimpan sebagai environment variable)
api_key = os.environ.get("GROQ_API_KEY")

# Buat instance client Groq
client = Groq(api_key=api_key)

# Buat permintaan chat completion
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Jelaskan apa itu machine learning dalam bahasa Indonesia",
        }
    ],
    model="llama3-8b-8192",
)

# Dapatkan dan cetak hasil generasi
result = chat_completion.choices[0].message.content
print(result)