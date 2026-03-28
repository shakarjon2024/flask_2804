from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/colors')
def colors_page():
    return render_template('colors.html', colors=colors)


if __name__ == '__main__':
    app.run(debug=True)
