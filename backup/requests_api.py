from try_requests import try_req 
import requests
#1 
def rev_fis_avg (years, city ): 
    api_url = "http://127.0.0.1:8000/revenu_fiscal_moyen/"
    params = {"year": "2020", "city": "montpellier"}
    try_req (api_url,params)
    return (test)
#2
api_url = "http://127.0.0.1:8000/dix_derniere_transactions/"
params = { "city": "city"}
#3 
api_url = "http://127.0.0.1:8000/nombre_acquisitions/"
params = { "city": "FIGEAC"}
#4
api_url = "http://127.0.0.1:8000/prix_m2/"
params = {}
#5
api_url = "http://127.0.0.1:8000/nb_acquisitions_studios_rennes/"
params = {"city": "RENNES"}
#6
api_url = "http://127.0.0.1:8000/repartition_app_vendu_a_marseille_en_2022/"
params = {"city": "marseille"}
#7
api_url = "http://127.0.0.1:8000/prix_m2_avignon_2022/"
params = {"city": "AVIGNON"}
#8
api_url = "http://127.0.0.1:8000/nombre_de_transactions_par_département/"
params = {}
#9
api_url = "http://127.0.0.1:8000/nombre_total_appartements_2022/"
params = {}
#10
api_url = "http://127.0.0.1:8000/top10_villes_les_plus_dynamiques_transactions/"
params = {}
#11
api_url = "http://127.0.0.1:8000/top10_villes_les_plus_bas_pour_appartements/"
params = {}
#12
api_url = "http://127.0.0.1:8000/top10_villes_les_plus_haut_pour_maison/"
params = {}





