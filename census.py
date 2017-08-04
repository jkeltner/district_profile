import logging
import httplib2
import json
from api_keys import CENSUS_API_KEY

#   CHARTS
#   This is a list of all the charts we have in an array with section names.
#   First set of items is the section names
#   Each item under a section is an array with fourt items:
#   [Name, Description, Query Name, Annotations]
#   The Query Name must match to a query item below.
#   Annotations should be an array of String objects that should be displayed as 
#   annotations to the chart. This is usually due to shortening variable names.

census_charts = [
    ["Demographics" , [
        ["Age", "", "age", ["Please not that some bars are 5 year spans and others are 10 year spans."]],
        ["Ethnicity", "", "ethnicity", 
            ["(1) Includes American Indians and Alaskan Natives", 
             "(2) Includes Hawaiians and other Pacific Islanders"]],
        ["Eduation", "Education attaitment of individuals 25 years of age and older.", "education", []],
        ["School Enrollment", "Portion of population 3 yrs and older enrolled in school.", "school_enrollment", []],
        ["Health Insurance", "Portion of the civilian population by health insurance type", "health_insurance", []]
    ]],
    ["Economics" , [
        ["Employment", "Employment status of individuals 16 years and older.", "employment", []],
        ["Income", "", "income", []],
        ["Industry", "", "industry", 
            ["(1) Agriculture, forestry, fishing and hunting, and mining",
             "(2) Transportation and warehousing, and utilities",
             "(3) Finance and insurance, and real estate and rental and leasing",
             "(4) Professional, scientific, and management, and administrative and waste management services",
             "(5) Educational services, and health care and social assistance",
             "(6) Arts, entertainment, and recreation, and accommodation and food services"
             ]],
        ["Occuption", "", "occupation", [
            "(1) Management, business, science, and arts occupations",
            "(2) Natural resources, construction, and maintenance occupations"
        ]],
        ["Class of Worker", "", "class_of_worker",
            ["(1) In own not incorporated business"]],
        ["Home Value", "Value of owner-occupied housing units", "home_value" ,[]],
        ["Rent", "Rental cost of occupied units", "rent" ,[]],
        ["Rent peer Income", "Gross rent as a percentage of gross income", "rent_per_income", []],
        ["Housing Vacancy", "Rate of vacancy by top of property", "housing_vacancy", []]
    ]]
]

#   QUERIES
#   This is the list of all queries for the charts.
#   In each tuple, the first item is the label for the data point.
#   The second item is the Census Bureau API variable name for the data point.
#   URL to find variables: https://api.census.gov/data/2015/acs/acs1/profile/variables.html
# 
queries = {
    "age" : [
        ["Under 5"                  , "DP05_0004PE"],
        ["5 to 9"                   , "DP05_0005PE"],
        ["10 to 14"                 , "DP05_0006PE"],
        ["15 to 19"                 , "DP05_0007PE"],
        ["20 to 24"                 , "DP05_0008PE"],
        ["25 to 34"                 , "DP05_0009PE"],
        ["35 to 44"                 , "DP05_0010PE"],
        ["45 to 54"                 , "DP05_0011PE"],
        ["55 to 59"                 , "DP05_0012PE"],
        ["60 to 64"                 , "DP05_0013PE"],
        ["65 to 74"                 , "DP05_0014PE"],
        ["75 to 84"                 , "DP05_0015PE"],
        ["85+"                      , "DP05_0016PE"]
    ],
    "class_of_worker" : [
        ["Private"                  , "DP03_0047PE"],
        ["Government"               , "DP03_0048PE"],
        ["Self-employed (1)"          , "DP03_0049PE"],
        ["Unpaid family workers"    , "DP03_0050PE"]
    ],
    "education" : [
        ["No HS"                    , "DP02_0059PE"],
        ["Some HS"                  , "DP02_0060PE"],
        ["HS Grad or GED"           , "DP02_0061PE"],
        ["Some college"             , "DP02_0062PE"],
        ["Associate's Degree"       , "DP02_0063PE"],
        ["Bachelor's Degree"        , "DP02_0064PE"],
        ["Grad or Prof Degree"      , "DP02_0065PE"]
    ],
    "employment" : [
        ["Employed Civilian"        , "DP03_0004PE"],
        ["Employed Military"        , "DP03_0006PE"],
        ["Unemployed"               , "DP03_0005PE"],
        ["Not in Labor Force"       , "DP03_0007PE"]
    ],
    "ethnicity" : [    
        ["White"                     , "DP05_0032PE"],
        ["Hispanic"                  , "DP05_0067PE"],
        ["Black or AA"               , "DP05_0033PE"],
        ["Native American (1)"       , "DP05_0034PE"],
        ["Asian"                     , "DP05_0039PE"],
        ["Pacific Islander (2)"      , "DP05_0047PE"],
        ["Other"                     , "DP05_0052PE"],
        ["2+ Races "                 , "DP05_0030PE"]
    ], 
    "health_insurance" : [
        ["Private"                  , "DP03_0097PE"],
        ["Pulic"                    , "DP03_0098PE"],
        ["Uninsured"                , "DP03_0099PE"]
    ],
    "home_value" : [
        ["<$50K"                    , "DP04_0081PE"],
        ["$50-100K"                 , "DP04_0082PE"],
        ["$100-150K"                , "DP04_0083PE"],
        ["$150-200K"                , "DP04_0084PE"],
        ["$200-300K"                , "DP04_0085PE"],
        ["$300-500K"                , "DP04_0086PE"],
        ["$500K-1M"                 , "DP04_0087PE"],
        ["$1M+"                     , "DP04_0088PE"]
    ],
    "housing_vacancy" : [
        ["Howeowner"                , "DP04_0004E"],
        ["Rental"                   , "DP04_0005E"]
    ],
    "income" : [
        ["Under $10K"               , "DP03_0052PE"],
        ["$10-15K"                  , "DP03_0053PE"],
        ["$15-25K"                  , "DP03_0054PE"],
        ["$25-35K"                  , "DP03_0055PE"],
        ["$35-50K"                  , "DP03_0056PE"],
        ["$50-75K"                  , "DP03_0057PE"],
        ["$75-100K"                 , "DP03_0058PE"],
        ["$100-150K"                , "DP03_0059PE"],
        ["$150-200K"                , "DP03_0060PE"],
        ["$200K+"                   , "DP03_0061PE"]
    ],
    "industry" : [
        ["Agriculture (1)"          , "DP03_0033PE"],
        ["Construction"             , "DP03_0034PE"],
        ["Manufacturing"            , "DP03_0035PE"],
        ["Wholesale trade"          , "DP03_0036PE"],
        ["Retail trade"             , "DP03_0037PE"],
        ["Transportation (2)"       , "DP03_0038PE"],
        ["Information"              , "DP03_0039PE"],
        ["Finance + Real Estate (3)", "DP03_0040PE"],
        ["Management + Science (4)" , "DP03_0041PE"],
        ["Education and Health (5)" , "DP03_0042PE"],
        ["Arts + Entertainment (6)" , "DP03_0043PE"],
        ["Other services"           , "DP03_0044PE"],
        ["Public administration"    , "DP03_0045PE"]
    ],
    "occupation" : [
        ["Management (1)"               , "DP03_0027PE"],
        ["Service"                      , "DP03_0028PE"],
        ["Sales and Office"             , "DP03_0029PE"],
        ["Construction (2)"             , "DP03_0030PE"],
        ["Production (3)"   , "DP03_0031PE"]
    ],
    "rent" : [
        ["<$500"            , "DP04_0127PE"],
        ["$500-999"         , "DP04_0128PE"],
        ["$1K-1,499"        , "DP04_0129PE"],
        ["$1,500 - 2K"      , "DP04_0130PE"],
        ["$2K - 2,499"      , "DP04_0131PE"],
        ["$2,500 - 3K"      , "DP04_0132PE"],
        ["$3K+"             , "DP04_0133PE"]
    ],
    "rent_per_income" : [
        ["<15%"             , "DP04_0137PE"],
        ["15-19.9%"         , "DP04_0138PE"],
        ["20-24.9%"         , "DP04_0139PE"],
        ["25-29.9%"         , "DP04_0140PE"],
        ["30-34.9%"         , "DP04_0141PE"],
        ["35%+"             , "DP04_0142PE"]
    ],
    "school_enrollment" : [
        ["Preschool"                , "DP02_0053PE"],
        ["Kindergargten"            , "DP02_0054PE"],
        ["Grades 1-8"               , "DP02_0055PE"],
        ["High School"              , "DP02_0056PE"],
        ["College or Grad"          , "DP02_0057PE"]
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
    return "http://api.census.gov/data/2015/acs/acs1/profile?get=%s&for=%s&key=%s" % (variables, for_block, CENSUS_API_KEY)
