from flask import Flask, request, jsonify, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import string, random, qrcode, io, base64
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:UjnjWTuPeySqeMuTAixZpbswxbJHDqkU@shinkansen.proxy.rlwy.net:42679/railway'

db = SQLAlchemy(app)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.Text, nullable=False)
    short_id = db.Column(db.String(6), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# ✅ FIXED: Use application context
with app.app_context():
    db.create_all()

def generate_short_id(num_chars=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=num_chars))

def generate_qr_code(data):
    img = qrcode.make(data)
    buf = io.BytesIO()
    img.save(buf)
    return base64.b64encode(buf.getvalue()).decode("utf-8")

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form['url']
    short_id = generate_short_id()
    short_url = request.host_url + short_id

    # Store in DB
    url = URL(original_url=original_url, short_id=short_id)
    db.session.add(url)
    db.session.commit()

    qr_code = generate_qr_code(short_url)
    return render_template('index.html', short_url=short_url, qr_code=qr_code)

@app.route('/<short_id>')
def redirect_url(short_id):
    url = URL.query.filter_by(short_id=short_id).first_or_404()
    return redirect(url.original_url)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

