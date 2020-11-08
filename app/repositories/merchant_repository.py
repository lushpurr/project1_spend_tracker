from db.run_sql import run_sql
from models.merchant import Merchant

def save(merchant):
    sql = "INSERT INTO merchants( name, city ) VALUES ( %s, %s ) RETURNING id"
    values = [merchant.name, merchant.city]
    results = run_sql( sql, values )
    merchant.id = results[0]['id']
    return merchant


def select_all():
    merchants = []

    sql = "SELECT * FROM merchants"
    results = run_sql(sql)

    for row in results:
        merchant = Merchant(row['name'], row['city'], row['id'])
        merchants.append(merchant)
    return merchants


def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = Merchant(result['name'], result['city'], result['id'] )
    return merchant


def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)
