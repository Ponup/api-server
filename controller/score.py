
from base import BaseController
from models import Score
from datetime import datetime

class ListController( BaseController ):

	def get( self ):
		game_name = self.request.get( 'game_name' )
                limit = int( self.request.get( 'limit', '20' ) )

		scores = [ score.to_dict() for score in Score.find_by_game( game_name, limit ) ]
                self.send_json_response( scores )

class AddController( BaseController ):

	def post( self ):
		self.get()

	def get( self ):
		game_name = self.request.get( 'game_name' )
		game_level_number = self.request.get( 'game_level_number', None )
                if game_level_number: game_level_number = int( game_level_number )
		player_name = self.request.get( 'player_name' )
		value = int( self.request.get( 'value' ) )

		model = Score()
		model.game_name = game_name
                model.game_level_number = game_level_number
		model.player_name = player_name
		model.value = value
		model.put()
	
                self.send_json_response( True )

