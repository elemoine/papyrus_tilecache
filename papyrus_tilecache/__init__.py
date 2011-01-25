from pyramid.config import Configurator

from papyrus_tilecache.views import load_tilecache_config

def add_route(config):
    load_tilecache_config(config.get_settings())
    config.add_route('tilecache', '/tilecache{path:.*?}',
                     view='papyrus_tilecache.views:tilecache'
                     )

def includeme(config):
    add_route(config)

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include(includeme)

    return config.make_wsgi_app()


