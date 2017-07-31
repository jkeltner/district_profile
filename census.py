import logging
import httplib2
import json
from api_keys import CENSUS_API_KEY

#     QUERIES
#     This is the list of all queries for the charts.
#     In each tuple, the first item is the label for the data point.
#     The second item is the Census Bureau API variable name for the data point.
#     URL to find variables: https://api.census.gov/data/2015/acs1/subject/variables.html
# 
queries = {
    "age" : [
        ["Under 5"   , "S0101_C01_002E"],
        ["5 to 9"    , "S0101_C01_003E"],
        ["10 to 14"  , "S0101_C01_004E"],
        ["15 to 19"  , "S0101_C01_005E"],
        ["20 to 24"  , "S0101_C01_006E"],
        ["25 to 29"  , "S0101_C01_007E"],
        ["30 to 34"  , "S0101_C01_008E"],
        ["35 to 39"  , "S0101_C01_009E"],
        ["40 to 44"  , "S0101_C01_010E"],
        ["45 to 49"  , "S0101_C01_011E"],
        ["50 to 54"  , "S0101_C01_012E"],
        ["55 to 59"  , "S0101_C01_013E"],
        ["60 to 64"  , "S0101_C01_014E"],
        ["65 to 69"  , "S0101_C01_015E"],
        ["70 to 74"  , "S0101_C01_016E"],
        ["75 to 79"  , "S0101_C01_017E"],
        ["80 to 84"  , "S0101_C01_018E"],
        ["85+"       , "S0101_C01_019E"]
    ],
    "ethnicity" : [    
        ["White"                    , "S0501_C01_015E"],
        ["Hispanic"                  , "S0501_C01_022E"],
        ["Black or AA"               , "S0501_C01_016E"],
        ["Native American"           , "S0501_C01_017E"],
        ["Asian"                     , "S0501_C01_018E"],
        ["Pacific Islander"          , "S0501_C01_019E"],
        ["Other"                     , "S0501_C01_020E"],
        ["2+ Races "                 , "S0501_C01_021E"]
    ], 
    "income" : [
        ["Under $10K"   , "S1901_C01_002E"],
        ["$10-15K"      , "S1901_C01_003E"],
        ["$15-25K"      , "S1901_C01_004E"],
        ["$25-35K"      , "S1901_C01_005E"],
        ["$35-50K"      , "S1901_C01_006E"],
        ["$50-75K"      , "S1901_C01_007E"],
        ["$75-100K"     , "S1901_C01_008E"],
        ["$100-150K"    , "S1901_C01_009E"],
        ["$150-200K"    , "S1901_C01_010E"],
        ["$200K+"       , "S1901_C01_011E"]
    ]
}

# Function to iterate through all the charts
def getCensusData(chart_name, state, district):
    labels, district_data, state_data, fed_data = getChartData(queries[chart_name], state, district)
    resp = {
        "labels" : labels,
        "district_data" : district_data,
        "state_data" : state_data,
        "fed_data" : fed_data
    }
    return resp

# Function to pull the labels/data for a particular chart.
# Should be sent a dictionary of labels and the associated variable names.
# These dictionaries should all the be in the charts variable above.
def getChartData(query, state, district):
    labels = []
    variables = ""
    for item in query:
        labels.append(item[0])
        if (variables != ""):
            variables += ","
        variables += item[1]
    conn = httplib2.Http(disable_ssl_certificate_validation=True)
    resp, content = conn.request(getURL(variables, state, district))
    district_data = json.loads(content)[1][:len(labels)]
    resp, content = conn.request(getURL(variables, state))
    state_data = json.loads(content)[1][:len(labels)]
    resp, content = conn.request(getURL(variables))
    fed_data = json.loads(content)[1][:len(labels)]
    return labels, district_data, state_data, fed_data

# Simple function that builds our Census API URLs
def getURL(variables, state=None, district=None):
    if (state and district): for_block = "congressional+district:%s&in=state:%s" % (district, state)
    elif (state) : for_block = "state:%s" % state
    else : for_block = "us:*" 
    return "http://api.census.gov/data/2015/acs1/subject?get=%s&for=%s&key=%s" % (variables, for_block, CENSUS_API_KEY)