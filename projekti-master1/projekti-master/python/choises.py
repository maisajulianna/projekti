import misc
import connection
import colorama
import time
from colorama import Fore, Style

connection = connection.connection()


def continent_name(continent_abbr):
    if continent_abbr == 'AF':
        continent_fi = "Afrikka"
    elif continent_abbr == 'EU':
        continent_fi = "Eurooppa"
    elif continent_abbr == 'NA':
        continent_fi = "Pohjois-Amerikka"
    elif continent_abbr == 'SA':
        continent_fi = "Etelä-Amerikka"
    elif continent_abbr == 'OC':
        continent_fi = "Australia ja Oseania"
    elif continent_abbr == 'AS':
        continent_fi = "Aasia"
    elif continent_abbr == 'AN':
        continent_fi = "Etelämanner"
    return continent_fi


def user_continents(user):
    colorama.init()
    print(user)
    sql = f"SELECT * FROM game WHERE player_id = '{user[0]}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    temp_list = cursor.fetchone()
    # print(temp_list)
    print()
    print("Vihreällä maanosat, joissa olet jo käynyt, punaisella ne, jotka on käymättä:")

    if temp_list[5]:
        print(Fore.GREEN + "AFRIKKA")
    else:
        print(Fore.RED + "AFRIKKA")
    if temp_list[6]:
        print(Fore.GREEN + "ETELÄMANNER")
    else:
        print(Fore.RED + "ETELÄMANNER")
    if temp_list[7]:
        print(Fore.GREEN + "ASIA")
    else:
        print(Fore.RED + "ASIA")
    if temp_list[8]:
        print(Fore.GREEN + "EUROOPPA")
    else:
        print(Fore.RED + "EUROOPPA")
    if temp_list[9]:
        print(Fore.GREEN + "POHJOIS-AMERIKKA")
    else:
        print(Fore.RED + "POHJOIS-AMERIKKA")
    if temp_list[10]:
        print(Fore.GREEN + "AUSTRALIA")
    else:
        print(Fore.RED + "AUSTRALIA")
    if temp_list[11]:
        print(Fore.GREEN + "ETELÄ-AMERIKKA")
    else:
        print(Fore.RED + "ETELÄ-AMERIKKA")

    time.sleep(1)

    print(Style.RESET_ALL)


def choose_plane():

    sql = f"SELECT type, id, emission, risk, questions, velocity FROM plane_info"
    cursor = connection.cursor()
    cursor.execute(sql)
    planes = cursor.fetchall()
    print()
    print("Aloitetaan valitsemalla lentokone.")
    print()
    print("Minkä lentokoneen haluaisit valita?")
    print("Vaihtoehdot:")

    times = 0
    for i in planes:
        plane = planes[times]
        print(f"{plane[1]}: Koneen {plane[0]} päästötaso on {plane[2]}, riskitaso {plane[3]} prosenttia" \
              f" ja nopeus {plane[5]}. Kysymyksiä matkalla on {plane[4]}.")
        times += 1

    chosen = False
    while chosen == False:
        chosen = True

        print()
        plane = 0
        planeNumber = int(input("Valitsemasi lentokoneen numero: "))
        if planeNumber == 1:
            plane = planes[0]
            plane = plane[0]
            print(f"Valitsemasi lentokone on {plane}.")
        elif planeNumber == 2:
            plane = planes[1]
            plane = plane[0]
            print(f"Valitsemasi lentokone on {plane}.")
        elif planeNumber == 3:
            plane = planes[2]
            plane = plane[0]
            print(f"Valitsemasi lentokone on {plane}.")
        elif planeNumber == 4:
            plane = planes[3]
            plane = plane[0]
            print(f"Valitsemasi lentokone on {plane}.")
        else:
            print()
            print("Virheellinen arvo.")
            print("Paina mitä vain, jos haluat lopettaa.")
            again = input("Paina Enter, jos haluat valita uudestaan: ")
            print()
            if again == "":
                chosen = False
            else:
                print("Lopetit pelin.")

        if planeNumber >= 1 and planeNumber <=4 :
            print()
            print("Oletko tyytyväinen valintaasi?")
            confirmation = input("Valitse uudelleen painamalla mitä tahansa, varmista valinta painamalla Enter. ")
            if confirmation == "":
                print("Lentokone valittu!")
                chosen = True
            else:
                chosen = False
                sql = f"SELECT type, id, emission, risk, questions, velocity FROM plane_info"
                cursor = connection.cursor()
                cursor.execute(sql)
                planes = cursor.fetchall()
    return planeNumber


def choose_start():
    sql = f"SELECT ident, name, municipality, iso_country, continent FROM airport " \
          f"WHERE ident = 'DNMM' OR ident = 'ZBAA' OR ident = 'EDDF' " \
          f"OR ident = 'KLAS' OR ident = 'YSSY' OR ident = 'SBJH'"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    airports = cursor.fetchall()
    # print(airports)
    print()
    print("Seuraavaksi saat valita lentokentän, jolta aloitat pelin.")
    print()
    print("Lentokenttävaihtoehdot:")
    print()

    print('%-47s %-27s %-10s %-10s' % ("Lentokentän nimi:", "Kunta:", "Maa:", "Maanosa:"))
    times = 0
    id = 1
    for i in airports:
        airport = airports[times]
        print('%-4d %-45s %-25s %-10s %-10s' % (id, airport[1], airport[2], airport[3], airport[4]))
        times += 1
        id += 1

    chosen = False
    while not chosen:
        chosen = True

        print()
        airport_id = int(input("Valitsemasi lentokentän numero: "))
        airport = 0

        if 1 <= airport_id <= 6:
            index = airport_id - 1
            airport = airports[index][1]
            continent_abbr = airports[index][4]
            continent = continent_name(continent_abbr)
            print(f"Olet lentokentällä {airport} maanosassa {continent}.")
        else:
            print()
            print("Virheellinen arvo.")
            print("Paina mitä vain, jos haluat lopettaa.")
            again = input("Paina Enter, jos haluat valita uudestaan: ")
            print()
            if again == "":
                chosen = False
            else:
                print("Lopetit pelin.")

        if 1 <= airport_id <= 6:
            print()
            print("Oletko tyytyväinen valintaasi?")
            confirmation = input("Valitse uudelleen painamalla mitä tahansa, varmista valinta painamalla Enter. ")
            if confirmation == "":
                print("Lentokenttä valittu!")
                chosen = True
            else:
                chosen = False
                sql = f"SELECT ident, name, municipality, iso_country, continent FROM airport " \
                      f"WHERE ident = 'DNMM' OR ident = 'ZBAA' OR ident = 'EDDF' " \
                      f"OR ident = 'KLAS' OR ident = 'YSSY' OR ident = 'SBJH'"
                cursor = connection.cursor()
                cursor.execute(sql)
                airports = cursor.fetchall()
    return airport, continent_abbr


def choose_continent(from_continent):
    sql = f"SELECT continent FROM airport GROUP BY continent"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    continents = cursor.fetchall()
    # print(continents)

    print()
    print("Mihin haluat lentää?")
    print()
    print("Valitse aluksi maanosa: ")

    times = 0
    id = 1
    for i in continents:
        one = continents[times]
        continent_abbr = one[0]
        continenT = continent_name(continent_abbr)
        print(f"{id}: {continenT}")
        if continent_abbr == from_continent:
            print("Olet nyt täällä!)")
        times += 1
        id += 1

    chosen = False
    while not chosen:
        gameover1 = False
        print()
        continent_nro = int(input("Haluamasi maanosan numero: "))
        to_continent = 0

        if 1 <= continent_nro <= 7:
            index = continent_nro - 1
            continents = continents[index]
            to_continent = continents[0]
            continent = continent_name(to_continent)
            print(f"Valitsemasi maanosa on {continent}.")
        else:
            print()
            print("Virheellinen arvo.")
            print("Paina mitä vain jos haluat lopettaa.")
            again = input("Paina Enter, jos haluat valita uudestaan. ")
            if again == "":
                chosen = False
            else:
                print()
                print("Lopetit pelin.")
                chosen = True
                gameover1 = True

        if 1 <= continent_nro <= 7:
            print()
            print("Oletko tyytyväinen valintaasi?")
            confirmation = input("Valitse uudelleen painamalla mitä tahansa, varmista valinta painamalla Enter. ")
            if confirmation == "":
                print("Maanosa valittu!")
                chosen = True
            else:
                chosen = False
                sql = f"SELECT continent FROM airport GROUP BY continent"
                cursor = connection.cursor()
                cursor.execute(sql)
                continents = cursor.fetchall()
    return to_continent, gameover1


def choose_country(to_continent):
    # print(to_continent)
    print()
    print("Valitse seuraavaksi maa.")
    print()
    print("Valitsemasi maanosan maat:")

    sql = f"SELECT name, iso_country FROM country WHERE continent = '{to_continent}' GROUP BY name"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    countries = cursor.fetchall()
    # print(countries)

    times = 0
    id = 1
    for i in countries:
        one = countries[times]
        country = one[0]
        print(f"{id}: {country}")
        times += 1
        id += 1

    chosen = False
    while chosen == False:
        gameover2 = False
        print()
        list_index = len(countries)
        country_nro = int(input("Haluamasi maan numero: "))
        to_country = 0
        # print(list_index)

        if 1 <= country_nro <= list_index:
            index = country_nro - 1
            countries = countries[index]
            to_country = countries[0]
            iso_country = countries[1]
            print(f"Valitsemasi maa on {to_country}.")
        else:
            print()
            print("Virheellinen arvo.")
            print("Paina mitä vain, jos haluat lopettaa.")
            again = input("Paina Enter, jos haluat valita uudestaan: ")
            print()
            if again == "":
                chosen = False
            else:
                print("Lopetit pelin.")
                chosen = True
                gameover2 = True

        if 1 <= country_nro <= list_index:
            print()
            print("Oletko tyytyväinen valintaasi?")
            confirmation = input("Valitse uudelleen painamalla mitä tahansa, varmista valinta painamalla Enter. ")
            if confirmation == "":
                print("Maa valittu!")
                chosen = True
            else:
                chosen = False
                sql = f"SELECT iso_country FROM airport WHERE continent = '{to_continent}' GROUP BY iso_country"
                cursor = connection.cursor()
                cursor.execute(sql)
                countries = cursor.fetchall()
    return iso_country, gameover2


def choose_airport(to_country):
    print()
    print("Valitse vielä lentokenttä.")
    print()
    print("Lentokentät valitsemassasi kaupungissa:")

    sql = f"SELECT name, ident, municipality FROM airport WHERE iso_country = '{to_country}'"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    airports_list = cursor.fetchall()
    # print(airports_list)
    print()

    print('%-40s %-40s' % ("Lentokentän nimi:", "Sijainti:"))
    times = 0
    id = 1
    for i in airports_list:
        airport_name = airports_list[times][0]
        airport_place = airports_list[times][2]
        print('%-5d %-40s %-40s' % (id, airport_name, airport_place))
        id += 1
        times += 1

    gameover3 = False
    chosen = False
    continue_game = False

    while not chosen:

        print()
        list_index = len(airports_list)
        # print(list_index)
        airport_nro = int(input("Haluamasi lentokentän numero: "))
        airport = 0

        if 1 <= airport_nro <= list_index:
            index = airport_nro - 1
            airports_list = airports_list[index]
            airport = airports_list[0]
            airport_ident = airports_list[1]
            print(f"Valitsemasi lentokenttä on {airport}.")
        else:
            print()
            print("Virheellinen arvo.")
            print("Paina mitä vain, jos haluat lopettaa.")
            again = input("Paina Enter, jos haluat valita uudestaan: ")
            print()
            if again == "":
                chosen = False
            else:
                print("Lopetit pelin.")
                gameover3 = True

        if airport_nro >= 1:
            print()
            print("Oletko tyytyväinen valintaasi?")
            confirmation = input("Valitse uudelleen painamalla mitä tahansa, varmista valinta painamalla Enter.")
            if confirmation == "":
                print("Lentokenttä valittu!")
                chosen = True
                continue_game = True
            else:
                chosen = False
                sql = f"SELECT name, ident, municipality FROM airport WHERE iso_country = '{to_country}'"
                cursor = connection.cursor()
                cursor.execute(sql)
                airports_list = cursor.fetchall()
    return airport, airport_ident, gameover3, continue_game


def travel(start_continent):
    gameover_main = False
    while not gameover_main:

        result = choose_continent(start_continent)
        to_continent = result[0]
        gameover_main = result[1]
        if gameover_main:
            break

        result = choose_country(to_continent)
        to_country = result[0]
        gameover_main = result[1]
        if gameover_main:
            break

        result = choose_airport(to_country)
        to_airport = result[0]
        airport_ident = result[1]
        gameover_main = result[2]
        continue_game1 = result[3]
        if gameover_main:
            break

        if continue_game1:
            break

    return to_airport, airport_ident, to_continent, gameover_main
