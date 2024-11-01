from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://defaultuser:defaultpassword@localhost:5432/defaultdb')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Quotes model
class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<Quote {self.text}>"

def create_tables():
    with app.app_context():
        db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        quote_text = request.form["quote"]
        if quote_text:
            new_quote = Quote(text=quote_text)
            db.session.add(new_quote)
            db.session.commit()
        return redirect(url_for('index'))
    else:
        quotes = Quote.query.all()
        return render_template("index.html", quotes=quotes)

if __name__ == "__main__":
    create_tables()
    print("Table created successfully!!!")
    app.run(host="0.0.0.0", debug=True)
