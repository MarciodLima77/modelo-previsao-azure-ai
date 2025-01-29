import requests
import json

# URL do endpoint (substituir pela URL real do meu endpoint no Azure ou outro serviço)
endpoint = 'https://seu-endpoint.azure.com/predict'

# Cabeçalhos necessários para a requisição (adaptar conforme necessário)
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer meu_token_de_autenticacao'  # Adapte se necessário
}

# Dados de entrada para previsão (ajustar conforme o modelo que criei)
data = {
    "input_data": [
        {"feature1": valor1, "feature2": valor2, "feature3": valor3}  # Substituir com meus dados
    ]
}

# Converte os dados para JSON
data_json = json.dumps(data)

# Envia a requisição POST para o endpoint
response = requests.post(endpoint, headers=headers, data=data_json)

# Exibe a resposta (previsão)
if response.status_code == 200:
    print("Previsão recebida com sucesso:")
    print(response.json())
else:
    print(f"Erro ao fazer a previsão: {response.status_code}")
    print(response.text)
