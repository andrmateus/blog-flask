from sqlite3.dbapi2 import connect, register_converter
import bibliotecas as b

db = 'database/db-blog.db'
dataCriacao = b.date.today()
def insert(descricao, titulo):
    try:
        conn = b.sqlite3.connect(db)
        sql = 'INSERT INTO topico (descricao, data, titulo) VALUES (?, ?, ?)'

        registro = (descricao, dataCriacao, titulo)

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
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
    finally:
        conn.close()

def selectCamp(id):
    try:
        conn = b.sqlite3.connect(db)
        sql = 'SELECT descricao, titulo FROM topico WHERE idtopicos = %s' % id
        cur = conn.cursor()
        cur.execute(sql)
        regs = cur.fetchall()
        for r in regs:
            descricao = r[0]
            titulo = r[1]
        return(descricao, titulo, id)
        
    finally:
        conn.close()

def edita(titulo, descricao, id):
    try:
        conn = b.sqlite3.connect(db)
        sql = "update topico set titulo = ?, descricao = ? where idtopicos = ?"
        registro = (titulo, descricao, id)
        cur = conn.cursor()
        cur.execute(sql, registro)
        conn.commit()
    finally:
        conn.close()