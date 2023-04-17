# pytest-frappe

`pytest-frappe` is a set of pytest fixtures for testing Frappe applications. It provides two fixtures: `db_instance` and `db_transaction`, which can be used to create and manage database connections.

## Installation

You can install `pytest-frappe` via pip:

```bash
pip install pytest-frappe
```


## Usage

To use the fixtures provided by `pytest-frappe`

```python
def test_foo(db_transaction):
    # use the db_instance fixture to interact with the database
    pass
```


`pytest-frappe` also provides a command line option, `--sites-path`, which can be used to specify the directory where your Frappe sites are stored. This option is required to initialize the `db_instance` fixture.

Here's an example of how you can use the `--sites-path` option:

```bash
pytest --sites-path=/path/to/sites/directory
```


## Available fixtures

### `db_instance`

The `db_instance` fixture provides a database connection to a Frappe application. It is created at the beginning of the test session and destroyed at the end of the session. This fixture is used to perform database operations.

### `db_transaction`

The `db_transaction` fixture is a database transaction context manager. It creates a new transaction at the beginning of each test function and rolls back the transaction at the end of the test function. This fixture is used to perform database operations within a transaction.

## License

`pytest-frappe` is licensed under the MIT License. See LICENSE for more information.
