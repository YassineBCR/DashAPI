from fastapi import FastAPI, HTTPException, Depends
import sqlite3
import uvicorn

app = FastAPI()

# database = r"C:\Github\OLV\briefs\B7\data\db_immo.db"
database = r"data\db_immo.db"
con = sqlite3.connect(database)
cur = con.cursor()

queries = {
    "1": {
        "GET":
        "sql": "SELECT revenu_fiscal_moyen, date, ville FROM foyers_fiscaux WHERE date = {year} AND ville = '{city}'",
        "description": "En tant qu'Agent je veux pouvoir consulter le revenu fiscal moyen des foyers de ma ville (Montpellier)"
    },
    "2": {
        "sql": "SELECT * FROM transactions_sample ts WHERE ville ='{city}' ORDER BY date_transaction DESC LIMIT 10",
        "description": "En tant qu'Agent je veux consulter les 10 dernières transactions dans ma ville (Lyon)"
    },
    "3": {
        "sql": "SELECT COUNT(id_transaction) FROM transactions_sample ts WHERE ville = '{city}' AND date_transaction LIKE '2022%';",
        "description": "En tant qu'Agent je souhaite connaitre le nombre d'acquisitions dans ma ville (Paris) durant l'année 2022"
    },
    "4": {
        "sql": "SELECT AVG(prix / surface_habitable) AS prix_m2_moyen FROM transactions_sample WHERE type_batiment = 'Maison' AND date_transaction LIKE '{year}%' ;",
        "description": "En tant qu'Agent je souhaite connaitre le prix au m2 moyen pour les maisons vendues l'année 2022"
    },
    "5": {
        "sql": "SELECT COUNT(*) AS nombre_acquisitions_studios FROM transactions_sample WHERE ville = '{city}' AND type_batiment = 'Studio' AND date_transaction LIKE '{year}%' ;",
        "description": "En tant qu'Agent je souhaite connaitre le nombre d'acquisitions de studios dans ma ville (Rennes) durant l'année 2022"
    },
    "6": {
        "sql": "SELECT n_pieces, COUNT(*) AS nombre_appartements FROM transactions_sample WHERE ville LIKE '{city}' AND type_batiment = 'Appartement' AND date_transaction LIKE '{year}%' GROUP BY n_pieces ORDER BY n_pieces;",
        "description": "En tant qu'Agent je souhaite connaitre la répartition des appartements vendus (à Marseille) durant l'année 2022 en fonction du nombre de pièces"
    },
    "7": {
        "sql": "SELECT AVG(prix / surface_habitable) AS prix_m2_moyen FROM transactions_sample WHERE ville LIKE '{city}' AND type_batiment = 'Maison' AND date_transaction LIKE '{year}%' ;",
        "description": "En tant qu'Agent je souhaite connaitre le prix au m2 moyen pour les maisons vendues à Avignon l'année 2022"
    },
    "8": {
        "sql": "SELECT departement, COUNT(*) AS nombre_transactions FROM transactions_sample GROUP BY departement ORDER BY nombre_transactions DESC;",
        "description": "En tant que CEO, je veux consulter le nombre de transactions (tout type confondu) par département, ordonnées par ordre décroissant"
    },
    "9": {
        "sql": "SELECT COUNT(*) AS nombre_total_ventes FROM transactions_sample WHERE ville IN (SELECT ville FROM foyers_fiscaux WHERE revenu_fiscal_moyen > 70000 AND date = 2018) AND type_batiment = 'Appartement' AND date_transaction LIKE {year} ;",
        "description": "En tant que CEO je souhaite connaitre le nombre total de vente d'appartements en 2022 dans toutes les villes où le revenu fiscal moyen en 2018 est supérieur à 70k"
    }
}

def validate_year(year: str):
    if not year.isdigit() or not (len(year) == 4):
        raise HTTPException(status_code=400, detail="L'année doit être une valeur numérique de 4 chiffres")

    return year

def execute_query(query_id: str, **params):
    req = queries[query_id]["sql"].format(**params)
    cur.execute(req)
    result = cur.fetchall()
    print(result)
    return result

@app.get("/revenu_fiscal_moyen/", description=queries["1"]["description"])
async def revenu_fiscal_moyen(year: str = Depends(validate_year), city: str = ""):
    return execute_query("1", year=year, city=city)[0]

@app.get("/transactions/", description=queries["2"]["description"])
async def transactions_sample(city: str = ""):
    return execute_query("2", city=city)[0]

@app.get("/acquisitions/", description=queries["3"]["description"])
async def acquisitions(city: str = ""):
    return execute_query("3", city=city)[0]

@app.get("/prix au m2 moyen/", description=queries["4"]["description"])
async def acquisitions(year: str = Depends(validate_year)):
    return execute_query("4", year=year)[0]

@app.get("/nombre d'acquisitions de studios dans ma ville/", description=queries["5"]["description"])
async def revenu_fiscal_moyen(year: str = Depends(validate_year), city: str = ""):
    return execute_query("5", year=year, city=city)[0][0]

@app.get("/repartition des appartements vendus (à Marseille)/", description=queries["6"]["description"])
async def revenu_fiscal_moyen(year: str = Depends(validate_year), city: str = ""):
    return execute_query("6", year=year, city=city)[0][0]

@app.get("/prix au m2 moyen pour les maisons vendues /", description=queries["7"]["description"])
async def revenu_fiscal_moyen(year: str = Depends(validate_year), city: str = ""):
    return execute_query("7", year=year, city=city)[0][0]

@app.get("/nombre de transactions (tout type confondu) par département/", description=queries["8"]["description"])
async def transactions_sample():
    return execute_query("8")[0]


uvicorn.run(app)
