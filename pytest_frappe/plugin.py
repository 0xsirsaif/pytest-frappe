def pytest_addoption(parser):
    parser.addoption('--sites-path', action='store', dest='frappe_config',default='config', help='Frappe config file')
