from flask import Flask, send_from_directory, os

app = Flask(__name__, static_folder='.')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/download_video')
def download_video():
    # ফাইলটি বর্তমান ডিরেক্টরি থেকে সার্ভ করবে
    return send_from_directory(os.getcwd(), 'final_video.mp4')

if __name__ == '__main__':
    app.run()
