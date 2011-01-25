from pyramid.config import Configurator

from papyrus_tilecache.views import load_tilecache_config

def add_route(config):
    """ Add a route to the tilecache view callable. The TileCache
    service is made available at ``/tilecache``.

    Arguments:

    * ``config``: the ``pyramid.config.Configurator`` object.
    """
    return config.add_route('tilecache', '/tilecache{path:.*?}',
                            view='papyrus_tilecache.views:tilecache'
                            )

def includeme(config):
    """ The callable making it possible to include papyrus_tilecache
    in a Pyramid application.

    Calling ``config.include(papyrus_tilecache)`` will result in this
    callable being called.

    Arguments:

    * ``config``: the ``pyramid.config.Configurator`` object.
    """
    load_tilecache_config(config.get_settings())
    add_route(config)

def main(global_config, **settings):
    """ Return the Pyramid application.
    """
    config = Configurator(settings=settings)
    config.include(includeme)
    return config.make_wsgi_app()


