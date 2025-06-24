from flask import Flask, request, render_template
from chatbot_engine import ask_ai

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ""
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            response = ask_ai(query)
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
