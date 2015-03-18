
import webapp2
import json

from models import Score

class ListController( webapp2.RequestHandler ):

	def get( self ):
		game_name = self.request.get( 'game_name' )

		scores = [ score.to_dict() for score in Score.find_by_game( game_name, 20 ) ]

		body = json.dumps( scores )

		self.response.content_type = 'application/json'
		self.response.write( body )

class AddController( webapp2.RequestHandler ):

	def post( self ):
		self.get()

	def get( self ):
		game_name = self.request.get( 'game_name' )
		player_name = self.request.get( 'player_name' )
		value = int( self.request.get( 'value' ) )

		body = json.dumps( True )

		model = Score()
		model.game_name = game_name
		model.player_name = player_name
		model.value = value
		model.put()
		
		self.response.content_type = 'application/json'
		self.response.write( body )

