import mysql.connector
import time

def connection():
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user="userN",
        password="1234",
        autocommit=True)
    return connection


def delete_game(user):
    # delete current game of this user
    kursori = connection.cursor()

    sql = "delete from game where player_id=" + str(user[0])+ ";"
    kursori.execute(sql)


def timer(s):
    for aika in range(s, 0, -1):
        print(aika)
        time.sleep(1)
    print("Aika loppui!")


def timenoprint(s):
    for aika in range(s, 0, -1):
        # print(aika)
        time.sleep(1)
    # print("Aika loppui!")


def options(planeNumber):
    loop = True
    planeNumber = planeNumber
    while loop == True:
        print()
        print("1: Vaihda lentokone")
        print("2: Näytä peliohjeet uudestaan")
        print()
        choice = int(input("Mitä haluaisit tehdä? "))
        if choice == 1:
            planeNumber = choose_plane()
            loop = False
        elif choice == 2:
            peliohjeet()
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
    return planeNumber


def choose_options(plane):
    print()
    option = input("(Paina kirjainta V jos haluat nähdä vaihtoehdot.) ")
    if option == "v" or option == "V":
        plane = options(plane)
    return plane


def save_result(user, time_sec, score, airport):
    yhteys = mysql.connector.connect(
        host='127.0.0.1',  # localhost
        port=3306,  # MariaDB port
        database='flight_game',
        user='userN',
        password='1234',
        autocommit=True)
    kursori = yhteys.cursor()

    # check where airport located
    sql = "select country.continent from country inner join airport" \
          " on country.iso_country=airport.iso_country where airport.ident ='"+airport+"';"
    kursori.execute(sql)
    continent = kursori.fetchone()

    """update player's results
    user[0] - id
    user[1] - time in sec
    user[2] - screen name
    user[3] - score
    user[4] - last_location
    user[5] - AF (afrikka)
    user[6] - AN (antarktikka)
    user[7] - AS (australia)
    user[8] - EU (europa)
    user[9] - NA (north amerika)
    user[10] - OC (australia and ocean) ??? 
    user[11] - SA (south america)
    """
    sql = "update game set last_location='" + str(airport) +"', time_sec=" + str(user[1] + time_sec) + "," \
                           " score=" + str(user[3]+score) + "," \
                           " " + continent[0] +"_=TRUE where player_id=" + str(user[0]) + ";"

    # print(sql)
    kursori.execute(sql)


    # check if all continents were visited
    sql = "select  AF_*AN_*AS_*EU_*NA_*OC_*SA_ from game where player_id=" + str(user[0]) + ";"
    kursori.execute(sql)
    result = kursori.fetchone()
    result = bool(result[0])

    #if result = True all continents were visited, so we need to save result to table result
    if result:
        sql = "select * from game where player_id=" + str(user[0]) + ";"
        kursori.execute(sql)
        user = kursori.fetchone()
        """
        user[0] - id
        user[1] - time in sec
        user[2] - screen name
        user[3] - score
        """
        sql = "insert into results (player_id, screen_name, score, time_sec) " \
              "values ("+str(user[0])+", '" + str(user[2]) + "', " + str(user[3]) + ", " + str(user[1])+ ");"
        kursori.execute(sql)

    return result
