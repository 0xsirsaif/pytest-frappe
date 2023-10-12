def pytest_addoption(parser):
    parser.addoption(
        "--sites-path",
        action="store",
        dest="sites_path",
        default="config",
        help="Frappe config file",
    )
    parser.addoption(
        "--site",
        action="store",
        dest="site",
        default=None,
        help="Frappe site",
    )