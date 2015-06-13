
from google.appengine.ext import ndb

class Player( ndb.Model ):
    pass

class Score( ndb.Model ):
    game_name = ndb.StringProperty()
    game_level_number = ndb.IntegerProperty()
    player_name = ndb.StringProperty()
    value = ndb.IntegerProperty()
    registration_time = ndb.DateTimeProperty( auto_now_add = True )

    @classmethod
    def find_by_game( cls, game_name, limit = 20 ):
        return cls.query().filter( cls.game_name == game_name ).order( -cls.value ).fetch( limit )

class Game( ndb.Model ):
    alias = ndb.StringProperty( required = True )
    name = ndb.StringProperty( required = True )
    platforms = ndb.StringProperty( repeated = True )
    category = ndb.StringProperty()

    description = ndb.StringProperty()

    download_link_linux = ndb.StringProperty()
    download_link_osx = ndb.StringProperty()
    download_link_windows = ndb.StringProperty()
    download_link_java = ndb.StringProperty()
    
    store_link_chrome = ndb.StringProperty()
    store_link_android = ndb.StringProperty()
    store_link_ios = ndb.StringProperty()

