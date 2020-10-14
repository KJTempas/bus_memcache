# Python cache with Memcached


1. Install Memcached. Macs install with homebrew, Windows install 

https://memcached.org/

2. Install Python client for memcached https://pymemcache.readthedocs.io/en/latest/getting_started.html

3. Run memcached, leave it running while you run your code 

4. In code, connect to memcached client

5. Add data to cache. Each piece of data needs a unique identifier. See pymemcached docs

References: https://realpython.com/python-memcache-efficient-caching/
