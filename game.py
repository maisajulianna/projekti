import string, random
from airport import Airport
import config


class Game:

    def __init__(self, id, loc, player=None):
        self.status= {}
        self.location = []

        if id == 0:
             # new game
             # Create new game id
            letters = string.ascii_lowercase + string.ascii_uppercase + string.digits

            self.status = {
                "id": ''.join(random.choice(letters) for i in range(20)),
                "name": player,
                "game_over": False,
                "visited_location": {
                    "AN_": False,
                    "AS_": False,
                    "EU_": False,
                    "NA_": False,
                    "OC_": False,
                    "AF_": False,
                    "SA_": False
                }
            }


            # define continent of the loc
            self.location.append(Airport(loc, True))
            sql = 'select continent from airport where ident="' + loc + '"'
            cur = config.conn.cursor()
            cur.execute(sql)
            res = cur.fetchall()

            # Insert new game into DB

            sql = "INSERT INTO game (id, screen_Name, last_location, AN_,AS_,EU_,NA_,OC_,AF_,SA_) VALUES ('" + \
                  str(self.status["id"]) + "','" + str(player) + "','" + loc + "', FALSE, FALSE, FALSE, FALSE, FALSE, FALSE,FALSE)"
            print(sql)
            cur = config.conn.cursor()
            cur.execute(sql)

            # define continent of the loc in the game table

            sql = "select continent from airport where ident='" + loc + "'"
            #print(sql)
            cur = config.conn.cursor()
            cur.execute(sql)
            res = cur.fetchall()
            sql = "update game set " + str(res[0][0]) + "_= TRUE where id = '" + str(self.status["id"])+ "'"
            #print(sql)
            cur = config.conn.cursor()
            cur.execute(sql)

            # config.conn.commit()

        else:
            # add current location to db

            sql = "select continent from airport where ident='" + loc + "'"
            #print(sql)
            cur = config.conn.cursor()
            cur.execute(sql)
            res = cur.fetchall()
            sql = "update game set " + str(res[0][0]) + "_= TRUE where id = '" + str(id) + "'"
            #print(sql)
            cur = config.conn.cursor()
            cur.execute(sql)

            # find game from DB
            sql = "SELECT id, last_location, screen_Name, AN_,AS_,EU_,NA_,OC_,AF_,SA_ FROM Game WHERE id='" + id + "';"
            cur = config.conn.cursor()
            cur.execute(sql)
            res = cur.fetchall()
            if len(res) == 1:
                # game found
                self.status = {
                    "id": res[0][0],
                    "name": res[0][2],
                    "game_over": res[0][3]*res[0][4]*res[0][5]*res[0][6]*res[0][7]*res[0][8]*res[0][9],
                    "visited_location": {
                        "AN_": res[0][3],
                        "AS_": res[0][4],
                        "EU_": res[0][5],
                        "NA_": res[0][6],
                        "OC_": res[0][7],
                        "AF_": res[0][8],
                        "SA_": res[0][9]
                    }
                }
                # old location in DB currently not used

                apt = Airport(loc, True)
                self.location.append(apt)

                sql = "SELECT AN_*AS_*EU_*NA_*OC_*AF_*SA_ FROM Game WHERE id='" + id + "';"
                cur = config.conn.cursor()
                cur.execute(sql)
                self.game_over = cur.fetchall()

            else:
                print("************** PELIÄ EI LÖYDY! ***************")