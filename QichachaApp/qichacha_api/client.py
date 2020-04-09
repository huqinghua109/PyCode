from .base import QichachaRequestImpl, call_sync


class RequestClient(object):
    """
    
    """
    def __init__(self, appKey, secret_key, server_url="http://api.qichacha.com"):
        self.appKey = appKey
        self.secret_key = secret_key
        self.server_url = server_url

        self.request_impl = QichachaRequestImpl(self.appKey, self.secret_key, self.server_url)

    def get_details_by_name(self, companyName):
        request = self.request_impl.get_details_by_name(companyName)
        return call_sync(request)