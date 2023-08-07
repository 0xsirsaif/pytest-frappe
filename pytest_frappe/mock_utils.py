class FrappeMockedDB:
    def __init__(self, mocked_functions_dict):
        self.mocked_functions_dict = mocked_functions_dict

    def __getattr__(self, db_function_name):
        return self.mocked_functions_dict[db_function_name]
