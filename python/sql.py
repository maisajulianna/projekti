"""

user="userN",
password="1234"

DROP TABLE goal_reached;
DROP TABLE goal;
DROP TABLE game;


CREATE TABLE GAME (
player_id INTEGER not NULL PRIMARY KEY AUTO_INCREMENT,
time_sec INTEGER DEFAULT 0,
screen_Name VARCHAR(20),
score INTEGER DEFAULT 0,
last_location VARCHAR(40),
AF_ BOOLEAN DEFAULT FALSE, AN_ BOOLEAN DEFAULT FALSE, AS_ BOOLEAN DEFAULT FALSE,
EU_ BOOLEAN DEFAULT FALSE, NA_ BOOLEAN DEFAULT FALSE, OC_ BOOLEAN DEFAULT FALSE,
SA_ BOOLEAN DEFAULT FALSE,
FOREIGN KEY (last_location) REFERENCES airport(ident) ON UPDATE CASCADE ON DELETE NO ACTION);



CREATE TABLE RESULTS (
player_id INTEGER NOT NULL,
screen_name VARCHAR(20),
score INTEGER,
time_sec INTEGER);



CREATE TABLE plane_info(
id INT NOT NULL,
emission INT(3) null,
risk INT(3) null,
questions INT(3) null,
velocity INT(3)null,
type VARCHAR(40));
INSERT INTO plane_info(id, emission, risk, questions, velocity, type)
VALUES (1, 2, 2, 16, 8,'vähänpästoinen');
INSERT INTO plane_info(id, emission, risk, questions, velocity, type)
VALUES (2, 4, 2, 12, 8,'matkustajankone');
INSERT INTO plane_info(id, emission, risk, questions, velocity, type)
VALUES (3, 8, 4, 8, 4,'yksityiskone');
INSERT INTO plane_info(id, emission, risk, questions, velocity, type)
VALUES (4, 16, 8, 4, 2,'hävittäjä');



CREATE TABLE start_airports(
  id int(11) NOT null,
  ident varchar(40) NOT NULL,
  type varchar(40) DEFAULT NULL,
  name varchar(40) DEFAULT NULL,
  continent varchar(40) DEFAULT NULL,
  iso_country varchar(40) DEFAULT NULL,
  municipality varchar(40) DEFAULT NULL,
  keywords varchar(40) DEFAULT NULL,
  PRIMARY KEY (ident),
  FOREIGN KEY (iso_country) REFERENCES country(iso_country)
  )start_airports

INSERT INTO plane_info(id, emission, risk, questions, velocity)
VALUES ('1', '2', '20', '4', '8'), ('2', '2', '20', '4', '8'), ('3', '8', '40', '2', '4'), ('4', '16', '60', '1', '2');



CREATE TABLE questions (
id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
question VARCHAR(200),
option_1 VARCHAR(40),
option_2 VARCHAR(40),
option_3 VARCHAR(40)
);

INSERT INTO questions(question, option_1, option_2, option_3)
VALUES("Montako prosenttia Surinamen pinta-alasta on metsää?", "94,6 prosenttia", "73,1 prosenttia", "53,4 prosenttia"),
("Venezuelassa sijaitsee Heladeria Coromoto -jäätelöbaari, jossa on maailman "
"laajin makuvalikoima. Montako eri jäätelömakua siellä on saatavilla?", "860", "91", "157"),
("Montako miljoonakaupunkia Brasiliassa on?", "13", "7", "21"),
("Montako valtiota Etelä-Amerikassa on?", "12", "17", "9"),
("Minkä valtion virallisia kolikoita koristavat Pokemon-, Disney- ja Star Wars -hahmot?", "Niue", "Australia", "Uusi-Seelanti"),
("Montako maata Oseaniaan kuuluu?", "23", "12", "18"),
("Montako kengurulajia Australiassa on?", "Yli 50", "27", "Yli 90"),
("Paljonko painoindeksi on Naurussa asukasta kohden?", "34-35", "20-21", "26-28"),
("Mitä Guamin saarelta ei löydy lainkaan?", "Hiekkaa", "Asfalttia", "Soraa"),
("Kuinka pitkä on Kanadan rantaviiva?", "202 080 kilometriä", "130 421 kilometriä", "190 134 kilometriä"),
("Montako kansallispuistoa Yhdysvalloissa on?", "58", "32", "101"),
("Montako ihmistä Meksikossa on kadonnut viimeisen vuosikymmenen aikana?", "Yli 27 000", "Noin 9000", "Noin 15 000"),
("Monelleko aikavyöhykkeelle Ranska ulottuu, kun otetaan huomioon sen territoriot ja alusmaat?", "12", "5", "9"),
("Missä maassa sijaitsee Longyearbyen kaupunki, jossa 'kuoleminen on kiellettyä', koska kylmyyden vuoksi ruumiit eivät maadu?",
"Norjassa", "Ruotsissa", "Islannissa"),
("Missä maassa sijaitsee mikrovaltio Ladonia?", "Ruotsissa", "Italiassa", "Kreikassa"),
("Kuinka suuri osa Kosovon asukkaista on alle 25-vuotiaita?", "Puolet", "Neljännes", "Noin 10%"),
("Missä maassa sijaitsee maailman korkein vapaasti seisova lipputanko (165m)?", "Tadzikistanissa", "Kiinassa", "Bhutanissa"),
("Montako maatilaa on Singaporessa?", "0", "9", "37"),
("Malediivit sijaitsee Intian valtamerellä ja on maailman matalin valtio. Paljonko sen korkeus on keskimäärin merenpinnasta?", "2,1m", "3,2m", "5,5m"),
("Montako jokea virtaa Saudi-Arabiassa?", "0", "1", "3"),
("Paljonko on Etelämantereen mannerjään keskimääräinen paksuus?", "2,5km", "1,4km", "4,1km"),
("Kuinka nopeita Etelämantereen tuulet voivat olla pahimmillaan?", "320km/h", "35m/s", "235km/h"),
("Montako millimetriä Etelämantereella sataa vuosittain?", "50mm", "89mm", "150mm"),
("Kuinka monta prosenttia maapallon jäästä sijaitsee Etelämantereella?",  "90 prosenttia", "69 prosenttia", "79 prosenttia"),
"Montaako kieltä Afrikassa puhutaan?", "Yli 2000", "Noin 1300", "830"),
("Missä Afrikan maassa on eniten pyramideja?", "Sudanissa", "Egyptissä", "Libyassa"),
("Milloin Etiopiassa juhlitaan uutta vuotta?", "11.9.", "1.1.", "24.5."),
("Mikä on Afrikan pinta-ala?", "30 365 000 neliökilometriä", "21 222 421 neliökilometriä", "18 032 341 neliökilometriä");


DELETE FROM airport WHERE type = 'closed' OR type = 'seaplane_base' OR TYPE = 'heliport'

DELETE FROM country WHERE iso_country NOT IN (SELECT iso_country FROM airport WHERE airport.iso_country = country.iso_country)

UPDATE airport
SET municipality = 'Not in any municipality'
WHERE municipality = ''
"""