

class CloudFoundryService(object):

    meta = {}
    properties = {}
    provider = ''
    tier = ''
    service_type = ''
    vendor = ''
    version = ''

    def __init__(self, name, meta=None, properties=None, provider=None, tier=None, type=None, vendor=None,
                 version=None, interface=None):
        self._name = name
        self.meta = meta
        self.properties = properties
        self.provider = provider
        self.tier = tier
        self.service_type = type
        self.vendor = vendor
        self.version = version
        self.interface = interface

    @property
    def name(self):
        return self._name

    @staticmethod
    def from_dict(dict, interface=None):
        return CloudFoundryService(interface=interface, **dict)

    def delete(self):
        if not self.interface:
            raise Exception("Tried to delete service %s without providing an interface for doing so" % self.name)
        self.interface.delete_service(self.name)
