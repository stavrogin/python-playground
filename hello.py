import requests

# Cerchiamo i dati di Pikachu
pokemon = "pikachu"
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

try:
    response = requests.get(url)
    response.raise_for_status() # Controlla se ci sono errori HTTP
    data = response.json()
    
    nome = data['name'].capitalize()
    tipo = data['types'][0]['type']['name']
    print(f"Nome: {nome} | Tipo principale: {tipo}")

except Exception as e:
    print(f"Si è verificato un errore: {e}")