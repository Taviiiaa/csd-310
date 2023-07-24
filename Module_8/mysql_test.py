CREATE USER 'pysports_user'@'localhost'  IDENTIFIED WITH mysql_native_password BY  'Hazel0101!' ;

GRANT ALL PRIVILEGES ON pysports.* TO 'pysports_user'@'localhost'

-- drop test user if exists 
DROP USER IF EXISTS 'pysports_user'@'localhost';

CREATE TABLE team (
    team_id     INT             NOT NULL        AUTO_INCREMENT,
    team_name   VARCHAR(75)     NOT NULL,
    mascot      VARCHAR(75)     NOT NULL,
    PRIMARY KEY(team_id)
); 

CREATE TABLE player (
    player_id   INT             NOT NULL        AUTO_INCREMENT,
    first_name  VARCHAR(255)     NOT NULL,
    last_name   VARCHAR(255)     NOT NULL,
    team_id     INT             NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team 
    FOREIGN KEY(team_id)
        REFERENCES team(team_id)
);


#Insert 
INSERT INTO team(team_name, mascot)
    VALUES('Team Red ', 'Red Robins');

INSERT INTO team(team_name, mascot)
    VALUES('Team Blue', 'Blue Birds');

-- drop tables if they are present
DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS team;

--Insert player into the teams

INSERT INTO team(team_name, mascot) VALUES('Team Red', 'Red Robins'); INSERT INTO team(team_name, mascot) VALUES('Team Blue', 'Blue Birds');

INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Michelle', 'Grace', (SELECT team_id FROM team WHERE team_name = 'Team Blue'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Larry', 'Haze', (SELECT team_id FROM team WHERE team_name = 'Team Blue'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Zach', 'Baldwin', (SELECT team_id FROM team WHERE team_name = 'Team Blue'));

INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Bailey', 'Jones', (SELECT team_id FROM team WHERE team_name = 'Team Red'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Molly', 'Brown', (SELECT team_id FROM team WHERE team_name = 'Team Red'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Justin', 'Bieber', (SELECT team_id FROM team WHERE team_name = 'Team Red'));


#Import_into_database

import mysql.connector 
from mysql.connector import errorcode

#Config_Database 

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host" : "localhost",
    "database": "pysports",
    "raise_on_warnings": True
}

try:

    database = mysql.connector.connect(**config) 
    
    # output the connection status 
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    database.close()
