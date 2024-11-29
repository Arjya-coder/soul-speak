from flask import Flask, request, jsonify
from flask_cors import CORS
import bcrypt
import mysql.connector
import chatbot
import password_reset

app = Flask(__name__)
CORS(app)

# Database Connection
def connect_to_database():
    connection = mysql.connector.connect(
        host="localhost",  # XAMPP MySQL host
        user="root",       # Default XAMPP MySQL username
        password="",       # Default XAMPP MySQL password (leave blank if not set)
        database="soul_speak"  # Your database name
    )
    return connection

# Route: User Registration
@app.route('/register', methods=['POST'])
def register():
    data = request.form
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        db = connect_to_database()
        cursor = db.cursor()
        query = "INSERT INTO users (name, email, password_hash) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, hashed_password))
        db.commit()
        cursor.close()
        db.close()
        return jsonify({'status': 'Registration successful'})
    except mysql.connector.Error as err:
        return jsonify({'status': 'Error', 'message': str(err)}), 400

# Route: User Login
@app.route('/login', methods=['POST'])
def login():
    data = request.form
    email = data.get('email')
    password = data.get('password')

    try:
        db = connect_to_database()
        cursor = db.cursor(dictionary=True)
        query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()
        cursor.close()
        db.close()

        if user and bcrypt.checkpw(password.encode('utf-8'), user['password_hash'].encode('utf-8')):
            return jsonify({'status': 'Login successful'})
        else:
            return jsonify({'status': 'Error', 'message': 'Invalid credentials'}), 401
    except mysql.connector.Error as err:
        return jsonify({'status': 'Error', 'message': str(err)}), 400

# Route: Emotion Analysis
@app.route('/emotion', methods=['POST'])
def analyze_emotion():
    emotion = request.json['emotion']
    response = chatbot.get_emotional_response(emotion)
    return jsonify({'response': response})

# Route: Password Recovery
@app.route('/recover', methods=['POST'])
def recover_password():
    email = request.form['email']
    result = password_reset.send_recovery_email(email)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
