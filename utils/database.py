from utils.database_connection import DatabaseConnection
import sqlite3

database = 'data.db'


def createDatabase():
    with DatabaseConnection(database) as connection:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS goods(type text, name text, city text, price integer)")


def updateAll(file):
    _clearDate()
    createDatabase()
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        for line in lines:
            print(line)
            type, name, city, price = line.split(':#: ')
            addOne(type, name, city, price)


def seeAll():
    with DatabaseConnection(database) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM goods")
        goods = cursor.fetchall()

    for good in goods:
        print(good)


def addOne(type, name, city, price):
    with DatabaseConnection(database) as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO goods VALUES(?, ?, ?, ?)",
                       (type, name, city, price))


def _clearDate():
    with DatabaseConnection(database) as connection:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE goods")