from flask import Flask, render_template
from flask_cors import CORS
from database import init_db
from routes.deals import deals_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(deals_bp, url_prefix='/api')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)