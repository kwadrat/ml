#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import urllib2

declared_browser = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0'

def replace_user_agent(opener):
    debug_substitution = 0
    the_tag = 'User-Agent'
    upper_tag = the_tag.upper()
    header_count = len(opener.addheaders)
    for i in range(header_count):
        if opener.addheaders[i][0].upper() == upper_tag:
            if debug_substitution:
                print 'Original:', opener.addheaders[i]
            opener.addheaders[i] = (the_tag, declared_browser)
            if debug_substitution:
                print 'Replaced:', opener.addheaders[i]

def save_to_file(file_name, data, verbose=0):
    open(file_name, 'wb').write(data)
    if verbose:
        print 'Written %(data)d bytes to %(file_name)s' % dict(
            data=len(data),
            file_name=file_name,
            )

def get_http_page(dst_address):
    opener = urllib2.build_opener()
    replace_user_agent(opener)
    url_fd = opener.open(dst_address)
    html_data = url_fd.read()
    url_fd.close()
    return html_data

def save_page_to_file(dst_address, file_name):
    html_data = get_http_page(dst_address)
    save_to_file(file_name, html_data, verbose=1)
