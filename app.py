from flask import Flask, render_template_string

app = Flask(__name__)

html_code = open("index.html").read()

@app.route("/")
def home():
    return render_template_string(html_code)

if __name__ == "__main__":
    app.run(debug=True)
