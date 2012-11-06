
class CloudFoundryApp(object):
    environment_variables = []
    instances = 0
    meta = {}
    created = 0
    debug = None
    version = 0
    name = ""
    running_instances = 0
    services = []
    state = ""
    uris = []

    def __init__(self, name, env=None, instances=None, meta=None, created=None, debug=None, version=None, runningInstances=None, services=None, state=None, uris=None, staging=None, resources=None):
        self.name = name
        self.environment_variables = env
        self.instances = instances
        self.meta = meta
        self.created = created
        self.debug = debug
        self.version = version
        self.running_instances = runningInstances
        self.services = services
        self.state = state
        self.uris = uris

    @staticmethod
    def from_dict(dict):
        return CloudFoundryApp(**dict)