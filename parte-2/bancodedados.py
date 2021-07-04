import sqlite3 as sql

class TransactionObject():
    database    = "anuncios.db"
    conn        = None
    cur         = None
    connected   = False

    def connect(self):
        TransactionObject.conn      = sql.connect(TransactionObject.database)
        TransactionObject.cur       = TransactionObject.conn.cursor()
        TransactionObject.connected = True

    def disconnect(self):
        TransactionObject.conn.close()
        TransactionObject.connected = False

    def execute(self, sql, parms = None):
        if TransactionObject.connected:
            if parms == None:
                TransactionObject.cur.execute(sql)
            else:
                TransactionObject.cur.execute(sql, parms)
            return True
        else:
            return False

    def fetchall(self):
        return TransactionObject.cur.fetchall()

    def persist(self):
        if TransactionObject.connected:
            TransactionObject.conn.commit()
            return True
        else:
            return False



def initDB():
    trans = TransactionObject()
    trans.connect()
    trans.execute("CREATE TABLE IF NOT EXISTS anuncios (id INTEGER PRIMARY KEY , anuncio TEXT, cliente TEXT, dataInicio TEXT, dataTermino TEXT, investimento TEXT)")
    trans.persist()
    trans.disconnect()

def insert(anuncio, cliente, dataInicio, dataTermino, investimento):
    trans = TransactionObject()
    trans.connect()
    trans.execute("INSERT INTO anuncios VALUES(NULL, ?,?,?,?,?)", (anuncio, cliente, dataInicio, dataTermino, investimento))
    trans.persist()
    trans.disconnect()


def view():
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM anuncios")
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def search(anuncio="", cliente="", dataInicio="", dataTermino="", investimento=""):
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM anuncios WHERE anuncio=? or cliente=? or dataInicio=? or dataTermino=? or investimento=?", (anuncio, cliente, dataInicio, dataTermino, investimento))
    rows = trans.fetchall()
    trans.disconnect()
    return rows


def delete(id):
    trans = TransactionObject()
    trans.connect()
    trans.execute("DELETE FROM anuncios WHERE id = ?", (id,))
    trans.persist()
    trans.disconnect()

def update(id, anuncio, cliente, dataInicio, dataTermino, investimento):
    trans = TransactionObject()
    trans.connect()
    trans.execute("UPDATE anuncios SET anuncio=?, cliente=?, dataInicio=?, dataTermino=?, investimento=? WHERE id = ?",(anuncio, cliente, dataInicio, dataTermino, investimento, id))
    trans.persist()
    trans.disconnect()

initDB()


