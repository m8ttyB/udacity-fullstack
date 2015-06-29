-- Start with a clean slate each time we run the schema file
\c postgres;
DROP DATABASE tournament;
CREATE DATABASE tournament;

-- Create the tables
\c tournament;

CREATE TABLE players (
  user_id	SERIAL primary key,
  user_name	VARCHAR(40) not null
);

CREATE TABLE matches (
  winner_user_id INT references players(user_id) not null,
  loser_user_id INT references players(user_id) not null
);

-- Create the views
CREATE VIEW player_wins AS
	SELECT players.user_id, players.user_name, COUNT(winner_user_id) AS wins
		FROM players LEFT JOIN matches
			ON players.user_id = matches.winner_user_id
			AND matches.winner_user_id > 0
		GROUP BY players.user_id,  winner_user_id;

CREATE VIEW player_losses AS
	SELECT players.user_id, players.user_name, COUNT(loser_user_id) AS losses
		FROM players LEFT JOIN matches
			ON players.user_id = matches.loser_user_id
		GROUP BY players.user_id,  loser_user_id;