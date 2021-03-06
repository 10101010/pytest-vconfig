import consul

from urllib.parse import urlparse

import pytest
from vyper import v


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """
    Performs loading of json-formatted config and extracts vyper object to pytest context variable 'config'

    The config can be loaded from consul server if consul-url, consul-token, consul-path provided,
        seeks for config at {consul-url/consul-path/env}

    If consul-url is not specified, reads config files stored at {test-rootdir/config/env.json}

    """
    config_type = 'json'
    env = config.option.env

    v.set_config_type(config_type)

    is_remote = bool(config.option.consul_url)

    if is_remote:
        c = urlparse(config.option.consul_url)

        token = config.option.consul_token
        client = consul.Consul(host=c.hostname, port=c.port, scheme=c.scheme, token=token)
        path = f'{config.option.consul_path}/{env}'
        provider = 'consul'

        v.add_remote_provider(provider, client, path)
        v.read_remote_config()
    else:
        path = f'{config.rootdir.strpath}/config'

        v.set_config_name(config.option.env)
        v.add_config_path(path)

        try:
            v.read_in_config()
        except FileNotFoundError:
            raise FileNotFoundError(f'File not found: {path}/{env}.{config_type}')

    config.v = v


def pytest_addoption(parser):
    group = parser.getgroup('vconfig')
    group.addoption(
        '--consul-url',
        action='store',
        dest='consul_url',
        default=None,
        help='Set the url to your consul server'
    )
    group.addoption(
        '--consul-token',
        action='store',
        dest='consul_token',
        default=None,
        help='Consul token used to access consul server'
    )
    group.addoption(
        '--consul-path',
        action='store',
        dest='consul_path',
        default=None,
        help='Path to directory with configuration file'
    )
    group.addoption(
        '--env',
        action='store',
        dest='env',
        default='dev',
        help='Environment to use config for'
    )
