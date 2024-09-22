from flask import Flask, render_template
from routes.bfhl import bfhl_api

app = Flask(__name__)

# Register blueprint
app.register_blueprint(bfhl_api)

# Route for serving index.html (optional frontend)
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)