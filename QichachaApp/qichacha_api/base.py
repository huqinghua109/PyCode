import requests
import json
from .utils import create_signature, get_current_timestamp
from .urlparamsbuilder import UrlParamsBuilder

class RestApiRequest(object):
    def __init__(self):
        self.method = ""
        self.url = ""
        self.host = ""
        self.post_body = ""
        self.header = dict()
        self.json_parser = None
        # self.header.update({"client_SDK_Version": "binance_futures-1.0.1-py3.7"})

class QichachaRequestImpl(object):
    def __init__(self, api_key, secret_key, server_url="http://api.qichacha.com"):
        self.__api_key = api_key
        self.__secret_key = secret_key
        self.__server_url = server_url

    def _create_request_by_get(self, url, builder):
        request = RestApiRequest()
        request.method = "GET"
        request.host = self.__server_url
        # request.header.update({'Content-Type': 'application/json'})
        request.url = url + "?" + builder.build_url()
        return request

    def __create_request_by_get_with_signature(self, url, builder):
        request = RestApiRequest()
        request.method = "GET"
        request.host = self.__server_url
        timestamp_str = str(get_current_timestamp())
        request.header.update({"Timespan": timestamp_str})
        request.header.update({"Token": create_signature(self.__api_key, self.__secret_key, timestamp_str)})
        request.url = url + "?" + builder.build_url()
        return request
    
    def get_details_by_name(self, name):
        builder = UrlParamsBuilder()
        builder.put_url("key", self.__api_key)
        builder.put_url("keyword", name)

        request = self.__create_request_by_get_with_signature("/ECIV4/GetDetailsByName", builder)

        def parse(json_wrapper):
            result = json.loads(json_wrapper)
            return result

        request.json_parser = parse
        return request

    def Search_by_keyword(self, keyword, **kwargs):
        builder = UrlParamsBuilder()
        builder.put_url("key", self.__api_key)
        builder.put_url("keyword", keyword)
        if "provinceCode" in kwargs:
            builder.put_url("provinceCode", kwargs['provinceCode'])
        if "cityCode" in kwargs:
            builder.put_url("cityCode", kwargs['cityCode'])

        request = self.__create_request_by_get_with_signature("/ECIV4/Search", builder)

        def parse(json_wrapper):
            result = json.loads(json_wrapper)
            return result

        request.json_parser = parse
        return request

def call_sync(request):
    if request.method == "GET":
        response = requests.get(request.host + request.url, headers=request.header)
        print(response.text)
        return request.json_parser(response)
