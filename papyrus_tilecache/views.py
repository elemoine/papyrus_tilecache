import time
import email
import ConfigParser

from pyramid.wsgi import wsgiapp

from TileCache.Service import Service, wsgiHandler


# default expiration time is set to 1 year
DEFAULT_EXPIRATION = 3600*24*365

# TileCache Service instance
_service = None

def load_tilecache_config(settings):
    """ Load the TileCache config.

    This function calls ``TileCache.Service.Service.load`` and
    stores the return value in a private global variable.

    Arguments:

    * ``settings``: a dict with a ``tilecache.cfg`` key whose
      value provides the path to TileCache configuratio file.
    """
    global _service
    _service = Service.load(settings.get('tilecache.cfg'))

@wsgiapp
def tilecache(environ, start_response):
    try:
        expiration = _service.config.getint('cache', 'expire')
    except ConfigParser.NoOptionError:
        expiration = DEFAULT_EXPIRATION

    # custom_start_response adds cache headers to the response
    def custom_start_response(status, headers, exc_info=None):
        headers.append(('Cache-Control', 'public, max-age=%s'
            % expiration))
        headers.append(('Expires', email.Utils.formatdate(
            time.time() + expiration, False, True)))
        return start_response(status, headers, exc_info)

    return wsgiHandler(environ, custom_start_response, _service)

