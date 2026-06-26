from flask import Flask, render_template, request
import random

tentativas = 0

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/jogo', methods=['GET', 'POST'])
def jogo():

    global tentativas
    acertou = None
    numero = random.randint(1, 100)

    if request.method == 'POST':
        numForm = int(request.form['numForm'])

        if numero == numForm:
            tentativas = 0
            acertou = True
        else:
            tentativas += 1
            acertou = False

    return render_template('jogo.html', acertou=acertou, tentativas=tentativas)


if __name__ == '__main__':
    app.run(debug=True)
