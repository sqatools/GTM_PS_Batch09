from base.api_base import APIBase
from .ready_api_data import  *

class ReadyAPI(APIBase):

    def get_all_objects_details(self):
        response, st_code = self.get_method(url=ready_api_url)
        return response, st_code
