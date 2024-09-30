from flask import Flask, render_template, request
from helper import generate_quote


app = Flask(__name__)

# Function to get a motivational quote based on mood
def get_quote(mood):
    return generate_quote(mood)

@app.route('/', methods=['GET', 'POST'])
def index():
    quote = ""
    if request.method == 'POST':
        mood = request.form['mood']
        print(mood)
        quote = get_quote(mood)
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
