# [START imports]

import os
import jinja2
import webapp2
import json
import logging
from census import getCensusData, census_charts

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class DistrictProfileHandler(webapp2.RequestHandler):
    def get(self):
        state = self.request.get('state')
        district = self.request.get('district')
        if ((state == '') or  (district == '')) : # defaults to Jeff's home state and district it not provided
            state = "CA"         
            district = "27"
        template_values = {
            'state' : state,
            'district' : district,
            'census_charts' : census_charts
        }
        template = JINJA_ENVIRONMENT.get_template('district.html')
        self.response.write(template.render(template_values))

class CensusDataRequestHandler(webapp2.RequestHandler):
    def get(self):
        state = self.request.get('state')
        district = self.request.get('district')
        chart_name = self.request.get('chart_name')
        resp = getCensusData(chart_name, state, district)
        self.response.write(json.dumps(resp))

app = webapp2.WSGIApplication([
    ('/', DistrictProfileHandler),
    ('/getdata/census', CensusDataRequestHandler),
], debug=True)
