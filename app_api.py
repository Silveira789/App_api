"""
API --> Lugar para disponibilizar recursos e/ou funcionalidades

    * Objetivos - Criar uma api que disponibiliza consulta, criação, edição e exclusão de livros
    * URL Base  - Local onde realiza as requisições
        --> localhost
    * Endpoints - Funcionalidades (Verbos) disponibilizados pela API
        --> Consulta:       localhost/livros    (GET)           - Consultar livros
        --> Criação:       localhost/livros     (POST)          - Criar novos livros
        --> Consulta:       localhost/livros    (GET)           - Consulta por id
        --> Modificação:    localhost/livro/id  (PUT)           - Modificação de um livro por id
        --> Excluir:        localhost/livro/id  (DELETE)        - Excluir livro por id

    * Recursos (ou Funcionalidades) - Livros




Requisitos:
    - Postman
    - pip install flask
    -
"""

from flask import Flask, jsonify, request

# Flask --> servidor
# jsonify --> formato de retorno de dados
# request --> acesso de dados

app_api = Flask(__name__)

livros = [

    {
        'id': 1,
        'título': 'Moby Dick',
        'autor': 'Herman Melville'

    },

    {
        'id': 2,
        'título': 'Guerra e Paz',
        'autor': 'Liev Tolstói'

    },

    {
        'id': 3,
        'título': 'O código da Vinci',
        'autor': 'Dan Brown'

    }

]


# 1° Criar funcionalidades

# Consultar (todos)
@app_api.route("/livros", methods=['GET'])  # Indica qual o caminho (endpoint/url) para acesso ao local
def obter_livros():
    return livros


# OBS: methods especifica qual método pertencente ao endpoint


# Consultar (id)
@app_api.route("/livros/<int:id>", methods=['GET'])  # Indica qual o caminho (endpoint/url) para acesso ao local
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)


# Editar
@app_api.route("/livros/<int:id>", methods=['PUT'])  # Indica qual o caminho (endpoint/url) para acesso ao local
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indicie, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indicie].update(livro_alterado)
            return jsonify(livros[indicie])


# Criar
@app_api.route("/livros", methods=['POST'])  # Indica qual o caminho (endpoint/url) para acesso ao local
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)


# Excluir
@app_api.route("/livros/<int:id>", methods=['DELETE'])  # Indica qual o caminho (endpoint/url) para acesso ao local
def excluir_livro(id):
    for indicie, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indicie]

    return jsonify(livros)


# Executando a aplicação
app_api.run(port=5000, host='localhost', debug=True)
