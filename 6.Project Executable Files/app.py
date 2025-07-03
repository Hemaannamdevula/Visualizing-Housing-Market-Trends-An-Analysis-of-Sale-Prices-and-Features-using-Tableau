from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')  # Tableau JS embed is already in HTML

@app.route('/story')
def story():
    return render_template('story.html')      # Tableau JS embed is already in HTML

if __name__ == '__main__':
    app.run(debug=True)
