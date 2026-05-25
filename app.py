from flask import Flask, send_from_directory, render_template

app = Flask(__name__, static_folder='.')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/final_video.mp4')
def serve_video():
    return send_from_directory('.', 'final_video.mp4')

if __name__ == '__main__':
    app.run()
