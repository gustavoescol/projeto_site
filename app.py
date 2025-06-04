from flask import Flask
from routes.main_routes import main_bp
from routes.usuario_routes import usuario_bp
from routes.carrinho_routes import carrinho_bp

app = Flask(__name__)

app.register_blueprint(main_bp)
app.register_blueprint(usuario_bp)
app.register_blueprint(carrinho_bp)

if __name__ == '__main__':
    app.run(debug=True)