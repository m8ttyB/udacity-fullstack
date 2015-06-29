#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

from bleach import clean
import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    query = 'DELETE FROM matches;'

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()

def deletePlayers():
    """Remove all the player records from the database."""
    query = 'DELETE FROM players;'

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    query = 'SELECT count(*) FROM players;'

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    player_count = cursor.fetchall()
    conn.close()

    return int(player_count[0][0])


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    query = 'INSERT INTO players VALUES (DEFAULT, %s);'

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query, (clean(name),))
    conn.commit()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    query = """SELECT p.user_id, p.user_name, p.wins,
                    SUM(p.wins + l.losses) AS matches
                FROM player_wins p, player_losses l
                WHERE p.user_id = l.user_id
                GROUP BY p.user_id, p.user_name, p.wins, l.losses
            ORDER BY p.wins DESC;"""

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()

    return results

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    query = 'INSERT INTO matches VALUES (%s, %s);'

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query, (clean(winner), clean(loser)))
    conn.commit()
    conn.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    query = """SELECT a.user_id, a.user_name, b.user_id, b.user_name
                FROM player_wins a, player_wins b
                    WHERE a.wins = b.wins
                    AND a.user_id < b.user_id;"""

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    pairings = cursor.fetchall()
    conn.close()

    # if the length of the swiss pairs list is != half the player count, the
    # game is over and we have a winner
    if len(pairings) == countPlayers() / 2:
        return pairings
    else:
        return []

