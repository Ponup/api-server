
import webapp2, os, logging

from webapp2_extras import routes

import controller.score as score
import controller.game as game

import webob.exc

routes = [
	webapp2.Route( '/score/list', handler = score.ListController ),
	webapp2.Route( '/score/add', handler = score.AddController ),
	webapp2.Route( '/game/list', handler = game.ListController ),
	webapp2.Route( '/game/add', handler = game.AddController ),
]

def error_handler( request, response, exception ):
	if type( exception ) == webob.exc.HTTPNotFound:
		response.set_status( 404 )
		response.write( 'Resource not found' )
	else:
		logging.exception( exception )
		response.write( 'Internal error' )

app = webapp2.WSGIApplication( routes, debug = True )
app.error_handlers[404] = error_handler
app.error_handlers[500] = error_handler

