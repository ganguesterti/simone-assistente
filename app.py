from flask import Flask, request, jsonify

app = Flask(__name__)

def responder_mensagem(texto):
    texto = texto.lower()
    if "oi" in texto:
        return "Oi, chefe! A Simone tá aqui, ativa! 💬"
    elif "saldo" in texto:
        return "Seu saldo hoje é R$ 1.234,56"
    elif "venda" in texto:
        return "Venda anotada com sucesso! 🧾"
    elif "lembrar" in texto:
        return "Lembrete criado, chefe! Te aviso no horário certo. ⏰"
    else:
        return "Não entendi, chefe. Pode repetir de outro jeito? 🤖"

@app.route("/api/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("[WEBHOOK] Recebido:", data)

    if not data or "message" not in data:
        return jsonify({"status": "ignorado"})

    mensagem = data.get("message")
    numero = data.get("phone")
    resposta = responder_mensagem(mensagem)

    print(f"[Simone] Respondendo para {numero}: {resposta}")
    return jsonify({"status": "ok", "resposta": resposta})

@app.route('/saúde')
def health_check():
    return "OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)

