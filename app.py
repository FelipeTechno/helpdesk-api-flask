from flask import Flask, jsonify
from database import db
from routes.chamados import chamados_bp

app = Flask(__name__)

# Config SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///helpdesk.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Criar tabelas
with app.app_context():
    db.create_all()

app.register_blueprint(chamados_bp)


@app.get("/ping")
def ping():
    return jsonify(status="ok", project="HelpDesk API")


if __name__ == "__main__":
    app.run(debug=True)
