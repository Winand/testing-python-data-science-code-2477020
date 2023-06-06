import pytest
import yaml

@pytest.fixture(scope="session")
def cases():
    with open("Ch02/02_06/split_cases.yml") as f:
        return yaml.safe_load(f)
