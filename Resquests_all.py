from api_client import get

racine_api = 'http://127.0.0.1:8000'

def revenu_fiscal_moyen(year: str, city: str):
    try:
        return get(racine_api + '/revenu_fiscal_moyen/', params={'year': year, 'city': city})
    except IndexError:
        return None
    except Exception as e:       
        print(f"Une erreur s'est produite : {e}")
        return None

def dix_derniere_transactions(city: str):
    try:
        return get(racine_api + '/dix_derniere_transactions/', params={'city': city})
    except Exception as e:
        print(str(e))

def nombre_acquisitions(city: str):
    try:
        return get(racine_api + '/dix_derniere_transactions/', params={'city': city})
    except Exception as e:
        print(str(e))

def prix_m2_2022(city: str):
    try:
        return get(racine_api + '/dix_derniere_transactions/', params={'city': city})
    except Exception as e:
        print(str(e))

