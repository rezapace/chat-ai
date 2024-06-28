# Chat App

## Deskripsi
Chat App adalah aplikasi perbandingan respons AI yang memungkinkan pengguna untuk mengirim pesan dan menerima balasan dari dua model AI yang berbeda, yaitu Gemini dan Groq. Aplikasi ini dirancang untuk memberikan wawasan tentang bagaimana kedua model AI merespons pertanyaan atau pernyataan yang sama.

## Kegunaan
Aplikasi ini berguna untuk:
- Membandingkan respons dari dua model AI yang berbeda.
- Menguji kemampuan dan keakuratan model AI dalam memahami dan merespons input pengguna.
- Memberikan pengalaman interaktif dalam berkomunikasi dengan AI.

## Fungsi
Fungsi utama dari Chat App adalah:
- Mengirim pesan dari pengguna ke dua model AI (Gemini dan Groq).
- Menerima dan menampilkan balasan dari kedua model AI.
- Menyediakan antarmuka pengguna yang intuitif untuk berinteraksi dengan AI.

## Bagaimana Menjalankan
Untuk menjalankan aplikasi ini, ikuti langkah-langkah berikut:

1. **Clone repositori:**
   ```bash
   git clone https://github.com/rezapace/chat-ai
   cd chat-app
   ```

2. **Instal dependensi:**
   ```bash
   npm install
   ```

3. **Jalankan server backend:**
   Pastikan Anda memiliki server backend yang berjalan untuk menangani permintaan chat. Anda dapat menggunakan `groq/main.py` dan `gemini/main.py` sebagai referensi untuk mengatur server backend.

4. **Jalankan aplikasi:**
   ```bash
   npm start
   ```

5. **Buka aplikasi di browser:**
   Buka [http://localhost:3000](http://localhost:3000) untuk melihat aplikasi di browser.

6. **jalankan python**
    ```bash
    export GROQ_API_KEY="gsk_yIQ"

    cd /github/AI-Financial-Analysis/tampilan
    python app.py
    ```

## Kesimpulan
Chat App adalah alat yang berguna untuk membandingkan respons dari dua model AI yang berbeda, Gemini dan Groq. Dengan antarmuka yang intuitif dan mudah digunakan, aplikasi ini memungkinkan pengguna untuk berinteraksi dengan AI dan mengevaluasi kemampuan mereka dalam memahami dan merespons input. Aplikasi ini dapat digunakan untuk berbagai tujuan, termasuk penelitian, pengembangan, dan hiburan.