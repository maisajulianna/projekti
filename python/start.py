import pygame
import time
import sys
import connection

connection = connection.connection()


def start_print():
    print(
        "Tervetuloa maailmanympärysmatkalle! Tehtävänäsi on käydä jokaisessa maanosassa. "
        "Pääset eteenpäin vastaamalla kysymyksiin.")
    input("Oletko valmis? ")


def start_game():
    username = input("Anna haluamasi käyttäjänimi: ")
    print()
    print(f"Hei, {username}!")

    sql = f"SELECT * FROM game WHERE screen_name = '{username}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    user = cursor.fetchall()

    game_starts = False
    while not game_starts:
        if not user:
            cursor = connection.cursor()
            print("Sinulla ei ole keskeneräistä peliä, uusi alkaa hetken kuluttua...")
            sql = f"INSERT INTO game VALUES (NULL, 0, '{username}', 0, NULL, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE)"
            cursor.execute(sql)
            sql = f"SELECT * FROM game WHERE screen_name = '{username}'"
            cursor.execute(sql)
            user = cursor.fetchone()
            game_starts = True

        else:
            print("Sinulla on tallennettuna keskeneräinen peli. Haluatko...")
            print("A: jatkaa vanhaa peliä")
            print("B: aloittaa uuden pelin (poistaa vanhat tiedot)")
            print("C: aloittaa uuden pelin eri käyttäjänimellä")
            print()
            answer = input("Vastauksesi: ").lower()

            if answer == "a":
                print("Aloitetaan peli!")
                game_starts = True

            elif answer == "b":
                sql = "UPDATE game SET AF_ = FALSE, AN_ = FALSE, AS_ = FALSE, " \
                      "EU_= FALSE, NA_ = FALSE, OC_= FALSE, SA_ = FALSE, time_sec = 0, " \
                      f"score = 0, last_location = NULL WHERE player_id = '{username}'"
                # cursor = connection.cursor()
                cursor.execute(sql)
                sql = f"SELECT * FROM game WHERE screen_name = '{username}'"
                cursor.execute(sql)
                user = cursor.fetchone()
                print("Tiedot päivitetty, aloitetaan peli !")
                game_starts = True

            elif answer == "c":
                username = input("Anna haluamasi käyttäjänimi: ")

    return user


def peliohjeet():
    print()
    print("Lentomatkan varrella sinulta kysytään kysymyksiä matkakohteesta.")
    print("Kysymykset ovat kolmen kohdan monivalintakysymyksiä.")
    print("Yhdestä tehtävästä voit saada 4 pistettä. Jos vastaat väärin, maximi pistemäärä laskee 2 pisteellä.")
    print("Tehtävä loppuu, jos pisteet laskevat nolliin.")
    print()
    print("Tehtävissä on aika, joka mittaa lentomatkasi pituutta.")
    print("Jos annettu aika ylittyy ennen kuin vastaat oikein, saat 0 pistettä.")
    print("Onnea vastaamiseen!")
    print()


def end():
    pygame.init()
    size = width, height = 600, 600
    white = 255, 255, 255
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("MVMN-Lentopeli")
    screen.fill(white)
    pygame.display.flip()

    #lentava lentokone
    logo = pygame.image.load("images/logo_game.png")
    logo_rect = logo.get_rect()
    logo_rect = logo_rect.move([1, height])
    flight = True
    x = 50
    y = height - 50
    while x < width-50:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        logo_rect.centerx = x
        y = 0.005*(x**2)-3.3*x+700
        logo_rect.centery = y

        screen.fill(white)
        screen.blit(logo, logo_rect)
        pygame.display.flip()
        x += 1
        time.sleep(0.01)

    # show all results from table results
    kursori = connection.cursor()
    sql = "select * from results;"
    kursori.execute(sql)
    tulokset = kursori.fetchall()
    print(screen, "TULOKSET", 250, 20)
    print(screen, "Nimi", 60, 80)
    print(screen, "Pisteet", 260, 80)
    print(screen, "Aika", 360, 80)
    rivi = 130
    for t in tulokset:
        print(screen, str(t[1]), 60, rivi)
        print(screen, str(t[2]), 260, rivi)
        print(screen, str(t[3]), 360, rivi)
        rivi += 40

    connection.close()
    time.sleep(5)
