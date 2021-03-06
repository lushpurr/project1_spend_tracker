from db.run_sql import run_sql
from models.tag import Tag

def save(tag):
    sql = "INSERT INTO tags( category, active ) VALUES ( %s, %s ) RETURNING id"
    values = [tag.category, tag.active]
    results = run_sql( sql, values )
    tag.id = results[0]['id']
    return tag


def select_all():
    tags = []

    sql = "SELECT * FROM tags"
    results = run_sql(sql)

    for row in results:
        tag = Tag(row['category'], row['active'], row['id'])
        tags.append(tag)
    return tags


def select(id):
    tag = None
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        tag = Tag(result['category'], result['active'], result['id'] )
    return tag


def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM tags WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(tag):
    sql = "UPDATE tags SET ( category, active ) = ( %s, %s ) WHERE id = %s"
    values = [tag.category, tag.active, tag.id]
    run_sql(sql, values)


def get_categories():
    sql = "SELECT DISTINCT category FROM tags"
    results=run_sql(sql)
    return [category[0] for category in results]