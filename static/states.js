var states = {
  "AL" : {
    "name": "Alabama",
    "FIPS": "01",
    "districts": 7
  },
  "AK" : {
    "name": "Alaska",
    "FIPS": "02",
    "districts": 1
  },
  "AZ" : {
    "name": "Arizona",
    "FIPS": "04",
    "districts": 9
  },
  "AR" : {
    "name": "Arkansas",
    "FIPS": "05",
    "districts": 4
  },
  "CA" : {
    "name": "California",
    "FIPS": "06",
    "districts": 53
  },
  "CO" : {
    "name": "Colorado",
    "FIPS": "08",
    "districts": 7
  },
  "CT" : {
    "name": "Connecticut",
    "FIPS": "09",
    "districts": 5
  },
  "DE" : {
    "name": "Delaware",
    "FIPS": "10",
    "districts": 1
  },
  "DC" : {
    "name": "District of Columbia",
    "FIPS": "11",
    "districts": 1
  },
  "FL" : {
    "name": "Florida",
    "FIPS": "12",
    "districts": 27
  },
  "GA" : {
    "name" : "Georgia",
    "FIPS" : "13",
    "districts": 14
  },
  "HI" : {
    "name" : "Hawaii",
    "FIPS" : "15",
    "districts": 2
  },
  "ID" : {
    "name" : "Idaho",
    "FIPS" : "16",
    "districts": 2
  },
  "IL" : {
    "name" : "Illinois",
    "FIPS" : "17",
    "districts": 18
  },
  "IN" : {
    "name" : "Indiana",
    "FIPS" : "18",
    "districts": 9
  },
  "IA" : {
    "name" : "Iowa",
    "FIPS" : "19",
    "districts": 4
  },
  "KS" : {
    "name" : "Kansas",
    "FIPS" : "20",
    "districts": 4
  },
  "KY" : {
    "name" : "Kentucky",
    "FIPS" : "21",
    "districts": 6
  },
  "LA" : {
    "name" : "Louisiana",
    "FIPS" : "22",
    "districts": 6
  },
  "ME" : {
    "name" : "Maine",
    "FIPS" : "23",
    "districts": 2
  },
  "MD" : {
    "name" : "Maryland",
    "FIPS" : "24",
    "districts": 8
  },
  "MA" : {
    "name" : "Massachusetts",
    "FIPS" : "25",
    "districts": 9
  },
  "MI" : {
    "name" : "Michigan",
    "FIPS" : "26",
    "districts": 14
  },
  "MN" : {
    "name" : "Minnesota",
    "FIPS" : "27",
    "districts": 8
  },
  "MS" : {
    "name" : "Mississippi",
    "FIPS" : "28",
    "districts": 4
  },
  "MO" : {
    "name" : "Missouri",
    "FIPS" : "29",
    "districts": 8
  },
  "MT" : {
    "name" : "Montana",
    "FIPS" : "30",
    "districts": 1
  },
  "NE" : {
    "name" : "Nebraska",
    "FIPS" : "31",
    "districts": 1
  },
  "NV" : {
    "name" : "Nevada",
    "FIPS" : "32",
    "districts": 4
  },
  "NH" : {
    "name" : "New Hampshire",
    "FIPS" : "33",
    "districts": 2
  },
  "NJ" : {
    "name" : "New Jersey",
    "FIPS" : "34",
    "districts": 12
  },
  "NM" : {
    "name" : "New Mexico",
    "FIPS" : "35",
    "districts": 3
  },
  "NY" : {
    "name" : "New York",
    "FIPS" : "36",
    "districts": 27
  },
  "NC" : {
    "name" : "North Carolina",
    "FIPS" : "37",
    "districts": 9
  },
  "ND" : {
    "name" : "North Dakota",
    "FIPS" : "38",
    "districts": 1
  },
  "OH" : {
    "name" : "Ohio",
    "FIPS" : "39",
    "districts": 16
  },
  "OK" : {
    "name" : "Oklahoma",
    "FIPS" : "40",
    "districts": 5
  },
  "OR" : {
    "name" : "Oregon",
    "FIPS" : "41",
    "districts": 5
  },
  "PA" : {
    "name" : "Pennsylvania",
    "FIPS" : "42",
    "districts": 18
  },
  "RI" : {
    "name" : "Rhode Island",
    "FIPS" : "44",
    "districts": 2
  },
  "SC" : {
    "name" : "South Carolina",
    "FIPS" : "45",
    "districts": 7
  },
  "SD" : {
    "name" : "South Dakota",
    "FIPS" : "46",
    "districts": 1
  },
  "TN" : {
    "name" : "Tennessee",
    "FIPS" : "47",
    "districts": 9
  },
  "TX" : {
    "name" : "Texas",
    "FIPS" : "48",
    "districts": 36
  },
  "UT" : {
    "name" : "Utah",
    "FIPS" : "49",
    "districts": 4
  },
  "VT" : {
    "name" : "Vermont",
    "FIPS" : "50",
    "districts": 1
  },
  "VA" : {
    "name" : "Virginia",
    "FIPS" : "51",
    "districts": 11
  },
  "WA" : {
    "name" : "Washington",
    "FIPS" : "53",
    "districts": 10
  },
  "WV" : {
    "name" : "West Virginia",
    "FIPS" : "54",
    "districts": 3
  },
  "WI" : {
    "name" : "Wisconsin",
    "FIPS" : "55",
    "districts": 8
  },
  "WY" : {
    "name" : "Wyoming",
    "FIPS" : "56",
    "districts": 1
  }
}

/*
 * Non-states FIPS territories. 
 * 
 *   
  "GU" : {
    "name" : "Guam",
    "FIPS" : "66"
  },
  "MP" : {
    "name" : "Northern Mariana Islands",
    "FIPS" : "69"
  },
  "AS" : {
    "name" : "American Samoa",
    "FIPS" : "60"
  },
  "PR" : {
    "name" : "Puerto Rico",
    "FIPS" : "72"
  },
  "VI" : {
    "name" : "Virgin Islands",
    "FIPS" : "78"
  }
*/
