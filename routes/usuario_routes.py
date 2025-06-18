from flask import Blueprint, render_template, request, redirect, session, url_for

usuario_bp = Blueprint('usuario', __name__)

USERS = {
    'gustavo': "lindinho" }

@usuario_bp.route('/login')
def login():
    return render_template('login.html')

@usuario_bp.route('/servicos')
def servicos():
    return render_template('servicos.html', nomeuser = "Gustavo")

@usuario_bp.route('/acesso', methods=['POST'])
def acesso():
    username = request.form['username']
    password = request.form['password']


    session['usuario'] = username

    if username in USERS and USERS[username] == password:
        session['usuario'] = username
        return redirect(url_for('usuario.servicos'))
    else:
        session.pop('usuario', None)
        return 'Usuário ou senha inválidos', 401

@usuario_bp.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@usuario_bp.route('/add_cadastro', methods=['POST'])
def add_cadastro():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    endereco = request.form.get('endereco')
    datanasc = request.form.get('datanasc')
    cpf = request.form.get('cpf')

    session['usuario'] = {
        'nome': nome,
        'email': email,
        'senha': senha,
        'endereco': endereco,
        'datanasc': datanasc,
        'cpf': cpf
 
    }