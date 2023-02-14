from db.run_sql import run_sql

from models.artist import Artist

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING id"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def delete_all():
    sql = "DELETE FROM artists"
    results = run_sql(sql)
    return results