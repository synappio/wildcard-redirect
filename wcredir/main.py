import os
import re
import string

from pyramid.config import Configurator
import pyramid.httpexceptions as exc
from formencode import variabledecode


def app_factory(global_config, **local_settings):
    settings = dict(global_config)
    settings.update(local_settings)
    update_settings_from_environ(settings)
    settings = variabledecode.variable_decode(settings)
    settings['patterns'] = compile_patterns(settings['patterns'])
    config = Configurator(settings=settings)
    config.add_view(root)
    return config.make_wsgi_app()


def root(request):
    patterns = request.registry.settings['patterns']
    host = request.host
    for regex, exp in patterns:
        mo = regex.match(host)
        if mo is None:
            continue
        new_url = mo.expand(exp)
        raise exc.HTTPFound(location=new_url)
    raise exc.HTTPNotFound()


def compile_patterns(raw_patterns):
    result = []
    for x in raw_patterns:
        re_pat = re.compile(x['pat'])
        result.append((re_pat, x['sub']))
    return result


def update_settings_from_environ(settings):
    for k, v in settings.items():
        if not isinstance(v, basestring):
            continue
        t = string.Template(v)
        v1 = t.safe_substitute(os.environ)
        settings[k] = v1
