import os
import unittest

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

    # _makeOne, _getViewCallable, and _getRouteRequestIface come from Pyramid
    # pyramid/tests/test_config.py:ConfiguratorTests

    def _makeOne(self, *arg, **kw):
        from pyramid.config import Configurator
        return Configurator(*arg, **kw)

    def _getViewCallable(self, config, ctx_iface=None, request_iface=None,
                         name='', exception_view=False):
        from zope.interface import Interface
        from pyramid.interfaces import IRequest
        from pyramid.interfaces import IView
        from pyramid.interfaces import IViewClassifier
        from pyramid.interfaces import IExceptionViewClassifier
        if exception_view:
            classifier = IExceptionViewClassifier
        else:
            classifier = IViewClassifier
        if ctx_iface is None:
            ctx_iface = Interface
        if request_iface is None:
            request_iface = IRequest
        return config.registry.adapters.lookup(
            (classifier, request_iface, ctx_iface), IView, name=name,
            default=None)

    def _getRouteRequestIface(self, config, name):
        from pyramid.interfaces import IRouteRequest
        iface = config.registry.getUtility(IRouteRequest, name)
        return iface

    def test(self):
        from pyramid.interfaces import IRoutesMapper
        from papyrus_tilecache import add_route
        from papyrus_tilecache.views import tilecache
        config = self._makeOne(autocommit=True)
        add_route(config)
        mapper = config.registry.getUtility(IRoutesMapper)
        routes = mapper.get_routes()
        self.assertEqual(len(routes), 1)
        self.assertEqual(routes[0].name, 'tilecache')
        self.assertEqual(routes[0].pattern, '/tilecache{path:.*?}')
        request_iface = self._getRouteRequestIface(config, 'tilecache')
        self.assertNotEqual(request_iface, None)
        wrapper = self._getViewCallable(config, request_iface=request_iface)
        self.assertEqual(wrapper, tilecache)

from pyramid import testing

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
