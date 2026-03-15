"""
Copyright 2010 NaviSite, Inc.
"""

# A dummy SMTP listener base class. 
import smtpd

class DummySMTPD(smtpd.SMTPServer):
    def __init__(self, listen_addr, real_smtpserver):
        # listen_addr and real_smtpserver are tuples of (ipaddr, port)
        smtpd.SMTPServer.__init__(self, listen_addr, real_smtpserver)

        # Store header: func mappings and the order to perform them as a list
        # This way they are deterministic. The order callbacks are added matters.
        # The first matching handler is executed and the rest are not.
        self.callbacks = [] # [ (header, callback), ... ]
        
        # Function to call if message doesn't match any callback_map headers
        self.non_match_func = None

    # If email has a given header call they want the associated function called
    def add_callback(self, header, callback_func):
        self.callbacks.append( (header.lower(), callback_func) )
        
    # What function should we call for emails that dont match any headers
    def set_non_match_callback(self, callback_func):
        self.non_match_func = callback_func

    # A callback caller can use on non-match to print email to stdout
    def non_match_stdout(self, peer, mailfrom, rcpttos, data):
        print 'PEER: %s' % str(peer)        
        print '---------- MESSAGE FOLLOWS ----------'
        
        in_headers = True        
        for line in data.split('\n'):
            if in_headers:
                if line:
                    print 'HEADER: %s' % line
                else:
                    in_headers = False
            print 'BODY: %s' % line
        print '------------ END MESSAGE ------------'

    # A callback the caller can use to forward the email to the real_smtpserver
    def non_match_forward(self, peer, mailfrom, rcpttos, data):
        #######################################################
        # Code copied from smtpd.py module Proxy class
        #######################################################        
        def deliver(mailfrom, rcpttos, data):
            import smtplib
            import socket
            refused = {}
            try:
                s = smtplib.SMTP()
                s.connect(self._remoteaddr[0], self._remoteaddr[1])
                try:
                    refused = s.sendmail(mailfrom, rcpttos, data)
                finally:
                    s.quit()
            except smtplib.SMTPRecipientsRefused, e:
                print >>sys.stderr, 'SMTP server refused email'
                refused = e.recipients
            except (socket.error, smtplib.SMTPException), e:
                print >>sys.stderr, 'SMTP refused ALL emails'
                # All recipients were refused.  If the exception had an associated
                # error code, use it.  Otherwise,fake it with a non-triggering
                # exception code.
                errcode = getattr(e, 'smtp_code', -1)
                errmsg = getattr(e, 'smtp_error', 'ignore')
                for r in rcpttos:
                    refused[r] = (errcode, errmsg)
            return refused

        # Look for the last header
        lines = data.split('\n')
        i = 0
        for line in lines:
            if not line:
                break
            i += 1
        lines.insert(i, 'X-Peer: %s' % peer[0])
        data = '\n'.join(lines)
        refused = deliver(mailfrom, rcpttos, data)
        # XXX: what to do with refused?

        # Return OK by returning "None"
        return None
    
    def process_message(self, peer, mailfrom, rcpttos, data):
        # Check headers against callback map. If we find a match hand off to callback
        # otherwise hand to the non_match_callback if any, otherwise toss on floor

        # Need to parse out all the mail headers before we process callbacks.
        headers = {}
        
        for line in data.split('\n'):
            # Headers are first in the file. They end at first empty line
            if line:
                # See if one of the headers matches an entry in callbacks
                header_fields = line.split(':')
                header = header_fields[0].lower()
                headers[header] = 1
            else:
                # Reached body
                break

        # Found some matching headers
        for header, callback in self.callbacks:
            if header in headers:
                # Found a match. hand the entire message to the callback and abort by returning
                # whatever the callback returns
                return callback(peer, mailfrom, rcpttos, data)

        # No matching headers. if provided a non-matching callback, call it and return
        # to the user whatever status it gives back to us.
        if self.non_match_func:
            return self.non_match_func(peer, mailfrom, rcpttos, data)
        else:
            # None provide. return "None" to indicate success
            return None
        

# Example usage:
# NOTE: The following code would need to be run as root to bind port 25 on localhost
# import dummy_smtpd
# import asyncore

# def my_callback(peer, mailfrom, rcpttos, data):
#     # do something here with the message
#     print '----------------------------'
#     print 'In My callback!!!!'
#     print str(data)
#     print
#     return None

# def non_match(peer, mailfrom, rcpttos, data):
#     # do something with non-matching emails here
#     print '================================'
#     print 'Got email with non-matching header: %s' % str(data)
#     print
#     return None

# dd =  dummy_smtpd.DummySMTPD(('127.0.0.1', 25), ('10.208.9.166', 25))
# dd.add_callback('X-Einvoice', my_callback)
# dd.set_non_match_callback(non_match)
#
# you can also use one of the built in non_match callbacks:
##dd.set_non_match_callback(dd.non_match_stdout)  # print messages to stdout
##dd.set_non_match_callback(dd.non_match_forward) # forward the email to the real mail server for delivery

# try:
#     asyncore.loop()
# except KeyboardInterrupt:
#         pass
