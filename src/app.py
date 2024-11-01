import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Read secrets from Docker Secrets Path
def get_secret(file_path):
    with open(file_path) as f:
        return f.read().strip()
    
db_user = get_secret('/run/secrets/db_user')
db_password = get_secret('/run/secrets/db_password')
db_host = 'db'
db_name = 'quotes_db'

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Quote model
class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)

# Create the database and the table
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        quote_content = request.form['quote']
        if quote_content:
            new_quote = Quote(content=quote_content)
            db.session.add(new_quote)
            db.session.commit()
            return redirect(url_for('index'))

    quotes = Quote.query.all()
    return render_template('index.html', quotes=quotes)

if __name__ == '__main__':
    app.run(host='0.0.0.0/0', debug=True)
