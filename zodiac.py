from flask import Flask, render_template, request

app = Flask(__name__)

#routes 

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('home.html')
    

if __name__ == "__main__":
    app.run(debug=True)