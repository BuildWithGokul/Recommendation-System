from flask import Flask, request, render_template

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template("index.html")

# Recommendation route
@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.form['user_input']
    mode = request.form['mode']

    if mode == 'collaborative':
        recommendations = [f"Collaborative Recommendation {i}" for i in range(1, 6)]
    else:
        recommendations = [f"Content-Based Recommendation {i}" for i in range(1, 6)]

    return render_template('index.html', recommendations=recommendations)

# Localhost run only
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
