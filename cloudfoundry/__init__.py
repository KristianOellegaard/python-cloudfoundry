import json
import urllib
from urlparse import urljoin
import requests
from cloudfoundry.apps import CloudFoundryApp
from cloudfoundry.services import CloudFoundryService

class CloudFoundryException(Exception):
    pass

class CloudFoundryInterface(object):
    def __init__(self, target, username=None, password=None):
        self.target = target
        self.username = username
        self.password = password
        self.token = None

    def auth_args(self, authentication_required):
        if not authentication_required and not self.token:
            return {}
        elif not self.token:
            raise CloudFoundryException("Please login before using this function")
        return {'headers': {'Authorization': self.token}}

    def _request(self, url, request_type=requests.get, authentication_required=True, data=None):
        if data:
            data = json.dumps(data)
        return request_type(urljoin(self.target, url), data=data, **self.auth_args(authentication_required))

    def _get_json_or_exception(self, *args, **kwargs):
        request = self._request(*args, **kwargs)
        if request.status_code == 200:
            return request.json
        else:
            raise CloudFoundryException("HTTP %s - %s" % (request.status_code, request.text))

    def _get_true_or_exception(self, *args, **kwargs):
        request = self._request(*args, **kwargs)
        if request.status_code == 200:
            return True
        else:
            raise CloudFoundryException(request.text)

    def login(self):
        self.token = self._get_json_or_exception(
            "users/%s/tokens" % urllib.quote_plus(self.username),
            request_type=requests.post,
            authentication_required=False,
            data={'password': self.password}
        )['token']
        return True

    def get_apps(self):
        return [CloudFoundryApp.from_dict(app) for app in self._get_json_or_exception("apps/")]

    def get_app(self, name):
        return CloudFoundryApp.from_dict(self._get_json_or_exception("apps/%s" % name))

    def get_app_crashes(self, name):
        return self._get_json_or_exception("apps/%s/crashes" % name)

    def get_app_instances(self, name):
        return self._get_json_or_exception("apps/%s/instances" % name)

    def get_app_stats(self, name):
        return self._get_json_or_exception("apps/%s/stats" % name)

    def delete_app(self, name):
        return self._get_true_or_exception("apps/%s" % name, request_type=requests.delete)

    def get_services(self):
        return [CloudFoundryService.from_dict(service) for service in self._get_json_or_exception("services/")]

    def get_service(self, name):
        return CloudFoundryService.from_dict(self._get_json_or_exception("services/%s" % name))

    def delete_service(self, name):
        return self._get_true_or_exception("services/%s" % name, request_type=requests.delete)

