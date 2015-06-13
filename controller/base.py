
import webapp2, json

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime):
        return { 'date': obj.date().isoformat(), 'time': obj.time().isoformat() }

    raise TypeError ("Type not serializable")

class BaseController( webapp2.RequestHandler ):

    def send_json_response( self, string ):
	json_string = json.dumps( string, default = json_serial )
        self.response.headers.add_header( 'Access-Control-Allow-Origin', '*' )
        self.response.content_type = 'application/json'
        self.response.write( json_string )

