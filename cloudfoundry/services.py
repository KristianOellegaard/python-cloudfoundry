

class CloudFoundryService(object):

    meta = {}
    name = ''
    properties = {}
    provider = ''
    tier = ''
    service_type = ''
    vendor = ''
    version = ''

    def __init__(self, name, meta=None, properties=None, provider=None, tier=None, type=None, vendor=None, version=None):
        self.name = name
        self.meta = meta
        self.properties = properties
        self.provider = provider
        self.tier = tier
        self.service_type = type
        self.vendor = vendor
        self.version = version

    @staticmethod
    def from_dict(dict):
        return CloudFoundryService(**dict)
