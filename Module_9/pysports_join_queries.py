import select
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}


try:
    """ try/catch block for handling potential MySQL database errors """

# connect to the pysports database 

    database = mysql.connector.connect(**config) 
    
    cursor = database.cursor()

#inner_join 

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    player = cursor.fetchall()

    print("\n  -- DISPLAYING TEAM RECORDS --")
    
    for player in player:
        print(f"  Player ID: {player[0]}\n  First Name: {player[1]}\n  Last Name: {player[2]}\n  Team ID: {player[3]}\n")

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

