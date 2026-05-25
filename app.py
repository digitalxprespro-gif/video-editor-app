from flask import Flask, request, jsonify, send_from_directory
import yt_dlp
from moviepy.editor import VideoFileClip
import os

app = Flask(__name__, static_folder='.')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    url = data.get('url')
    
    # ১. ডাউনলোড
    ydl_opts = {'outtmpl': 'video.mp4'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    # ২. এডিটিং (কপিরাইট এড়াতে পিচ চেঞ্জ ও ট্রানজিশন)
    video = VideoFileClip("video.mp4")
    # অডিও পিচ পরিবর্তন (কপিরাইট ফ্রি করার জন্য)
    new_audio = video.audio.fx(lambda a: a.speedx(1.05)) 
    video = video.set_audio(new_audio)
    
    video.write_videofile("final_video.mp4", codec="libx264", audio_codec="aac")
    
    return jsonify({"message": "সম্পন্ন হয়েছে!"})

if __name__ == '__main__':
    app.run()
