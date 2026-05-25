from flask import Flask, request, jsonify, send_from_directory
import yt_dlp

app = Flask(__name__, static_folder='.')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    url = data.get('url')
    # ভিডিও ডাউনলোডের সাধারণ লজিক
    return jsonify({"message": f"প্রসেসিং শুরু হয়েছে: {url}"})

if __name__ == '__main__':
    app.run()
