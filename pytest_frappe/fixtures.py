import pathlib
import frappe
import pytest


def get_current_site(site_config_path: pathlib.Path, test_site=None) -> str:
    # Check if frappe.local.site is available
    if hasattr(frappe.local, 'site'):
        current_site = frappe.local.site
    else:
        current_site = None

    # Check if current_site is available in currentsite.txt
    if not current_site:
        current_site_file: pathlib.Path = site_config_path / "currentsite.txt"
        try:
            with open(current_site_file, "r") as f:
                current_site = f.readline().strip()
        except FileNotFoundError:
            current_site = None

    # If test_site is provided, use it as the current site
    if not current_site and test_site:
        current_site = test_site

    return current_site


def select_test_site(request: pytest.FixtureRequest) -> str:
    test_site: str = request.config.getoption("--test-site")

    if test_site:
        return test_site
    else:
        raise Exception("Please specify a test site using the --test-site option")


def is_testing_allowed(test_site: str) -> bool:
    site_config: dict = frappe.get_conf(site=test_site)
    allow_tests: str = site_config.get("allow_tests", "0")
    return allow_tests and allow_tests.lower() not in ["0", "false", "no"]


@pytest.fixture(scope="session")
def db_instance(request: pytest.FixtureRequest):
    sites_path = request.config.getoption("--sites-path")
    site_config_path = pathlib.Path(sites_path)

    if not site_config_path:
        raise Exception("Please provide the sites path")

    current_site = get_current_site(site_config_path)
    selected_test_site = select_test_site(request)
    if current_site != selected_test_site:
        raise Exception("Selected test site does not match the current site")

    if not is_testing_allowed(selected_test_site):
        raise Exception("Testing is not allowed for the selected test site")

    frappe.init(site=selected_test_site, sites_path=str(site_config_path))
    frappe.connect()

    yield frappe.db
    frappe.destroy()


@pytest.fixture()
def db_transaction(db_instance):
    # create a new transaction.
    db_instance.begin()
    yield db_instance
    db_instance.rollback()
