#!../framework/bin/python
from game import *
from flask import Flask, jsonify, abort,redirect,request
from player import *

app = Flask(__name__)

"""game list"""
_games_ = {}

"""player list"""
_players_ = {}

"""index of games"""
index = 0

#only for testing
@app.route("/printPlayers", methods = ['GET'])
def print_players():
	for item in _players_:
		print _players_[item].username + " " + _players_[item].ip
	return "",200

#only for testing
@app.route("/printGames", methods = ['GET'])
def print_games():
	for item in _games_:
		print _games_[item]
	return "",200

@app.route("/")
def hello():
	return "sono il server di anno domini\n"

@app.route('/createPlayer/<string:username>', methods = ['POST'])
def create_p(username):
	new_p = Player(username)
	if new_p.username not in _players_:
		_players_[new_p.username] = new_p
	else:
		return "Username already chosen\n", 400
	return "", 201

@app.route('/createGame/<string:username>/<int:n_players>', methods = ['POST'])
def create_g(username, n_players):
	global index 
	if username in _players_:
		try:
			new_g = Game(index, _players_[username], n_players)
		except PlayersNumberRangeException:		
			return "Wrong number of players\n", 400
		except CreatorNotFoundException:
			return "Creator non found\n", 400
		_games_[index] = new_g
		index = index + 1
	else:
		return "Unknown username\n", 400
	return new_g.to_json(), 201 
	#TODO Perche restituire il json con tutto il game? Bisognerebbe restituire solo l'ID del game.
	#[Stefano] non lo so poi ci ragioniamo quando siamo insieme

@app.route('/joinGame/<string:username>/<int:game_id>', methods = ['PUT'])
def join_g(username, game_id):
	#Controllo che username e game_id siano stati passati correttamente
	if username not in _players_ or game_id not in _games_:
		return "Player or game not found\n", 400
	player = _players_[username]
	game = _games_[game_id]
	try:
		game.add_player(player)
	except PlayersNumberReachedException:
		return "Number of players already reached\n", 400
	except UserSubscriptionException:
		return "User is already subscripted\n", 400
	if game.player_n == len(game.p_list):
		game.start_game()
		ip = request.remote_addr
		for player in game.p_list:
			return "http://"+player.ip+"/start_Game"
		#return redirect("http://172.16.30.135:5000/")
	return "Game joined\n", 200

@app.route('/unsubscribe/<string:username>/<int:game_id>', methods = ['DELETE'])
def unsubscribe(username, game_id):
	#Controllo che username e game_id siano stati passati correttamente
	if username not in _players_ or game_id not in _games_:
		return "Player or game not found", 400
	try:
		_games_[game_id].remove_player(_players_[username])
	except UserNotFoundException:
		return "User not subscripted to the specified game", 400
	except CreatorUnsubscriptionException:
		return "Creator cannot be unsubscribed", 400
	return "User is not partecipating anymore", 200

if __name__ == '__main__':
	app.debug = True
	app.run()
