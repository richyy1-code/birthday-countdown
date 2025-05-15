from flask import Flask, render_template
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
    # Send current time and birthday info to the webpage
    now = datetime.now()
    birthday = datetime(now.year, 5, 26)
    # If birthday passed, use next year
    if now > birthday:
        birthday = birthday.replace(year=now.year + 1)

    return render_template("index.html", now=now, birthday=birthday)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
