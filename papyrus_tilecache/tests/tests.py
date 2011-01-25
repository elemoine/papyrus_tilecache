import os
import unittest

from pyramid import testing

class LoadTileCacheConfigTests(unittest.TestCase):
    def test(self):
        from papyrus_tilecache.views import load_tilecache_config
        curdir = os.path.dirname(os.path.abspath(__file__))
        cfgfile = os.path.join(curdir, 'tilecache.cfg')
        settings = {'tilecache.cfg': cfgfile}
        load_tilecache_config(settings)
        from papyrus_tilecache.views import _service
        from TileCache.Service import Service
        self.assertTrue(isinstance(_service, Service))
        self.assertTrue(_service.config.has_section('basic'))

class AddRouteTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test(self):
        from papyrus_tilecache import add_route
        route = add_route(self.config)
        from pyramid.urldispatch import Route
        self.assertTrue(isinstance(route, Route))
        self.assertEqual(route.name, 'tilecache')
        self.assertEqual(route.pattern, '/tilecache{path:.*?}')

class IncludeMeTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test(self):
        from papyrus_tilecache import includeme
        includeme(self.config)
        from papyrus_tilecache.views import _service
        from TileCache.Service import Service
        self.assertTrue(isinstance(_service, Service))

class MainTests(unittest.TestCase):
    def test(self):
        from papyrus_tilecache import main
        app = main({}, a='a')
        from pyramid.router import Router
        self.assertTrue(isinstance(app, Router))

class TileCacheTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_tilecache(self):
        from papyrus_tilecache.views import tilecache
        from pyramid.request import Request
        from papyrus_tilecache.views import load_tilecache_config

        curdir = os.path.dirname(os.path.abspath(__file__))
        cfgfile = os.path.join(curdir, 'tilecache.cfg')
        settings = {'tilecache.cfg': cfgfile}
        load_tilecache_config(settings)

        context = DummyContext()
        request = Request({})
        response = tilecache(context, request)
        from pyramid.response import Response
        self.assertTrue(isinstance(response, Response))

class DummyContext:
    pass
