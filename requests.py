# [START imports]

import os
import json
import webapp2
import logging
from census import getCensusData
from propublica import getProPublicaData

class CensusDataRequestHandler(webapp2.RequestHandler):
    def get(self):
        state = self.request.get('state')
        district = self.request.get('district')
        chart_name = self.request.get('chart_name')
        resp = getCensusData(chart_name, state, district)
        self.response.write(json.dumps(resp))

class ProPublicaDataRequestHandler(webapp2.RequestHandler):
    def get(self):
        state = self.request.get('state')
        district = self.request.get('district')

app = webapp2.WSGIApplication([
    ('/getdata/census', CensusDataRequestHandler),
    ('/getdata/propublica',ProPublicaDataRequestHandler)
], debug=True)