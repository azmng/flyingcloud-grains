#!/usr/bin/env python
def _my_custom_grain():
    my_grain = {
    	'server_name': 'webhost.domain.com',
    	'log_prefix': 'webhost_domain_com',
    	'backend_server': 'apphost.domain.com'
    }
    return my_grain

def main():
    # initialize a grains dictionary
    grains = {}
    grains['my_grains'] = _my_custom_grain()
    return grains
