def pytest_addoption(parser):
    parser.addoption(
        "--sites-path",
        action="store",
        dest="sites_path",
        default="config",
        help="Frappe config file",
    )
    parser.addoption(
        "--test-site",
        action="store",
        dest="test_site",
        default=None,
        help="Specify the test site for running tests",
    )