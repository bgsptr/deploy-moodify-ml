import os
from flask import Flask, jsonify, request, send_from_directory
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

import numpy as np
import re
import neattext.functions as nfx
import json

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('wordnet')
nltk.download('punkt_tab')

app = Flask(__name__)

model = load_model('model.keras')

JSON_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'json_folder')
with open(os.path.join(JSON_FOLDER, 'tokenizer_word_index.json'), 'r') as f:
    word_index = json.load(f)

tokenizer = Tokenizer()
tokenizer.word_index = word_index

lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = text.lower()
    text = nfx.remove_urls(text)
    text = re.sub(r'@[A-Za-z0-9_]+', '', text)
    text = re.sub(r'#[A-Za-z0-9_]+', '', text)
    text = re.sub(r'[^a-z\s]', ' ', text)
    text = re.sub(r'\n', ' ', text)
    text = nfx.remove_numbers(text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = nfx.remove_stopwords(text)
    text = ' '.join([lemmatizer.lemmatize(word) for word in word_tokenize(text)])
    return text

@app.route('/get-word-index/<filename>', methods=['GET'])
def get_word_index(filename):
    try:
        return send_from_directory(JSON_FOLDER, filename)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/predict", methods=['POST'])
def predict():
    try:
        data = request.json
        if 'sentence' not in data:
            return jsonify({"error": "No sentence provided"}), 400

        sentence = data['sentence']

        sentence = clean_text(sentence)
        sequence = tokenizer.texts_to_sequences([sentence])
        padded_sequence = pad_sequences(sequence, maxlen=256, truncating='pre')
        print(padded_sequence)

        labels = ["anger", "enthusiasm", "happiness", "sadness", "worry"]

        predictions = model.predict(padded_sequence)[0]
        proba = np.array(predictions).tolist()

        predictions = {}

        for i, label in enumerate(labels):
            print(f"{label}: {proba[i]*100:.2f}%")
            predictions[label] = proba[i]

        return jsonify({"predictions": predictions})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)
