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
    if not url:
        return jsonify({"message": "লিংক পাওয়া যায়নি!"})
    
    # এখানে ভিডিও ডাউনলোডের কাজ হবে
    return jsonify({"message": "সফলভাবে ডাউনলোড ও এডিট হয়েছে!"})

if __name__ == '__main__':
    app.run()
