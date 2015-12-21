
from base import BaseController
from models import Score

class ListController( BaseController ):

        default_list_limit = '20'

        def get_request_params( self ):
                return {
		    'game_name': self.request.get( 'game_name' ),
                    'limit': int( self.request.get( 'limit', self.default_list_limit ) )
                }
        
        def get_cache_key( self ):
                params = self.get_request_params()
                return 'score_list_%s_%d' % ( params['game_name'], params['limit'] )

	def do_get( self ):
	        params = self.get_request_params()

		scores = [ score.to_dict() for score in Score.find_by_game( params['game_name'], params['limit'] ) ]
                return self.data_to_json_string( scores )

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

