# pytest-vconfig
Pytest plugin-wrapper of vyper-config lib

Usage:
1. Install this plugin as requirement 
```
pip install -e git+https://github.com/10101010/pytest-vconfig#egg=pytest-vconfig
```
2. Provide consul-url, consul-token, consul-path, env ('dev' is default) arguments to pytest execution command.
```
pytest . --consul-url={CONSUL_URL} --consul-token={CONSUL_TOKEN} --consul-path={CONSUL_PATH} --env={ENV}
```
3. Define pytest_configure hook in your conftest.py
```
def pytest_configure(config):
    client.url = config.v.get('client.url')
```
4. Enjoy
