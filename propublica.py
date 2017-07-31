import httplib2
import json
from api_keys import PROPUBLICA_API_KEY

# This file defines the methods to get data from the ProPublica API on members of congress.
# https://projects.propublica.org/api-docs/congress-api/

# gets 
def getProPublicaData(state, district):
    conn = httplib2.Http(disable_ssl_certificate_validation=True)
    resp, content = conn.request()
