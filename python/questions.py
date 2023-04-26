import misc
import time
import random

connection = misc.connection()

def QuestionA(tehtävänanto, vaihtoehto1, vaihtoehto2,vaihtoehto3, aika):
    print()
    print("Painamalla Enter kesken vastaamisen näät kuluneen ajan.")
    start = input("Sinulla on 20 sekuntia aikaa, paina Enter aloittaaksesi: ")
    start_time = time.time()
    points = 4

    # vaihtoehdot tulostuu, jos vastauskenttä on tyhjä
    if start == "":
        print()
        print(tehtävänanto)
        print()
        print(f"Vaihtoehto A: {vaihtoehto1}")
        print(f"Vaihtoehto B: {vaihtoehto2}")
        print(f"Vaihtoehto C: {vaihtoehto3}")

    # tehtävä jatkuu, kun vastauskenttä on tyhjä
    aloitus = True
    while start == "":
        print()
        answer = input("Vastauksesi: ")

        # käyttäjä voi vastata ison tai pienen kirjaimen
        # väärästä vastauksesta lähtee 2 pistettä
        # oikea vastaus tulostaa lopullisen vastausajan ja lopettaa while-loopin

        if answer == "A" or answer == "a":
            print("Oikein!")
            end_time = time.time()
            endtime = end_time - start_time
            print(f"Aikasi oli {round(endtime)} sekuntia.")
            start = "stop"
        elif answer == "B" or answer == "b":
            print("Väärin :( yritä uudestaan.")
            points -= 2
        elif answer == "C" or answer == "c":
            print("Väärin :( yritä uudestaan.")
            points -= 2
        elif answer == "":
            print("")

        # jos käyttäjä ei vastaa mitään vaihtoehdoista, pisteet ei vähene
        else:
            print("Invalid syntax, yritä uudestaan.")

        # jos pisteet menee nolliin, vastausyritykset loppuu
        if points == 0:
            endtime = 20
            print("Yrityksesi loppuivat.")
            aloitus = False

        # tehtävä loppuu ja pisteet nollautuu, jos vastaamisessa menee yli 20 sekuntia
        now = time.time()
        timer = now - start_time
        if timer >= aika:
            print("Aika loppui :(")
            aloitus = False

        # kulunut aika tulostuu, jos käyttäjä ei ole vielä antanut oikeaa vastausta
        if answer != "A" and answer != "a":
            print(f"Aikaa kulunut {round(timer)} sekuntia.")

    if aloitus == False:
        points = 0
        endtime = 20

    print()
    print(f"Sait {points} pistettä ja aikaa kului {round(endtime)} tuntia.")
    return points, round(endtime)


def QuestionB(tehtävänanto, vaihtoehto1, vaihtoehto2,vaihtoehto3, aika):
    print()
    print("Painamalla Enter kesken vastaamisen näät kuluneen ajan.")
    start = input("Sinulla on 20 sekuntia aikaa, paina Enter aloittaaksesi: ")
    start_time = time.time()
    points = 4

    # vaihtoehdot tulostuu, jos vastauskenttä on tyhjä
    if start == "":
        print()
        print(tehtävänanto)
        print()
        print(f"Vaihtoehto A: {vaihtoehto1}")
        print(f"Vaihtoehto B: {vaihtoehto2}")
        print(f"Vaihtoehto C: {vaihtoehto3}")

    # tehtävä jatkuu, kun vastauskenttä on tyhjä
    while start == "":
        print()
        answer = input("Vastauksesi: ")

        # käyttäjä voi vastata ison tai pienen kirjaimen
        # väärästä vastauksesta lähtee 2 pistettä
        # oikea vastaus tulostaa lopullisen vastausajan ja lopettaa while-loopin

        if answer == "A" or answer == "a":
            print("Väärin :( yritä uudestaan.")
            points -= 2
        elif answer == "B" or answer == "b":
            print("Oikein!")
            end_time = time.time()
            endtime = (end_time - start_time)
            print(f"Aikasi oli {round(endtime)} sekuntia.")
            start = "stop"
        elif answer == "C" or answer == "c":
            print("Väärin :( yritä uudestaan.")
            points -= 2

        elif answer == "":
            print("")
        # jos käyttäjä ei vastaa mitään vaihtoehdoista, pisteet ei vähene
        else:
            print("Invalid syntax, yritä uudestaan.")

        # jos pisteet menee nolliin, vastausyritykset loppuu
        if points == 0:
            endtime = 20
            print("Yrityksesi loppuivat.")
            break

        # tehtävä loppuu ja pisteet nollautuu, jos vastaamisessa menee yli 20 sekuntia
        now = time.time()
        timer = now - start_time
        if timer >= aika:
            print("Aika loppui :(")
            points = 0
            endtime = 20
            break

        # kulunut aika tulostuu, jos käyttäjä ei ole vielä antanut oikeaa vastausta
        if answer != "B" and answer != "b":
            print(f"Aikaa kulunut {round(timer)} sekuntia.")

    if start != "" and start != "stop":
        points = 0
        endtime = 20

    print()
    print(f"Sait {points} pistettä ja aikaa kului {round(endtime)} tuntia.")
    return points, round(endtime)


def QuestionC(tehtävänanto, vaihtoehto1, vaihtoehto2,vaihtoehto3, aika):
    print()
    print("Painamalla Enter kesken vastaamisen näät kuluneen ajan.")
    start = input("Sinulla on 20 sekuntia aikaa, paina Enter aloittaaksesi: ")
    start_time = time.time()
    points = 4

    # vaihtoehdot tulostuu, jos vastauskenttä on tyhjä
    if start == "":
        print()
        print(tehtävänanto)
        print()
        print(f"Vaihtoehto A: {vaihtoehto1}")
        print(f"Vaihtoehto B: {vaihtoehto2}")
        print(f"Vaihtoehto C: {vaihtoehto3}")

    # tehtävä jatkuu, kun vastauskenttä on tyhjä
    while start == "":
        print()
        answer = input("Vastauksesi: ")

        # käyttäjä voi vastata ison tai pienen kirjaimen
        # väärästä vastauksesta lähtee 2 pistettä
        # oikea vastaus tulostaa lopullisen vastausajan ja lopettaa while-loopin

        if answer == "A" or answer == "a":
            print("Väärin :( yritä uudestaan.")
            points -= 2
        elif answer == "B" or answer == "b":
            print("Väärin :( yritä uudestaan.")
            points -= 2
        elif answer == "C" or answer == "c":
            print("Oikein!")
            end_time = time.time()
            endtime = end_time - start_time
            print(f"Aikasi oli {round(endtime)} sekuntia.")
            start = "stop"

        elif answer == "":
            print("")
        # jos käyttäjä ei vastaa mitään vaihtoehdoista, pisteet ei vähene
        else:
            print("Invalid syntax, yritä uudestaan.")

        # jos pisteet menee nolliin, vastausyritykset loppuu
        if points == 0:
            endtime = 20
            print("Yrityksesi loppuivat.")
            break

        # tehtävä loppuu ja pisteet nollautuu, jos vastaamisessa menee yli 20 sekuntia
        now = time.time()
        timer = now - start_time
        if timer >= aika:
            print("Aika loppui :(")
            points = 0
            endtime = 20
            break

        # kulunut aika tulostuu, jos käyttäjä ei ole vielä antanut oikeaa vastausta
        if answer != "C" and answer != "c":
            print(f"Aikaa kulunut {round(timer)} sekuntia.")

    if start != "" and start != "stop":
        points = 0
        endtime = 20

    print()
    print(f"Sait {points} pistettä ja aikaa kului {round(endtime)} tuntia.")
    return points, round(endtime)


def pistelaskuri(kokonaispisteet_lista):
    # varmistusprinttaus
    # print(f"Kokonaispistelista funktiossa {kokonaispisteet_lista}")
    print()

    # funktion oma muuttuja ('yhteispisteet')
    yhteispisteet = kokonaispisteet_summa

    # lisätään saadut pisteet kokonaispistemäärään
    for a in kokonaispisteet_lista:
        yhteispisteet += a[0]
    print(f"Sinulla on tällä hetkellä {yhteispisteet} pistettä.")

    # funktion sisäinen muuttuja 'yhteisaika'
    yhteisaika = aikaakulunut

    # lisätään kulunut aika kokonaismäärään
    for a in kokonaispisteet_lista:
        yhteisaika += a[1]
    print(f"Aikaa lennolla kului {yhteisaika} tuntia.")
    return yhteispisteet, yhteisaika



def travel_questionsAF(planeNumber):
    sql = f"SELECT type, risk, questions FROM plane_info WHERE id = {planeNumber}"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    planelist_list = cursor.fetchall()
    planelist = planelist_list[0]
    # print(planelist)

    print()
    print(f"Valitsemallasi lentokoneella '{planelist[0]}' riskitaso on {planelist[1]} prosenttia ja kysymyksiä on {planelist[2]}.")

    rip = False
    kokonaispisteet_lista = []
    if planeNumber == 1 or planeNumber == 2:
        result1 = QuestionA("Montaako kieltä Afrikassa puhutaan?", "Yli 2000", "Noin 1300", "830", 20)
        kokonaispisteet_lista.append(result1)
        result2 = QuestionC("Missä Afrikan maassa on eniten pyramideja?", "Egyptissä", "Libyassa", "Sudanissa", 20)
        kokonaispisteet_lista.append(result2)
        result3 = QuestionB("Milloin Etiopiassa juhlitaan uutta vuotta?", "1.1.", "11.9.", "24.5.", 20)
        kokonaispisteet_lista.append(result3)
        result4 = QuestionA("Mikä on Afrikan pinta-ala?", "30 365 000 neliökilometriä", "21 222 421 neliökilometriä", "18 032 341 neliökilometriä", 20)
        kokonaispisteet_lista.append(result4)
        rip = incident_risk1(1)
    elif planeNumber == 3:
        result1 = QuestionC("Missä Afrikan maassa on eniten pyramideja?", "Egyptissä", "Libyassa", "Sudanissa", 20)
        kokonaispisteet_lista.append(result1)
        result2 = QuestionA("Montaako kieltä Afrikassa puhutaan?", "Yli 2000", "Noin 1300", "830", 20)
        kokonaispisteet_lista.append(result2)
        rip = incident_risk1(2)
    elif planeNumber == 4:
        result1 = QuestionB("Milloin Etiopiassa juhlitaan uutta vuotta?", "1.1.", "11.9.", "24.5.", 20)
        kokonaispisteet_lista.append(result1)
        rip = incident_risk1(3)
    return kokonaispisteet_lista, rip


def travel_questionsAN(planeNumber):
    sql = f"SELECT type, risk, questions FROM plane_info WHERE id = {planeNumber}"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    planelist_list = cursor.fetchall()
    planelist = planelist_list[0]
    # print(planelist)

    print()
    print(f"Valitsemallasi lentokoneella '{planelist[0]}' riskitaso on {planelist[1]} prosenttia ja kysymyksiä on {planelist[2]}.")

    play_points = 0
    kokonaispisteet_lista = []
    if planeNumber == 1 or planeNumber == 2:
        result1 = QuestionB("Paljonko on Etelämantereen mannerjään keskimääräinen paksuus?", "1,4km", "2,5km", "4,1km", 20)
        kokonaispisteet_lista.append(result1)
        result2 = QuestionC("Kuinka nopeita Etelämantereen tuulet voivat olla pahimmillaan?", "35m/s", "235km/h", "320km/h", 20)
        kokonaispisteet_lista.append(result2)
        result3 = QuestionA("Montako millimetriä Etelämantereella sataa vuosittain?", "50mm", "89mm", "150mm", 20)
        kokonaispisteet_lista.append(result3)
        result4 = QuestionC("Kuinka monta prosenttia maapallon jäästä sijaitsee Etelämantereella?", "69 prosenttia", "79 prosenttia", "90 prosenttia", 20)
        kokonaispisteet_lista.append(result4)
        play_points = incident_risk2(1)
    elif planeNumber == 3:
        result1 = QuestionA("Montako millimetriä Etelämantereella sataa vuosittain?", "50mm", "89mm", "150mm", 20)
        kokonaispisteet_lista.append(result1)
        result2 = QuestionC("Kuinka monta prosenttia maapallon jäästä sijaitsee Etelämantereella?", "69 prosenttia", "79 prosenttia", "90 prosenttia", 20)
        kokonaispisteet_lista.append(result2)
        play_points = incident_risk2(2)
    elif planeNumber == 4:
        result1 = QuestionB("Paljonko on Etelämantereen mannerjään keskimääräinen paksuus?", "1,4km", "2,5km", "4,1km", 20)
        kokonaispisteet_lista.append(result1)
        play_points = incident_risk2(3)
    return kokonaispisteet_lista, play_points


def travel_questionsAS(planeNumber):
    sql = f"SELECT type, risk, questions FROM plane_info WHERE id = {planeNumber}"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    planelist_list = cursor.fetchall()
    planelist = planelist_list[0]
    # print(planelist)

    print()
    print(f"Valitsemallasi lentokoneella '{planelist[0]}' riskitaso on {planelist[1]} prosenttia ja kysymyksiä on {planelist[2]}.")

    kokonaispisteet_lista = []
    play_points = 0
    if planeNumber == 1 or planeNumber == 2:
        result1 = QuestionC("Missä maassa sijaitsee maailman korkein vapaasti seisova lipputanko (165m)?", "Kiinassa", "Bhutanissa", "Tadzikistanissa", 20)
        kokonaispisteet_lista.append(result1)
        result2 = QuestionC("Montako maatilaa on Singaporessa?", "9", "37", "0", 20)
        kokonaispisteet_lista.append(result2)
        result3 = QuestionA("Malediivit sijaitsee Intian valtamerellä ja on maailman matalin valtio. "
                            "Paljonko sen korkeus on keskimäärin merenpinnasta?", "2,1m", "3,2m", "5,5m", 20)
        kokonaispisteet_lista.append(result3)
        result4 = QuestionB("Montako jokea virtaa Saudi-Arabiassa?", "1", "0", "3", 20)
        kokonaispisteet_lista.append(result4)
        play_points = incident_risk3(1)
    elif planeNumber == 3:
        result1 = QuestionC("Missä maassa sijaitsee maailman korkein vapaasti seisova lipputanko (165m)?", "Kiinassa", "Bhutanissa", "Tadzikistanissa", 20)
        kokonaispisteet_lista.append(result1)
        result2 = QuestionB("Montako jokea virtaa Saudi-Arabiassa?", "1", "0", "3", 20)
        kokonaispisteet_lista.append(result2)
        play_points = incident_risk3(2)
    elif planeNumber == 4:
        result1 = QuestionC("Montako maatilaa on Singaporessa?", "9", "37", "0", 20)
        kokonaispisteet_lista.append(result1)
        play_points = incident_risk3(3)
    return kokonaispisteet_lista, play_points


def travel_questionsEU(planeNumber):
    sql = f"SELECT type, risk, questions FROM plane_info WHERE id = {planeNumber}"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    planelist_list = cursor.fetchall()
    planelist = planelist_list[0]
    # print(planelist)

    print()
    print(f"Valitsemallasi lentokoneella '{planelist[0]}' riskitaso on {planelist[1]} prosenttia ja kysymyksiä on {planelist[2]}.")

    play_points = 0
    kokonaispisteet_lista = []
    if planeNumber == 1 or planeNumber == 2:
        result1 = QuestionC("Monelleko aikavyöhykkeelle Ranska ulottuu, kun otetaan huomioon sen territoriot ja alusmaat?", "5", "9", "12", 20)
        kokonaispisteet_lista.append(result1)
        result2 = QuestionA("Missä maassa sijaitsee Longyearbyen kaupunki, jossa 'kuoleminen on kiellettyä', "
                            "koska kylmyyden vuoksi ruumiit eivät maadu?", "Norjassa", "Ruotsissa", "Islannissa", 20)
        kokonaispisteet_lista.append(result2)
        result3 = QuestionA("Missä maassa sijaitsee mikrovaltio Ladonia?", "Ruotsissa", "Italiassa", "Kreikassa", 20)
        kokonaispisteet_lista.append(result3)
        result4 = QuestionB("Kuinka suuri osa Kosovon asukkaista on alle 25-vuotiaita?", "Neljännes", "Puolet", "Noin 10%", 20)
        kokonaispisteet_lista.append(result4)
        play_points = incident_risk4(1)
    elif planeNumber == 3:
        result1 = QuestionB("Kuinka suuri osa Kosovon asukkaista on alle 25-vuotiaita?", "Neljännes", "Puolet", "Noin 10%", 20)
        kokonaispisteet_lista.append(result1)
        result2 = QuestionB("Missä maassa sijaitsee Longyearbyen kaupunki, jossa 'kuoleminen on kiellettyä', "
                            "koska kylmyyden vuoksi ruumiit eivät maadu?", "Ruotsissa", "Norjassa", "Islannissa", 20)
        kokonaispisteet_lista.append(result2)
        play_points = incident_risk4(2)
    elif planeNumber == 4:
        result1 = QuestionA("Missä maassa sijaitsee Longyearbyen kaupunki, jossa 'kuoleminen on kiellettyä', "
                            "koska kylmyyden vuoksi ruumiit eivät maadu?", "Norjassa", "Ruotsissa", "Islannissa", 20)
        kokonaispisteet_lista.append(result1)
        play_points = incident_risk4(3)
    return kokonaispisteet_lista, play_points


def travel_questionsNA(planeNumber):
    sql = f"SELECT type, risk, questions FROM plane_info WHERE id = {planeNumber}"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    planelist_list = cursor.fetchall()
    planelist = planelist_list[0]
    # print(planelist)

    print()
    print(f"Valitsemallasi lentokoneella '{planelist[0]}' riskitaso on {planelist[1]} prosenttia ja kysymyksiä on {planelist[2]}.")

    play_points = 0
    kokonaispisteet_lista = []
    if planeNumber == 1 or planeNumber == 2:
        result1 = QuestionB("Mitä Guamin saarelta ei löydy lainkaan?", "Asfalttia", "Hiekkaa", "Soraa", 20)
        kokonaispisteet_lista.append(result1)
        result2 = QuestionC("Kuinka pitkä on Kanadan rantaviiva?", "130 421 kilometriä", "190 134 kilometriä", "202 080 kilometriä", 20)
        kokonaispisteet_lista.append(result2)
        result3 = QuestionB("Montako kansallispuistoa Yhdysvalloissa on?", "32", "58", "101", 20)
        kokonaispisteet_lista.append(result3)
        result4 = QuestionA("Montako ihmistä Meksikossa on kadonnut viimeisen vuosikymmenen aikana?", "Yli 27 000", "Noin 9000", "Noin 15 000", 20)
        kokonaispisteet_lista.append(result4)
        play_points = incident_risk5(1)
    elif planeNumber == 3:
        result1 = QuestionA("Montako ihmistä Meksikossa on kadonnut viimeisen vuosikymmenen aikana?", "Yli 27 000", "Noin 9000", "Noin 15 000", 20)
        kokonaispisteet_lista.append(result1)
        result2 = QuestionC("Kuinka pitkä on Kanadan rantaviiva?", "130 421 kilometriä", "190 134 kilometriä", "202 080 kilometriä", 20)
        kokonaispisteet_lista.append(result2)
        play_points = incident_risk5(2)
    elif planeNumber == 4:
        result1 = QuestionB("Mitä Guamin saarelta ei löydy lainkaan?", "Asfalttia", "Soraa", "Hiekkaa", 20)
        kokonaispisteet_lista.append(result1)
        play_points = incident_risk5(3)
    return kokonaispisteet_lista, play_points


def travel_questionsOC(planeNumber):
    sql = f"SELECT type, risk, questions FROM plane_info WHERE id = {planeNumber}"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    planelist_list = cursor.fetchall()
    planelist = planelist_list[0]
    # print(planelist)

    print()
    print(f"Valitsemallasi lentokoneella '{planelist[0]}' riskitaso on {planelist[1]} prosenttia ja kysymyksiä on {planelist[2]}.")

    play_points = 0
    kokonaispisteet_lista = []
    if planeNumber == 1 or planeNumber == 2:
        result1 = QuestionA("Minkä valtion virallisia kolikoita koristavat Pokemon-, Disney- ja Star Wars -hahmot?", "Niue", "Australia", "Uusi-Seelanti", 20)
        kokonaispisteet_lista.append(result1)
        result2 = QuestionB("Montako maata Oseaniaan kuuluu?", "12", "23", "18", 20)
        kokonaispisteet_lista.append(result2)
        result3 = QuestionB("Montako kengurulajia Australiassa on?", "27", "Yli 50", "Yli 90", 20)
        kokonaispisteet_lista.append(result3)
        result4 = QuestionC("Paljonko painoindeksi on Naurussa asukasta kohden?", "20-21", "26-28", "34-35", 20)
        kokonaispisteet_lista.append(result4)
        play_points = incident_risk6(1)
    elif planeNumber == 3:
        result1 = QuestionB("Montako maata Oseaniaan kuuluu?", "12", "23", "18", 20)
        kokonaispisteet_lista.append(result1)
        result2 = QuestionC("Minkä valtion virallisia kolikoita koristavat Pokemon-, Disney- ja Star Wars -hahmot?", "Uusi-Seelanti", "Australia", "Niue", 20)
        kokonaispisteet_lista.append(result2)
        play_points = incident_risk6(2)
    elif planeNumber == 4:
        result1 = QuestionA("Minkä valtion virallisia kolikoita koristavat Pokemon-, Disney- ja Star Wars -hahmot?", "Niue", "Australia", "Uusi-Seelanti", 20)
        kokonaispisteet_lista.append(result1)
        play_points = incident_risk6(3)
    return kokonaispisteet_lista, play_points


def travel_questionsSA(planeNumber):
    sql = f"SELECT type, risk, questions FROM plane_info WHERE id = {planeNumber}"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    planelist_list = cursor.fetchall()
    planelist = planelist_list[0]
    # print(planelist)

    print()
    print(f"Valitsemallasi lentokoneella '{planelist[0]}' riskitaso on {planelist[1]} prosenttia ja kysymyksiä on {planelist[2]}.")
    # input("Paina Enter jatkaaksesi. ")

    play_points = 0
    kokonaispisteet_lista = []
    if planeNumber == 1 or planeNumber == 2:
        result1 = QuestionA("Montako prosenttia Surinamen pinta-alasta on metsää?", "94,6 prosenttia", "73,1 prosenttia", "53,4 prosenttia", 20)
        kokonaispisteet_lista.append(result1)
        result2 = QuestionC("Venezuelassa sijaitsee Heladeria Coromoto -jäätelöbaari, jossa on maailman "
                            "laajin makuvalikoima. Montako eri jäätelömakua siellä on saatavilla?", "91", "157", "860", 20)
        kokonaispisteet_lista.append(result2)
        result3 = QuestionB("Montako miljoonakaupunkia Brasiliassa on?", "7", "13", "21", 20)
        kokonaispisteet_lista.append(result3)
        result4 = QuestionA("Montako valtiota Etelä-Amerikassa on?", "12", "17", "9", 20)
        kokonaispisteet_lista.append(result4)
        play_points = incident_risk7(1)
    elif planeNumber == 3:
        result1 = QuestionC("Venezuelassa sijaitsee Heladeria Coromoto -jäätelöbaari, jossa on maailman "
                            "laajin makuvalikoima. Montako eri jäätelömakua siellä on saatavilla?", "91", "157", "860", 20)
        kokonaispisteet_lista.append(result1)
        result2 = QuestionA("Montako valtiota Etelä-Amerikassa on?", "12", "17", "9", 20)
        kokonaispisteet_lista.append(result2)
        play_points = incident_risk7(2)
    elif planeNumber == 4:
        result1 = QuestionB("Montako miljoonakaupunkia Brasiliassa on?", "7", "13", "21", 20)
        kokonaispisteet_lista.append(result1)
        play_points = incident_risk7(3)
    return kokonaispisteet_lista, play_points


def which_question(continent_abb, planeNumber):
    kokonaispisteet_funktiossa = 0
    if continent_abb == "AF":
        result = travel_questionsAF(planeNumber)
        kokonaispisteet_lista = result[0]
        points = result[1]
        kokonaispisteet_funktiossa += points
        return kokonaispisteet_lista, points
    elif continent_abb == "AN":
        result = travel_questionsAN(planeNumber)
        kokonaispisteet_lista = result[0]
        points = result[1]
        kokonaispisteet_funktiossa += points
        return kokonaispisteet_lista, kokonaispisteet_funktiossa
    elif continent_abb == "AS":
        result = travel_questionsAS(planeNumber)
        kokonaispisteet_lista = result[0]
        points = result[1]
        kokonaispisteet_funktiossa += points
        return kokonaispisteet_lista, kokonaispisteet_funktiossa
    elif continent_abb == "EU":
        result = travel_questionsEU(planeNumber)
        kokonaispisteet_lista = result[0]
        points = result[1]
        kokonaispisteet_funktiossa += points
        return kokonaispisteet_lista, kokonaispisteet_funktiossa
    elif continent_abb == "NA":
        result = travel_questionsNA(planeNumber)
        kokonaispisteet_lista = result[0]
        points = result[1]
        kokonaispisteet_funktiossa += points
        return kokonaispisteet_lista, kokonaispisteet_funktiossa
    elif continent_abb == "OC":
        result = travel_questionsOC(planeNumber)
        kokonaispisteet_lista = result[0]
        points = result[1]
        kokonaispisteet_funktiossa += points
        return kokonaispisteet_lista, kokonaispisteet_funktiossa
    elif continent_abb == "SA":
        result = travel_questionsSA(planeNumber)
        kokonaispisteet_lista = result[0]
        points = result[1]
        kokonaispisteet_funktiossa += points
        return kokonaispisteet_lista, kokonaispisteet_funktiossa


def incident_risk1(luku):
    incident = random.randint(1,5)
    points = 0
    if incident <= luku:
        kolikko = random.choice(["Kruuna", "Klaava"])
        print("Lentokoneesi on syöksylaskussa!")
        print(f'Teitä on enää kaksi lentokoneessa, mutta tarjolla on vain yksi laskuvarjo.')
        print(f'Päätätte selvittää kolikonheitolla, kumpi teistä saa laskuvarjon.')
        print(f'Jos kolikko laskeutuu {kolikko} puoli ylöspäin, sinä saat sen.')
        print()
        input("Paina 'Enter' jatkaaksesi")

        kolikonheitto_satunnainen = "Kruuna" if random.randint(0, 1) > 0.5 else "Klaava"

        for aika in range(3, 0, -1):
            print(aika)
            time.sleep(1)

        print(kolikonheitto_satunnainen)

        if kolikko == kolikonheitto_satunnainen:
            print("Selvisit! Laskeudut turvallisesti seuraavalle lentokentälle.")
        else:
            print()
            print("Hävisit! Olet nyt yksin syöksyävässä koneessa... vaihtoehdot ovat vähissä.")
            print("Päätät hypätä vapaapudotukseen ja toivoa parasta.")
            print("Muistikuvat hämärtyvät...")
            input("Paina 'Enter' jatkaaksesi")
            print()
            print("Joku ravistelee sinut hereille... merirosvoja!! X_X")
            print()
            print("Olet selvästikin selvinnyt pudotuksesta ja ajelehtinut autiolle saarelle.")
            print("Piraatit tarjoavat sinulle kyydin sivistyksen pariin kolmella pisteellä.")
            print("Päätät tarttua tarjoukseen, muuta vaihtoehtoa ei ole.")
            points -= 3
    else:
        print("Saavuit kohteeseen turvallisesti!")

    return points


def incident_risk2(luku):
    incident = random.randint(1,5)
    points = 0

    if incident <= luku:
        print("Löysit lottolipun maasta!")
        print("Syötä lappuun kaksi arpanumeroa yksi kerrallaan ja käy lunastamassa se läheiseltä kioskilta.")
        print()
        voittonumerot = random.sample(range(1, 11), 2)
        pelaaja_numerot = []
        for i in range(2):
            while True:
                try:
                    numero = int(input("Syötä numero väliltä 1-10: "))
                    if numero < 1 or numero > 10:
                        raise ValueError
                    break
                except ValueError:
                    print("Virhe. Syötä numero väliltä 1-10: ")
            pelaaja_numerot.append(numero)

        if pelaaja_numerot == voittonumerot:
            print("Onnittelut! Voitit 10 pistettä!")
            points = 10
        else:
            print(f'Valitettavasti arpaonni ei suosinut tällä kertaa, voittonumerot olisi olleet: {voittonumerot}')
    else:
        print("Saavuit kohteeseen turvallisesti!")

    return points


def incident_risk3(luku):
    incident = random.randint(1,5)
    points = 0
    if incident <= luku:
        vastaus_a = "Jatka kohti vessaa"
        vastaus_b = "Pahoittele ja anna 2 pistettä"

        print("Lähdet lentokoneessa vessaan, murra matkallasi tönäiset vahingossa ärtyisän oloista mieshenkilöä.")
        print("Mies kääntää päänsä ja vaikuttaa nyt hyvin vihaiselta.")
        print()
        print("Mitä teet?")
        print(f'A: {vastaus_a}')
        print(f'B: {vastaus_b}')

        vaihtoehdot = ["a", "b"]
        toiminta = True

        while toiminta:
            print()
            pelaaja = input("Vastauksesi: ").lower()
            print()

            if pelaaja not in vaihtoehdot:
                print("Virhe. Yritä uudelleen.")
                print()

            else:
                if pelaaja == "a":
                    print("Mieshenkilö ei vaikutakaan enää kovin vihaiselta ja haluaa tarjota sinulle huikan. Mitä teet?")
                    print()
                    print("A: Jatka matkaasi vessaan")
                    print("B: Ota huikka miehen vihreästä pullosta")
                    vaihtoehdot = ["a", "b"]
                    print()
                    valinta = input("Vastauksesi: ").lower()
                    if valinta == "a":
                        print("'Wrong answer pal...'")
                        print()
                        print("Heräät lentokoneen ensiapuvuoteelta, hoitokulusi ovat 4 pistettä.")
                        points -= 4
                    toiminta = False

                    if valinta == "b":
                        print("          Otat huikan...")
                        print("...askel vaikuttaa heti keveämmältä...")
                        print()
                        print("Voit jatkaa matkaasi.")
                    toiminta = False

                elif pelaaja == "b":
                    print("'You got lucky this time, pal...'")
                    print()
                    print("Selvisit säikähdyksellä, onneksi ei käynyt pahemmin...")
                toiminta = False
    else:
        print("Saavuit kohteeseen turvallisesti!")
    return points


def incident_risk4(luku):
    incident = random.randint(1,5)
    points = 0
    if incident <= luku:
        print("Törmäät lentokentän käytävällä kodittomaan henkilöön.")
        print("Hän anelee sinulta yhtä pistettä.")
        print()
        valinta = input("Annatko pisteen? (kyllä/ei) ")

        if valinta.lower() == "kyllä" or "k":
            print("Annoit pisteen.")
            points -= 1
        if valinta.lower() == "ei" or "e":
            print("Koditon: :-(")
    else:
        print("Saavuit kohteeseen turvallisesti!")

    return points


def incident_risk5(luku):
    incident = random.randint(1,5)
    points = 0

    if incident <= luku:
        print("Otat osaa kilpailuun.")
        print("Tehtävänäsi on painaa 'Enter'-näppäintä sata (100) kertaa 15 sekunnin aikana!")
        print()
        print(input("Paina Enter aloittaaksesi:"))

        pisteet = 0
        start_time = time.time()

        while True:
            input(f'Paina Enter {pisteet}/100')
            pisteet += 1
            time_elapsed = time.time() - start_time
            if time_elapsed >= 15:
                break
            if pisteet == 100:
                break

        print("Aika loppui!")

        if pisteet >= 100:
            print(f'Onnea, voitit 5 pistettä! Aikaa kului {round(time_elapsed, 2)} sekuntia.')
            points = 5
        else:
            print(f'Hävisit:(. Kokonaistuloksesi oli {pisteet}/100.')
    else:
        print("Saavuit kohteeseen turvallisesti!")

    return points


def incident_risk6(luku):
    incident = random.randint(1,5)
    points = 0
    if incident <= luku:
        vastaus_a = "Osta oma lippu (-2 pistettä)"
        vastaus_b = "Yritä anastaa lippu"

        print("On aika hankkia lentoliput seuraavaan kohteeseen.")
        print("Olet matkalla kohti lippupistettä, kun huomaat penkillä nukkuvan vanhuksen, jonka taskusta pilkistää lentolippu.")
        print()
        print("Voit yrittää anastaa lipun häneltä tai hakea oman viidellä pisteellä.")
        print()
        print("Miten toimit?")
        print(f'A: {vastaus_a}')
        print(f'B: {vastaus_b}')

        vaihtoehdot = ["a", "b"]
        toiminta = True

        while toiminta:
            print()
            pelaaja = input("Vastauksesi: ").lower()
            print()

            if pelaaja not in vaihtoehdot:
                print("Virhe. Yritä uudelleen.")
                print()

            else:
                if pelaaja == "b":
                    print("Kurotat kätesi taskulle...")
                    print("Haluatko varmasti jatkaa?")
                    print()
                    print("A: Anasta lippu")
                    print("B: Käänny ja osta oma lippusi (-2 pistettä)")
                    vaihtoehdot = ["a", "b"]
                    print()
                    valinta = input("Vastauksesi: ").lower()
                    if valinta == "b":
                        print("Ostit oman lipun ':D'")
                        points = -2
                    toiminta = False

                    if valinta == "a":
                        print("Sait lipun... Pakenet...")
                        print()
                        print("Matkallasi kohti lähtöselvitystä vartija pysäyttää sinut.")
                        print("Turvakameratalleenteesta on selvinnyt, että varastit lipun.")
                        print()
                        print("Rangaistukseksi saat 4 pisteen sakon.")
                        points -= 4

                    toiminta = False

                elif pelaaja == "a":
                    print("Ostit oman lipun ':D'")
                    points = -2
                toiminta = False
    else:
        print("Saavuit kohteeseen turvallisesti!")

    return points


def incident_risk7(luku):
    incident = random.randint(1,5)
    points = 0
    if incident <= luku:
        print("Sinut haastetaan 'kivi, paperi, sakset' -peliin.")
        print("Voit joko voittaa tai hävitä yhden pisteen.")
        print()
        print("Syötä valintasi, kun olet valmis aloittamaan.")

        vaihtoehdot = ("kivi", "paperi", "sakset", "liimapuikko")
        toiminta = True

        while toiminta:

            pelaaja = None
            tietokone = random.choice(vaihtoehdot)

            while pelaaja not in vaihtoehdot:
                pelaaja = input("Syötä valinta (kivi, paperi, sakset): ")
                print()

            if pelaaja not in vaihtoehdot:
                print("Virhe. Yritä uudelleen.")
                print()

            print(f'Sinä: {pelaaja}')
            print(f'Vastustaja: {tietokone}')

            if pelaaja == tietokone:
                print("Tasapeli! Uusintakierros.")
                print()

            elif pelaaja == "kivi" and tietokone == "sakset":
                print("Sinä voitit! (+1 piste)")
                points = 1

            elif pelaaja == "paperi" and tietokone == "kivi":
                print("Sinä voitit! (+1 piste)")
                points = 1

            elif pelaaja == "sakset" and tietokone == "paperi":
                print("Sinä voitit! (+1 piste)")
                points = 1

            if pelaaja == "liimapuikko":
                print("Saat viisi pistettä luovuudesta :D")
                points = 5

            else:
                print("Sinä hävisit. (-1 piste)")
                points -= 1
            toiminta = False
    else:
        print("Saavuit kohteeseen turvallisesti!")

    return points