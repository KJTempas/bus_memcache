import time 
from datetime import datetime 
import json
import sys
from pymemcache.client.base import Client
from pymemcache import serde


# Connect to memcached - make sure memcached is running 
# Uses pickle to store objects https://docs.python.org/3/library/pickle.html

memcache_client = Client('localhost', serde=serde.pickle_serde) 


def add(cachable):
    memcache_client.set(cachable.identifier, cachable, expire=60)  # 60 seconds


def fetch(identifier, cls):
    cached_object = memcache_client.get(identifier)
    return cached_object


