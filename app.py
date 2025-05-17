import os
import random

from flask import Flask, jsonify, render_template, request, session

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Pares: termo e definição
PAIRS = {
    'Kernel': 'Componente central de um sistema operacional que atua como ponte entre software e hardware.',
    'Processo': 'Instância de um programa em execução, com seu próprio espaço de memória.',
    'Thread': 'Unidade de execução dentro de um processo.',
    'Sistema Operacional': 'Software que gerencia recursos do hardware e oferece serviços para programas.'
}

@app.route("/")
def index():
    session['score'] = 0

    cards = []
    for key, definition in PAIRS.items():
        cards.append({'id': key, 'type': 'key', 'text': key})
        cards.append({'id': key, 'type': 'definition', 'text': definition})

    random.shuffle(cards)
    return render_template("index.html", cards=cards)

@app.route("/score", methods=["POST"])
def update_score():
    data = request.get_json()
    points = data.get("points", 0)
    session['score'] = session.get('score', 0) + points
    return jsonify(score=session['score'])

@app.route("/get_score")
def get_score():
    return jsonify(score=session.get('score', 0))

if __name__ == "__main__":
    app.run(debug=True)