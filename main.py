from senha import API_KEY
import requests
import json

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"

body_mensagem = {
    "model": id_modelo,
    "messages": [{"role": "user", "content": "escreva um email para meu chefe a previsão do dolar nos proximos meses"}]
}

body_mensagem = json.dumps(body_mensagem)

requisicao = requests.post(link, headers=headers, data=body_mensagem)

print(requisicao)
print(requisicao.text)
#resposta = requisicao.json()

mensagem = resposta["choices"][0]["message"]["content"]





