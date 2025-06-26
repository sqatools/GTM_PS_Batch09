import pytest
from api.ready_api.ready_api_class import ReadyAPI

class TestReadyAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.r_api = ReadyAPI()

    def test_get_object_and_verify(self):
        res, st_code = self.r_api.get_all_objects_details()
        assert len(res) == 13
        assert st_code == 200

