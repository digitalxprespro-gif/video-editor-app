from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='.')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/download_video')
def download_video():
    # এখানে আপনার এডিট করা ভিডিও ফাইলটি থাকতে হবে
    return send_from_directory('.', 'final_video.mp4')

if __name__ == '__main__':
    app.run()
