import sqlite3


def connection():
    login = sqlite3.connect("books.db")
    aux = login.cursor()
    aux.execute("CREATE TABLE IF NOT EXISTS livre (id INTEGER PRIMARY KEY, titre text, auteur text, annee integer, isbn integer)")
    login.commit()
    login.close()


def ajouter(titre, auteur, annee, isbn):
    login = sqlite3.connect("books.db")
    aux = login.cursor()
    aux.execute("INSERT INTO livre VALUES(NULL, ?,?,?,?)", (titre, auteur, annee, isbn))
    login.commit()
    login.close()


def afficher():
    login = sqlite3.connect("books.db")
    aux = login.cursor()
    aux.execute("SELECT * FROM livre")
    lignes = aux.fetchall()
    login.close()
    return lignes


def chercher(titre="", auteur="", annee="", isbn=""):
    login = sqlite3.connect("books.db")
    aux = login.cursor()
    aux.execute("SELECT * FROM livre WHERE titre=? OR auteur=? OR titre=? OR isbn=?", (titre, auteur, annee, isbn))
    lignes = aux.fetchall()
    login.close()
    login.close()
    return lignes


def supprimer(id):
    login = sqlite3.connect("books.db")
    aux = login.cursor()
    aux.execute("DELETE FROM livre WHERE id=?", (id,))
    login.commit()
    login.close()


def modifier(id, titre, auteur, annee, isbn):
    login = sqlite3.connect("books.db")
    aux = login.cursor()
    aux.execute("UPDATE livre SET titre=?, auteur=?, annee=?, isbn=? WHERE id=?", (titre, auteur, annee, isbn, id))
    login.commit()
    login.close()


#connection()
#ajouter("bonjour", "hjdv", 120, 4555201)
#modifier(1, "balafon", "engelbert mveng", 1980, 45896217)
#supprimer(3)
#print(chercher(annee=2004))
#afficher()
#print(afficher())