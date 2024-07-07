from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from flask_cors import CORS
import numpy as np
import os
import sqlite3
from datetime import datetime

app = Flask(__name__)
CORS(app)  

model = load_model('D:/Model/combined_model.h5')

class_labels = ['COVID', 'no', 'Normal', 'yes']

DB_FILE = 'D:/Model/app.db'

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row  
    return conn

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Images (
            id INTEGER PRIMARY KEY,
            filename TEXT NOT NULL,
            path TEXT NOT NULL,
            upload_date TEXT,
            prediction TEXT
        )
    ''')
    conn.commit()
    conn.close()

create_tables()

def prepare_image(image_path, target_size=(224, 224)):
    img = load_img(image_path, target_size=target_size)
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0  
    return img

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        filepath = os.path.join('uploads', file.filename)
        file.save(filepath)

        img = prepare_image(filepath)

        preds = model.predict(img)
        pred_class = class_labels[np.argmax(preds)]

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Images (filename, path, upload_date, prediction)
            VALUES (?, ?, ?, ?)
        ''', (file.filename, filepath, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), pred_class))
        conn.commit()
        conn.close()

        return jsonify({'prediction': pred_class})

    return jsonify({'error': 'File not processed'})

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)

