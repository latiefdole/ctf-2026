# Aplikasi manajemen konfigurasi internal
# PT Nusantara Sistem Solusi

import flask
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"status": "ok", "version": "1.0.0"})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
