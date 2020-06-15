import sqlite3
def main():
    db=sqlite3.connect("dbase.db")
    db.row_factory=sqlite3.Row#changer les donner de la base sous dictionary
    db.execute("create table if not exists Admin(name text,age int)")
    db.execute("insert into Admin(name,age)values(?,?)",('Adam',28 ))
    db.execute("insert into Admin(name,age)values(?,?)", ('Gabby', 19))
    db.execute("insert into Admin(name,age)values(?,?)", ('Gabbriella', 19))
    #db.commit() tronsaction refaire les requetes

    cursor=db.execute("select * from Admin")
    for row in cursor:
        print("Name:{},Age:{}".format(row["name"],row["age"]))


if __name__ == '__main__':main()
