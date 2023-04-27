import mysql.connector
import time
import choises
import start


def connection():
    connection_ = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user="userN",
        password="1234",
        autocommit=True)
    return connection_


connection = connection()


def delete_game(user):
    # delete current game of this user
    cursor = connection.cursor()
    sql = f"delete from game where player_id = {user[0]}"
    cursor.execute(sql)


def options(plane_nr):
    loop = True
    plane_nr = plane_nr
    while loop:
        print()
        print("1: Vaihda lentokone")
        print("2: Näytä peliohjeet uudestaan")
        print()
        choice = int(input("Mitä haluaisit tehdä? "))
        if choice == 1:
            plane_nr = choises.choose_plane()
            loop = False
        elif choice == 2:
            start.peliohjeet()
            loop = False
        else:
            print()
            print("Virheellinen arvo.")
            loop = input("Paina 1 jos haluat jatkaa valitsemista, 2 jos haluat lopettaa. ")
            if loop == "1":
                loop = True
            elif loop == "2":
                print("Prosessi lopetettu.")
                loop = False
    return plane_nr


def choose_options(plane):
    print()
    option = input("(Paina kirjainta V jos haluat nähdä vaihtoehdot.) ").lower()
    if option == "v":
        plane = options(plane)
    return plane


def save_result(user, time_sec, score, airport):
    # check where airport located
    sql = "SELECT country.continent FROM country INNER JOIN airport" \
          " ON country.iso_country=airport.iso_country WHERE airport.ident ='"+airport+"';"
    cursor = connection.cursor()
    cursor.execute(sql)
    continent = cursor.fetchone()

    """update player's results
    user[0] - id
    user[1] - time in sec
    user[2] - screen name
    user[3] - score
    user[4] - last_location
    user[5] - AF (Afrikka)
    user[6] - AN (Etelä-Manner)
    user[7] - AS (Aasia)
    user[8] - EU (Eurooppa)
    user[9] - NA (Pohjois-Amerikka)
    user[10] - OC (Australia ja Oseania)
    user[11] - SA (Etelä-Amerikka)
    """
    sql = "UPDATE game SET last_location = '" + str(airport) +"', time_sec = " + str(user[1] + time_sec) + \
                           ", score = " + str(user[3]+score) + "," \
                           + continent[0] + " = TRUE WHERE player_id = " + str(user[0])

    # print(sql)
    cursor.execute(sql)

    # check if all continents were visited
    sql = "SELECT  AF_ * AN_ * AS_ * EU_ * NA_ * OC_ * SA_ FROM game WHERE player_id = " + str(user[0])
    cursor.execute(sql)
    result = cursor.fetchone()
    result = bool(result[0])

    #if result = True all continents were visited, so we need to save result to table result
    if result:
        sql = "SELECT * FROM game WHERE player_id = " + str(user[0])
        cursor.execute(sql)
        user = cursor.fetchone()
        """
        user[0] - id
        user[1] - time in sec
        user[2] - screen name
        user[3] - score
        """
        sql = "INSERT INTO results (player_id, screen_name, score, time_sec) " \
              "values ("+str(user[0])+", '" + str(user[2]) + "', " + str(user[3]) + ", " + str(user[1]) + ");"
        cursor.execute(sql)

    return result
