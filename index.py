
import webapp2, os, logging

from webapp2_extras import routes

import controller.score as score

routes = [
	webapp2.Route( '/score/list', handler = score.ListController ),
	webapp2.Route( '/score/add', handler = score.AddController ),
]

def handle_error( request, response, exception ):
	logging.exception( exception )

	controller = ErrorPageController( request, response )
	controller.get()

app = webapp2.WSGIApplication( routes, debug = True )
app.error_handlers[404] = handle_error
app.error_handlers[500] = handle_error

