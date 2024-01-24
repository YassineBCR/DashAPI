# request.py

from api_client import get
import pandas as pd

racine_api = 'http://127.0.0.1:8000'

def revenu_fiscal_moyen(year: str, city: str):
    try:
        return get(racine_api + '/revenu_fiscal/', params={'year': year, 'city': city})
    except IndexError:
        return None
    except Exception as e:       
        print(f"Une erreur s'est produite : {e}")
        return None