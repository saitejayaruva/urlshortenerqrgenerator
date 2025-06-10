# 🔗 URL Shortener with QR Code Generator

A simple Flask-based application that shortens long URLs and generates QR codes for easy sharing. Built with Python, Flask, SQLAlchemy, and MySQL.

![App Screenshot](Images/Image.png)

## 🚀 Features

- 🔐 Unique short URL generation
- 📎 Automatic QR code generation
- 📊 Click tracking & analytics (to be added)
- 🌐 Easy redirect using short link
- 🗃️ Stores original URLs in a MySQL database
- 🎨 Simple, clean UI

## 🛠️ Tech Stack

- **Backend:** Flask, Python
- **Database:** MySQL
- **Frontend:** HTML/CSS
- **Others:** SQLAlchemy, QRCode
- **Deploy Options:** Render, Railway, Heroku

## 📷 QR Code + Short URL Demo

1. Enter a long URL.
2. Get a shortened URL like: `http://127.0.0.1:5000/GI2ssG`
3. Scan the generated QR code or click the short link.

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/saitejayaruva/urlshortenerqrgenerator.git
cd urlshortenerqrgenerator
2. Create & Activate Virtual Environment
bash
Copy
Edit
python -m venv venv
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Configure Database
Update your database URI in app.py:

python
Copy
Edit
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://username:password@host:port/dbname'
Or use .env file with python-dotenv.

5. Run the App
bash
Copy
Edit
python app.py
# Or with Gunicorn for production
gunicorn app:app
🖼️ Screenshot

🌐 Deployment Tips
On Render/Railway, configure:

gunicorn as the start command

Environment variable for database URI

Make sure your MySQL DB is accessible externally.

📬 Contact
Built with ❤️ by Saiteja Yaruva

📄 License
MIT License

yaml
Copy
Edit

---
