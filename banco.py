from sqlite3.dbapi2 import connect, register_converter
import bibliotecas as b

db = 'database/db-blog.db'
dataCriacao = b.date.today()
def insert(descricao):
    try:
        conn = b.sqlite3.connect(db)
        sql = 'INSERT INTO topico (descricao, data) VALUES (?, ?)'

        registro = (descricao, dataCriacao)

        cur = conn.cursor()

        cur.execute(sql,registro)

        conn.commit()

    except b.Error as e:
        print(e)
    finally:
        conn.close()


def list():
    try:
        conn = b.sqlite3.connect(db)
        sql = 'SELECT * FROM topico'

        cur = conn.cursor()
        cur.execute(sql)
        registros = cur.fetchall()
        return registros
    except b.Error as e:
        return e
    finally:
        conn.close()

def delete(id):
    try:
        conn = b.sqlite3.connect(db)
        sql = 'DELETE FROM topico WHERE idtopicos = %s' % id
        registro = (id)
        cur = conn.cursor()

        cur.execute(sql)

        conn.commit()
    finally:
        conn.close()

def selectCamp(id):
    
    return 