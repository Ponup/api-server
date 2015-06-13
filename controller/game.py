
from base import BaseController
from models import Game 
from datetime import datetime

class ListController( BaseController ):

	def get( self ):
		games = [ game.to_dict() for game in Game.query() ]
                self.send_json_response( games )

class AddController( BaseController ):

	def post( self ):
		self.get()

	def get( self ):
		alias = self.request.get( 'alias' )
		name = self.request.get( 'name' )
                platforms = self.request.get( 'platforms' ).split( ',' )
                category = self.request.get( 'category' )

                download_link_linux = self.request.get( 'download_link_linux' )
                download_link_osx = self.request.get( 'download_link_osx' )
                download_link_windows = self.request.get( 'download_link_windows' )
                download_link_java = self.request.get( 'download_link_java' )

                store_link_chrome = self.request.get( 'store_link_chrome' )
                store_link_android = self.request.get( 'store_link_android' )
                store_link_ios = self.request.get( 'store_link_ios' )

		model = Game()
                model.alias = alias
                model.name = name
                model.platforms = platforms
                model.category = category

                model.download_link_linux = download_link_linux
                model.download_link_osx = download_link_osx
                model.download_link_windows = download_link_windows
                model.download_link_java = download_link_java

                model.store_link_chrome = store_link_chrome
                model.store_link_android = store_link_android
                model.store_link_ios = store_link_ios
		model.put()
	
                self.send_json_response( True )

