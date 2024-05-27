import pytest
from selenium_module import SeleniumHelper

@pytest.fixture(scope="session")
def selenium_helper():
    helper = SeleniumHelper(config_path='config.yaml')
    helper.setup_driver()
    yield helper
    helper.teardown_driver()

@pytest.fixture
def element_properties():
    return {
        "search_box": {"by": "name", "value": "q"},
        "search_button": {"by": "name", "value": "btnK"}
    }