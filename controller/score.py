
import webapp2

class ListController( webapp2.RequestHandler ):

	def get( self ):
		domainUrl = self.request.get( 'domainUrl' )
		channelId = self.request.cookies.get( 'channelId' )

		body = """
		[{"playerName":"santi","value":142},{"playerName":"pablo","value":21}]
		"""
		self.response.write( body )

class AddController( webapp2.RequestHandler ):

	def get( self ):
		domainUrl = self.request.get( 'domainUrl' )
		channelId = self.request.cookies.get( 'channelId' )
		
		self.response.write( 'cool' )

