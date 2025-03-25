from flask import Flask, request

app = Flask(__name__)

alunos = [
    {"id": 1, "nome": "john"},
    {"id": 2, "nome": "roblox"}
]

@app.route('/<id>', methods=["GET"])
def metodo_get_por_id(id):
    for aluno in alunos:
        if aluno["id"] == id:
            return aluno
        return {}

@app.route('/', methods=["POST"])
def metodo_post():
    dados_recebidos = request.get_json()
    alunos.append(
        {"nome": dados_recebidos["nome"]}
    )
    return {"message": "ok"}

@app.route('/', methods=['PUT'])
def metodo_put():
    return 'metodo put'

@app.route('/', methods=['DELETE'])
def metodo_delete():
    return 'metodo delete'