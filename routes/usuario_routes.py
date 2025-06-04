from flask import Blueprint, render_template, request, redirect, session, url_for

usuario_bp = Blueprint('usuarios', __name__)

@usuario_bp.route('/login')
def login():
    return render_template('login.html')

@usuario_bp.route('/acesso', methods=['POST'])
def acesso():
    email = request.form.get('email')
    senha = request.form.get('senha')

    if email == 'gustavo@' and senha == '123':
        return redirect('/servicos')
    else:
        print('usuario nao encontrado')
        return "Usuário não encontrado", 404

@usuario_bp.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@usuario_bp.route('/add_cadastro', methods=['POST'])
def add_cadastro():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')

    session['usuario'] = {
        'email': email,
 
    }