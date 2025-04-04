from flask import Flask, request, jsonify
import pyautogui
import os

app = Flask(__name__)

@app.route("/comando", methods=["POST"])
def executar_comando():
    dados = request.json
    acao = dados.get("acao")
    valor = dados.get("valor")

    if acao == "digitar":
        pyautogui.write(valor)
        pyautogui.press("enter")

    elif acao == "abrir_app":
        os.system(f"start {valor}")

    elif acao == "teclado_virtual":
        os.system("osk.exe")

    return jsonify({"status": "Comando executado!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
