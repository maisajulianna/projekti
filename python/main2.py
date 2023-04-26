import misc
import start
import choises
import questions


# alkumäärittelyjä
connection = misc.connection()

kokonaispisteet_lista = []
kokonaispisteet_summa = 0
aikaakulunut = 0
MainGameOver = False



# asking username and welcoming player
start.welcome()
user = start.get_user()
misc.timenoprint(1)


# --- MAIN PELI:

# lentokoneen ja lähtöpaikan valinta
planeNumber = choises.choose_plane()

result = choises.choose_start()
start_airport = result[0]
start_continent = result[1]


# ensimmäisen matkakohteen valinta
choises.user_continents(user)


print()
result = choises.travel(start_continent)
travel_airport = result[0]
travel_ident = result[1]
travel_continent = result[2]
MainGameOver = result[3]

start.peliohjeet()

# 1. kohde
print("Lento alkaa.")
print()
result = questions.which_question(travel_continent, planeNumber)
kokonaispisteet_lista = result[0]
pisteitä = result[1]

result = questions.pistelaskuri(kokonaispisteet_lista)
kokonaispisteet_summa = result[0] + pisteitä
aikaakulunut = result[1]

misc.save_result(user, aikaakulunut, kokonaispisteet_summa, travel_ident)
planeNumber = misc.choose_options(planeNumber)


continue_ = misc.save_result(user, aikaakulunut, kokonaispisteet_summa, travel_ident)
while not continue_:
    choises.user_continents(user)
    print()
    result = choises.travel()
    travel_airport = result[0]
    travel_ident = result[1]
    travel_continent = result[2]
    # MainGameOver = result[3]

    print("Lento alkaa.")
    print()
    result = questions.which_question(travel_continent, planeNumber)
    kokonaispisteet_lista = result[0]
    pisteitä = result[1]

    result = questions.pistelaskuri(kokonaispisteet_lista)
    kokonaispisteet_summa = result[0] + pisteitä
    print(f"Sinulla on tällä hetkellä {kokonaispisteet_summa} pistettä")
    aikaakulunut = result[1]

    continue_ = misc.save_result(user, aikaakulunut, kokonaispisteet_summa, travel_ident)
    planeNumber = misc.choose_options(planeNumber)

# game over screen
start.end()

print("Peli loppui!")