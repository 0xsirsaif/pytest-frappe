import pathlib
import frappe
import pytest


def get_site_configs(sites_path_as_str):
    """Returns the sites path and the current site"""
    sites_path = pathlib.Path(sites_path_as_str)
    current_site = sites_path / "currentsite.txt"
    with open(current_site, "r") as f:
        current_site = f.readline().strip()
    return str(sites_path), current_site


@pytest.fixture(scope='session')
def db_instance(request):
    """Returns a database instance."""
    sites_path, current_site = get_site_configs(request.config.getoption("--sites-path"))

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
