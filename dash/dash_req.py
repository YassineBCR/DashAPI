from api_client import get
import pandas as pd
import requests


racine_api = 'http://127.0.0.1:8000'

def revenu_fiscal_moyen(year: str, city: str):
    try:
        return get(racine_api + '/revenu_fiscal/', params={'year': year, 'city': city})
    except IndexError:
        return None
    except Exception as e:       
        print(f"Une erreur s'est produite : {e}")
        return None
    
def transactions_sample(city: str):
    try:
        return get(racine_api + '/transactions_sample/', params={'city': city})
    except IndexError:
        return None
    except Exception as e:       
        print(f"Une erreur s'est produite : {e}")
        return None

def acquisitions(city: str):
    try:
        return get(racine_api + '/acquisitions/', params={'city': city})
    except IndexError:
        return None
    except Exception as e:       
        print(f"Une erreur s'est produite : {e}")
        return None

def prix_au_metre_carre(city: str):
    try:
        return get(racine_api + '/prix_au_metre_carre/', params={'city': city})
    except IndexError:
        return None
    except Exception as e:       
        print(f"Une erreur s'est produite : {e}")
        return None

def nombre_acquisitions(city: str):
    try:
        return get(racine_api + '/nombre_acquisitions/', params={'city': city})
    except IndexError:
        return None
    except Exception as e:       
        print(f"Une erreur s'est produite : {e}")
        return None

def count_appartments_rooms(city: str):
    try:
        return get(racine_api + '/count_appartments_rooms/', params={'city': city})
    except IndexError:
        return None
    except Exception as e:       
        print(f"Une erreur s'est produite : {e}")
        return None

def avg_prix_par_m2_avignon():
    try:
        return get(racine_api + '/avg_prix_par_m2_avignon/', params={})
    except IndexError:
        return None
    except Exception as e:       
        print(f"Une erreur s'est produite : {e}")
        return None

def transactions_count_by_department(department: str):
    try:
        requests.get (racine_api + "transactions_count_by_department/", params={'department': department})
    except IndexError:
        return None
    except Exception as e:       
        print(f"Une erreur s'est produite : {e}")
        return None

def vente_appart_2k22_foyer_70k(city: str):
    try:
        return get(racine_api + '/vente_appart_2k22_foyer_70k/', params={'city': city})
    except IndexError:
        return None
    except Exception as e:       
        print(f"Une erreur s'est produite : {e}")
        return None

def top_10_ville_dynamic():
    try:
        return get(racine_api + '/top_10_ville_dynamic/', params={})
    except IndexError:
        return None
    except Exception as e:       
        print(f"Une erreur s'est produite : {e}")
        return None

def top_10_prix_plus_bas_par_appart():
    try:
        return get(racine_api + '/top_10_prix_plus_bas_par_appart/', params={})
    except IndexError:
        return None
    except Exception as e:       
        print(f"Une erreur s'est produite : {e}")
        return None

def top_10_prix_plus_haut_par_maison():
    try:
        return get(racine_api + '/top_10_prix_plus_haut_par_maison/', params={})
    except IndexError:
        return None
    except Exception as e:       
        print(f"Une erreur s'est produite : {e}")
        return None
