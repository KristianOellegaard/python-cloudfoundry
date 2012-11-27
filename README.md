# Python-Cloudfoundry

Sample usage:
```python
from cloudfoundry import CloudFoundryInterface

cfi = CloudFoundryInterface("api.vcap.me", "username", "password")
cfi.login()

cfi.delete_app('demo')
cfi.delte_service('demo')
```
or store token locally:
```python
from cloudfoundry import CloudFoundryInterface

cfi = CloudFoundryInterface("api.vcap.me", "username", "password", store_token=True)
cfi.login()

cfi.delete_app('demo')
cfi.delte_service('demo')
```
