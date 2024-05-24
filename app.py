from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/check_news', methods=['POST'])
def check_news():
    headline = request.form['headline']
    plot = request.form['plot']

    # Dummy check (replace with your actual authenticity check logic)
    if 'fake' in headline.lower() or 'fake' in plot.lower():
        result = "This news is incorrect"
        color = "red"
    else:
        result = "This news is authentic"
        color = "green"

    return render_template("result.html", result=result, color=color)


if __name__ == '__main__':
    app.run()
