import requests

# URL de l'API que vous souhaitez interroger
api_url = "http://127.0.0.1:8000/revenu_fiscal_moyen/"

# Paramètres que vous devez inclure dans la requête
params = {"year": "2020", "city": "montpellier"}


try:
    # Effectuer une requête GET
    response = requests.get(api_url, params=params)

    # Afficher le code d'état HTTP
    print("Code d'état HTTP :", response.status_code)

    # Afficher la réponse brute
    print("Réponse brute de l'API :", response.text)

    # Vérifier si la requête a réussi (code de statut HTTP 200)
    if response.status_code == 200:
        # Afficher la réponse de l'API (souvent au format JSON)
        print("Réponse de l'API :")
        print(response.json())
    else:
        # Afficher un message d'erreur si la requête a échoué
        print(f"La requête a échoué avec le code de statut {response.status_code}")

except requests.RequestException as e:
    # Gérer les erreurs liées à la requête
    print(f"Une erreur de requête s'est produite : {e}")
