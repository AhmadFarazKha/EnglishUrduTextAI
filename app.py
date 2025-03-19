from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load AI model (Windows path compatible)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.route('/', methods=['GET', 'POST'])
def home():
    summary = ""
    if request.method == 'POST':
        text = request.form['text']
        summary = summarizer(text, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)