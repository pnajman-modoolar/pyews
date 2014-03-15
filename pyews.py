#!/usr/bin/python
##
## Created : Wed Mar 05 11:28:41 IST 2014
##
## Copyright (C) 2014 Sriram Karra <karra.etc@gmail.com>
##
## This file is part of pyews
##
## pyews is free software: you can redistribute it and/or modify it under
## the terms of the GNU Affero General Public License as published by the
## Free Software Foundation, version 3 of the License
##
## pyews is distributed in the hope that it will be useful, but WITHOUT
## ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
## FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public
## License for more details.
##
## You should have a copy of the license in the doc/ directory of pyews.  If
## not, see <http://www.gnu.org/licenses/>.

import logging
import utils
from   autodiscover import EWSAutoDiscover, ExchangeAutoDiscoverError

#from   httplib import HTTPException
#from   ntlm    import HTTPNtlmAuthHandler

USER = u'skarra@asynk.onmicrosoft.com'
PWD  = u'tsYWpw8m'

##
## Note: There is a feeeble attemp to mimick the names of classes and methods
## used in the EWS Managed Services API. However the similiarities are merely
## skin-deep, if anything at all.
##

class InvalidUserEmail(Exception):
    pass

class WebCredentials:
    def __init__ (self, user, pwd):
        self.user = user
        self.pwd  = pwd

class ExchangeService:
    def __init__ (self):
        self.ews_ad = None
        self.credentials = None

    def AutoDiscoverUrl (self):
        """blame the weird naming on the EWS MS APi."""

        creds = self.credentials
        self.ews_ad = EWSAutoDiscover(creds.user, creds.pwd)
        self.ews_url = self.ews_ad.discover()

    @property
    def credentials (self):
        return self._credentials

    @credentials.setter
    def credentials (self, c):
        self._credentials = c

    @property
    def ews_url (self):
        return self._ews_url

    @ews_url.setter
    def ews_url (self, url):
        self._ews_url = url

def main ():
    logging.getLogger().setLevel(logging.DEBUG)

    creds = WebCredentials(USER, PWD)
    ews = ExchangeService()
    ews.credentials = creds

    try:
        ews.AutoDiscoverUrl()
    except ExchangeAutoDiscoverError as e:
        logging.error('ExchangeAutoDiscoverError: %s', e)

if __name__ == "__main__":
    main()
