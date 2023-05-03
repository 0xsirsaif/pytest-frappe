import pathlib
import frappe
import pytest


def get_site_configs(sites_path, site=None):
    """Returns the sites path and the current site"""
    sites_path = pathlib.Path(sites_path)
    if site is None:
        current_site_file = sites_path / "currentsite.txt"
        with open(current_site_file, "r") as f:
            site_to_use = f.readline().strip()
    else:
        site_to_use = site
    return str(sites_path), site_to_use


@pytest.fixture(scope="session")
def db_instance(request):
    """Returns a database instance."""
    sites_path = request.config.getoption("--sites-path")
    site = request.config.getoption("--site")

    if not sites_path:
        raise Exception("Please provide the sites path")

    sites_path, current_site = get_site_configs(sites_path, site)

    frappe.init(site=current_site, sites_path=sites_path)
    frappe.connect()

    # TODO: should we mock the commit method?
    # mock_commit = MagicMock()
    # frappe.db.commit = mock_commit

    yield frappe.db
    frappe.destroy()


@pytest.fixture()
def db_transaction(db_instance):
    # create a new transaction.
    db_instance.begin()
    yield db_instance
    db_instance.rollback()
