#Lien vers FastAPI =====> http://127.0.0.1:8000/docs#/default/dix_dernier_transactions_dix_dernier_transactions__get

from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI()
con = sqlite3.connect(r"C:\Users\Utilisateur\AppData\Roaming\DBeaverData\workspace6\.metadata\sample-database-sqlite-1\Chinook.db")

def validate_year(year: str):
    if not year.isdigit() or not (len(year) == 4) :
        raise HTTPException(status_code=400, detail="L'année doit être une valeur numérique de 4 chiffres")

    return year
def execute_sql_query(con, query):
    cur = con.cursor()
    cur.execute(query)
    result = cur.fetchall()

    if result is None or len(result) == 0:
        raise HTTPException(status_code=400, detail='Aucune donnée existe pour cette ville ou vérifiez la saisie de votre ville.')

    if any(row[0] is None for row in result):
        return 'Aucune donnée existe pour cette ville'

    if len(result) == 1:
        return result[0][0]
    else:
        return [r[0] for r in result]
def execute_sql_query_3_result_detail(con,query):
    cur = con.cursor()
    cur.execute(query)
    result = cur.fetchall()
    if result is None or len(result) == 0:
        raise HTTPException(status_code=400, detail='La ville ne donne aucun résultat ou vérifiez bien si la saisie de votre ville est bien correcte')
    unique_transactions = set((r[1], r[2], r[0]) for r in result)
    return list(unique_transactions)
def execute_sql_query_2_result_detail(con, query):
    cur = con.cursor()
    cur.execute(query)
    result = cur.fetchall()

    if result is None or len(result) == 0:
        raise HTTPException(status_code=400, detail='Aucune répartition trouvée pour la ville de Marseille en 2022')

    unique_values_col0 = {r[0] for r in result}
    unique_values_col1 = {r[1] for r in result}

    unique_values = list(unique_values_col0 | unique_values_col1)

    return ', '.join(str(val) for val in unique_values)
def execute_sql_query_with_labels(con, query):
    cur = con.cursor()
    cur.execute(query)
    result = cur.fetchall()
    formatted_result = [(f"nombre: {row[0]}", f"departement: {row[1]}") for row in result]    
    return formatted_result

#1
@app.get("/revenu_fiscal_moyen/", description="Consulter le revenu fiscal moyen des foyers d'une ville en France")
async def revenu_fiscal_moyen(year: str, city: str = ""):
    year = validate_year(year)    
    query = f"SELECT revenu_fiscal_moyen, date, ville FROM foyers_fiscaux WHERE date LIKE '%{year}%' AND ville LIKE LOWER('{city}')"
    return execute_sql_query(con, query)

#2
@app.get("/dix_derniere_transactions/", description="Consulter les 10 dernières transactions d'une ville en France")
async def dix_dernier_transactions(city: str):    
    query = f"SELECT ville, id_transaction, date_transaction FROM transactions_sample WHERE LOWER(ville) LIKE LOWER('{city}') ORDER BY date_transaction DESC LIMIT 10"
    return execute_sql_query_3_result_detail(con, query)

#3
@app.get("/nombre_acquisitions/", description="Connaitre le nombre d'acquisitions d'une ville durant l'année 2022")
async def nombre_acquisitions(city: str):
    query = f"SELECT COUNT(*) FROM transactions_sample WHERE ville LIKE LOWER('{city}') AND date_transaction LIKE '%2022%'"
    return execute_sql_query(con,query)

#4
@app.get("/prix_m2/", description="Connaitre le prix au m2 moyen pour les maisons vendues l'année 2022")
async def prix_m2():    
    query = f"SELECT AVG(prix/surface_habitable) FROM transactions_sample WHERE date_transaction LIKE '%2022%' AND type_batiment LIKE LOWER('Maison')"
    return execute_sql_query(con,query)
       
#5
@app.get("/nb_acquisitions_studios_rennes/", description="Connaitre le nombre d'acquisitions de studios de Rennes durant l'année 2022")
async def nb_acquisitions_studios_rennes():    
    query = f"SELECT COUNT(*) FROM transactions_sample WHERE strftime('%Y', date_transaction) = '2022' AND type_batiment = 'Appartement' AND n_pieces = 1 AND ville = 'RENNES'"
    return execute_sql_query(con,query)
    
#6
@app.get("/repartition_app_vendu_a_marseille_en_2022/", description="Connaitre la répartition des appartements vendus (Marseille) durant l'année 2022 en fonction du nombre de pièces")
async def repartition_app_vendu_a_marseille_en_2022():
    query = f"SELECT n_pieces, COUNT(*) AS nombre_appartements_vendus FROM transactions_sample WHERE strftime('%Y', date_transaction) = '2022' AND type_batiment = 'Appartement' AND ville LIKE 'MARSEILLE 1ER%' GROUP BY n_pieces ORDER BY n_pieces ASC"
    return execute_sql_query_2_result_detail(con,query)

#7
@app.get("/prix_m2_avignon_2022/", description="Connaitre le prix au m2 moyen pour les maisons vendues à Avignon l'année 2022")
async def prix_m2_avignon_2022():
    query = f"SELECT AVG(prix / surface_habitable) FROM transactions_sample WHERE strftime('%Y', date_transaction) LIKE '%2022%' AND type_batiment LIKE 'Maison' AND ville LIKE 'AVIGNON%'"
    return execute_sql_query(con,query)

#8
@app.get("/nombre_de_transactions_par_département/", description="Consulter le nombre de transactions (tout type confondu) par département, ordonnées par numéro de département")
async def nombre_de_transactions_par_département():
    query = "SELECT COUNT(*) AS nombres_de_ventes, departement FROM transactions_sample GROUP BY departement ORDER BY departement DESC"
    return execute_sql_query_with_labels(con, query)
    
#9
@app.get("/nombre_total_appartements_2022/", description="Connaitre le nombre total de vente d'appartements en 2022 dans toutes les villes où le revenu fiscal moyen en 2018 est supérieur Ã 70k")
async def nombre_total_appartements_2022():
    query = "SELECT COUNT(*), ts.ville AS ventes FROM transactions_sample ts JOIN foyers_fiscaux ff ON ts.ville = UPPER(ff.ville) WHERE (revenu_fiscal_moyen >= 7000 AND ff.date=2018) AND ts.date_transaction LIKE '%2022%' GROUP BY ts.ville"
    return execute_sql_query_with_labels(con, query)

#10
@app.get("/top10_villes_les_plus_dynamiques_transactions/", description="Consulter le top 10 des villes les plus dynamiques en termes de transactions immobilières")
async def top10_villes_les_plus_dynamiques_transactions():
    query = "SELECT ville, COUNT(*) AS nombre_transactions FROM transactions_sample GROUP BY ville ORDER BY COUNT(*) DESC LIMIT 10"
    return execute_sql_query(con, query)

#11
@app.get("/top10_villes_les_plus_bas_pour_appartements/", description="Accéder aux 10 villes avec un prix au m2 moyen le plus bas pour les appartements")
async def top10_villes_les_plus_bas_pour_appartements():
    query = "SELECT ville, AVG(prix / surface_habitable) AS prix_m2_moyen FROM transactions_sample WHERE type_batiment = 'Appartement' GROUP BY ville ORDER BY prix ASC LIMIT 10"
    return execute_sql_query(con, query)

#12
@app.get("/top10_villes_les_plus_haut_pour_maison/", description="Accéder aux 10 villes avec un prix au m2 moyen le plus haut pour les maisons")
async def top10_villes_les_plus_bas_pour_appartements():
    query = "SELECT ville, AVG(prix / surface_habitable) AS prix_m2_moyen FROM transactions_sample WHERE type_batiment = 'Maison' GROUP BY ville ORDER BY prix ASC LIMIT 10"
    return execute_sql_query(con, query)