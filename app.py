from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/acesso', methods=['POST'])
def acesso():
    username = request.form['username']
    password = request.form['password']
   
    if username == 'gabriel@' and password == '123':
        return redirect('/servicos')
    else:
        print('Usuário não encontrado')
        return "Usuário ou senha incorretos", 401

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/servicos')
def servicos():
    return render_template('servicos.html')


@app.route('/add_cadastro')
def add_cadastro():
    email = request.form['email']
    nome = request.form['nome']
    senha = request.form['password']
    endereco = request.form['endereco']
    telefone = request.form['telefone']

    print(f"cadastro realizado com sucesso: {email}, {nome}, {senha}, {endereco}, {telefone}")
    return redirect('/servicos')

if __name__ == '__main__':
    app.run(debug=True)