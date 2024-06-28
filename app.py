from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from groq import Groq
import logging

app = Flask(__name__)
CORS(app)  # Tambahkan ini

# Konfigurasi logging
logging.basicConfig(level=logging.DEBUG)

# Konfigurasi API keys
genai.configure(api_key="AIz")
groq_api_key = os.environ.get("GROQ_API_KEY")

# Inisialisasi model
gemini_model = genai.GenerativeModel('gemini-1.5-flash')
groq_client = Groq(api_key=groq_api_key)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        logging.debug(f"Data diterima: {data}")

        prompt_gemini = data.get('prompt_gemini')
        prompt_groq = data.get('prompt_groq')

        if not prompt_gemini:
            return jsonify({"error": "prompt_gemini is required"}), 400

        if not prompt_groq:
            return jsonify({"error": "prompt_groq is required"}), 400

        # Generate content with Gemini
        gemini_response = gemini_model.generate_content(prompt_gemini)
        if gemini_response._done:
            gemini_candidates = gemini_response._result.candidates
            if gemini_candidates:
                gemini_text = gemini_candidates[0].content.parts[0].text
            else:
                gemini_text = "No candidates found."
        else:
            gemini_text = "Gemini generation not done."

        # Generate content with Groq
        chat_completion = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt_groq,
                }
            ],
            model="llama3-8b-8192",
        )
        groq_text = chat_completion.choices[0].message.content

        return jsonify({
            "gemini_response": gemini_text,
            "groq_response": groq_text
        })

    except Exception as e:
        logging.error(f"Terjadi kesalahan: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
