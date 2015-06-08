
import webapp2
import json

from models import Score

from datetime import datetime

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime):
        return { 'date': obj.date().isoformat(), 'time': obj.time().isoformat() }

    raise TypeError ("Type not serializable")

class ListController( webapp2.RequestHandler ):

	def get( self ):
		game_name = self.request.get( 'game_name' )
                limit = int( self.request.get( 'limit', '20' ) )

		scores = [ score.to_dict() for score in Score.find_by_game( game_name, limit ) ]

		body = json.dumps( scores, default = json_serial )

                self.response.headers.add_header( 'Access-Control-Allow-Origin', '*' )
		self.response.content_type = 'application/json'
		self.response.write( body )

class AddController( webapp2.RequestHandler ):

	def post( self ):
		self.get()

	def get( self ):
		game_name = self.request.get( 'game_name' )
		game_level_number = self.request.get( 'game_level_number', None )
                if game_level_number: game_level_number = int( game_level_number )
		player_name = self.request.get( 'player_name' )
		value = int( self.request.get( 'value' ) )

		body = json.dumps( True )

		model = Score()
		model.game_name = game_name
                model.game_level_number = game_level_number
		model.player_name = player_name
		model.value = value
		model.put()
		
                self.response.headers.add_header( 'Access-Control-Allow-Origin', '*' )
		self.response.content_type = 'application/json'
		self.response.write( body )

