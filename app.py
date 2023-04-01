from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text_input = request.form['text_input']
        # Process the text input here using OpenAI API
        # ...
        return render_template('index.html', text_input=text_input)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
