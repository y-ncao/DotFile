#!/usr/bin/env python
"""
Copyright 2010 NaviSite, Inc.
"""
# MUST be run as root

import sys
import dummy_smtpd
import asyncore

def my_non_match(peer, mailfrom, rcpttos, data):
    # do something here with the message
    print '----------------------------'
    print 'In My callback!!!!'
    print str(data)
    print
    return None

dd =  dummy_smtpd.DummySMTPD(('127.0.0.1', 25), ('10.208.9.166', 25))
#dd.add_callback('X-Einvoice', my_callback)
#dd.set_non_match_callback(dd.non_match_stdout)
dd.set_non_match_callback(my_non_match)

try:
    asyncore.loop()
except KeyboardInterrupt:
    pass
