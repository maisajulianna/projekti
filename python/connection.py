import mysql.connector


def connection():
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user="userN",
        password="1234",
        autocommit=True)
    return connection
