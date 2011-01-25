papyrus_tilecache
=================

papyrus_tilecache provides an easy and convenient method for embeding
TileCache in Pyramid applications.

Install
-------

papyrus_tilecache can be installed with ``easy_install``::

    $ easy_install papyrus_tilecache

Often you'll want to make papyrus_tilecache a dependency of your Pyramid
application, which is done by adding ``papyrus_tilecache`` to the
``install_requires`` list defined in the Pyramid application's ``setup.py``
file.

Embed TileCache
---------------

Embeding TileCache in a Pyramid application is easy.

Edit the application's ``development.ini`` file and, in the main section
(``[app:]``), set ``tilecache.cfg`` to the location of the TileCache config
file. Example::

    [app:MyApp]
    use = egg:MyApp
    ...
    tilecache.cfg = %(here)s/tilecache.cfg

In this example the TileCache config file is located at the same location as
the ``development.ini`` file.

You can use the following TileCache config as an example::

    [cache]
    type=Disk
    base=/tmp/tilecache
    [basic]
    type=WMS
    url=http://vmap0.tiles.osgeo.org/wms/vmap0
    extension=png

Now, edit the application's main file, ``__init__.py``, and register
papyrus_tilecache using the ``Configurator.include`` method::

    def main(global_config, **settings):

        config = Configurator(settings=settings)

        import papyrus_tilecache
        config.include(papyrus_tilecache)

That's it! The Pyramid application now exposes a TileCache service at
``/tilecache``.

`Test URL <http://localhost:6543/tilecache?LAYERS=basic&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&STYLES=&EXCEPTIONS=application/vnd.ogc.se_inimage&FORMAT=image/jpeg&SRS=EPSG:4326&BBOX=-180,0,-90,90&WIDTH=256&HEIGHT=256>`_
