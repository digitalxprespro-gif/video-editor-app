from flask import Flask, request, jsonify, send_from_directory
import yt_dlp
import os

app = Flask(__name__, static_folder='.')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    video_url = data.get('url')
    
    if not video_url:
        return jsonify({"message": "অনুগ্রহ করে লিংক দিন!"})

    try:
        # yt_dlp কনফিগারেশন
        ydl_opts = {'format': 'best'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            video_title = info.get('title', 'video')
            # এখানে ডাউনলোডের পরবর্তী কাজ যুক্ত হবে
        return jsonify({"message": f"সাফল্যের সাথে পাওয়া গেল: {video_title}"})
    except Exception as e:
        return jsonify({"message": f"ত্রুটি হয়েছে: {str(e)}"})

if __name__ == '__main__':
    app.run()
