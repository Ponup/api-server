
import webapp2, json

import logging

from datetime import datetime

from google.appengine.api import memcache

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime):
        return { 'date': obj.date().isoformat(), 'time': obj.time().isoformat() }

    raise TypeError ("Type not serializable")

class BaseController( webapp2.RequestHandler ):

    cache_ttl = 60

    def get_cache_key( self ):
        ''' Returns the cache key string, or None if cache is disabled for the controller (default) '''
        return None

    def get( self ):
        cache_key = self.get_cache_key()
        if cache_key is not None:
            cached_body = self.get_cached_body( cache_key )
            if cached_body is not None:
                self.send_json_response( cached_body, False )
                return
        body = self.do_get()
        self.cache_body( cache_key, body )
        self.send_json_response( body, False )

    def get_cached_body( self, cache_key ):
        return memcache.get( cache_key )

    def cache_body( self, cache_key, body ):
        logging.debug( 'saving cached body for "%s"' % cache_key )
        memcache.add( cache_key, body, self.cache_ttl )

    def data_to_json_string( self, data ):
	return json.dumps( data, default = json_serial )

    def send_json_response( self, data, convert = True ):
	json_string = self.data_to_json_string( data ) if convert else data 
	self.send_response( 'application/json', json_string, { 'Access-Control-Allow-Origin': '*' } )

    def send_response( self, content_type, body, headers = None ):
        if isinstance( headers, dict ):
            for key, value in headers.iteritems():
                self.response.headers.add_header( key, value )
        self.response.content_type = content_type 
        self.response.write( body )


