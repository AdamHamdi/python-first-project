import sqlite3
def main():
    db=sqlite3.connect("dbase.db")
    db.execute("create table if not exists Admin(name text,age int)")
if __name__ == '__main__':main()
