import pygame
import time
import misc
import sys

connection = misc.connection()

def print_text(screen, message, x, y, font_color=(0,0,0),
               font_type="images/magneto_bold.ttf", font_size=20):

    # funktio näyttää tekstiä peli-ikkunassa
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x,y))
    pygame.display.flip()

def welcome():
    # Näytämme pelin tarinan ja lentävän lentokoneen, kunnes käyttäjä napsauttaa ENTER
    pygame.init()
    size = width, height = 600, 600
    speed = [1, 1]                  # lennon kuvan muutos videon aikana
    black = 0, 0, 0
    white = 255, 255, 255
    need_input = False
    screen = pygame.display.set_mode(size)
    logo = pygame.image.load("images/logo_game.png")
    tarina = pygame.image.load("images/tarina.png")
    logo_rect = logo.get_rect()
    tarina_rect = tarina.get_rect()
    logo_rect = logo_rect.move([1,height])
    pygame.display.set_caption("MVMN-Lentopeli")
    show_welcome = True
    while show_welcome:
            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                    sys.exit()
                 if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    show_welcome = False

            logo_rect = logo_rect.move([1,-1])
            screen.fill(white)
            screen.blit(tarina, tarina_rect)
            screen.blit(logo, logo_rect)
            pygame.display.flip()
            time.sleep(0.01)
    pygame.quit()


def get_user():
    # ask user_name
    pygame.init()
    size = width, height = 600, 600
    white = 255, 255, 255
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("MVMN-Lentopeli")
    screen.fill(white)
    pygame.display.flip()
    print_text(screen, "Aloitetaan...", 10, 1)
    print_text(screen, "Anna haluamasi käyttäjänimi: ", 10, 30)
    need_input = True
    user_name = ''
    while need_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if need_input and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        need_input = False

                    elif event.key == pygame.K_BACKSPACE:
                        user_name = user_name[0:-1]
                        screen.fill(white)
                        print_text(screen, "Aloitetaan...", 10, 1)
                        print_text(screen, "Anna haluamasi käyttäjänimi: ", 10, 30)
                        pygame.display.flip()
                        print_text(screen, user_name, 350, 30)

                    elif len(user_name) < 20:
                        user_name = user_name + event.unicode
                        print_text(screen, user_name, 350, 30)

    print_text(screen, "Hei, " + user_name + "!", 10, 90)
    # time.sleep(3)
    #check if user_name already exists in the table game (not finished games)

    sql = "select * from game where screen_name = '" + user_name + "';"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()

    if not result:  #Jos tietokannassa ei ole samannimistä käyttäjää
        print_text (screen, user_name + ", sinulla ei ole keskeneräisiä pelejä.", 10, 120)
        print_text(screen, "Aloitetaan uusi peli hetken kuluttua...", 10, 150)
        # add user to DB
        sql = "insert into game values (NULL, 0,'" + user_name + "',"\
              " 0, NULL, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE)"
        cursor.execute(sql)
        sql = "select * from game where screen_name = '" + user_name + "';"
        cursor.execute(sql)
        user = cursor.fetchone()    # user - kaikki tiedot nykyisestä pelaajasta
        need_input = False
        # time.sleep(3)
        pygame.quit()

    else: #Jos tietokannassa on samannimistä käyttäjää
        print_text(screen, "Olet jo aloittanut pelaamisen, haluatko jatkaa?", 10, 120)
        print_text(screen, "a - vaihda käyttäjänimi", 10, 180)
        print_text(screen, "b - aloita uusi peli ja poista vanhan pelin tulokset", 10, 210)
        # print_text(screen, "c - jatka viimeistä peliä", 10, 150)
        need_input = True
        while need_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if need_input and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                       print_text(screen, "a", 10, 240)
                       # time.sleep (3)
                       user = result               # user - kaikki tiedot nykyisestä pelaajasta
                       need_input = False
                    if event.key == pygame.K_b:    # "vanha" pelaaja aloittaa uuden pelin -
                                                   # on poistettava kaikki tiedot edellisestä pelistä
                        print_text(screen, "b", 10, 240)
                        sql = "update game set AF_= FALSE, AN_ = FALSE, AS_ = FALSE, " + \
                              "EU_= FALSE, NA_ = FALSE, OC_= FALSE,SA_ = FALSE, time_sec = 0, " + \
                              "score = 0, last_location = NULL where player_id=" + str(result[0])
                        cursor.execute(sql)
                        sql = "select * from game where player_id=" + str(result[0])
                        cursor.execute(sql)
                        user = cursor.fetchone() # user - kaikki tiedot nykyisestä pelaajasta
                        need_input = False
                        time.sleep(3)
                    if event.key == pygame.K_a:
                        print_text(screen, "c", 10, 240)
                        need_input = False
                        user = get_user()  # Varoitus, rekursio!
    pygame.quit()
    return user

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
    # print(user)

    game_starts = False
    while game_starts == False:
        if not user:
            print("Sinulla ei ole keskeneräistä peliä, uusi alkaa hetken kuluttua...")
            sql = f"INSERT INTO game VALUES (NULL, 0, '{username}', 0, NULL, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE)"
            cursor = connection.cursor()
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
                sql = "UPDATE game SET AF_= FALSE, AN_ = FALSE, AS_ = FALSE, " \
                      "EU_= FALSE, NA_ = FALSE, OC_= FALSE, SA_ = FALSE, time_sec = 0, " \
                      f"score = 0, last_location = NULL WHERE player_id = '{username}'"
                cursor = connection.cursor()
                cursor.execute(sql)
                user = cursor.fetchall()
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
    print_text(screen, "TULOKSET", 250, 20)
    print_text(screen, "Nimi", 60, 80)
    print_text(screen, "Pisteet", 260, 80)
    print_text(screen, "Aika", 360, 80)
    rivi = 130
    for t in tulokset:
        print_text(screen, str(t[1]), 60, rivi)
        print_text(screen, str(t[2]), 260, rivi)
        print_text(screen, str(t[3]), 360, rivi)
        rivi += 40

    connection.close()
    time.sleep(5)