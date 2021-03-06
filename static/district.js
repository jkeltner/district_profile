// placeholder dictionary where we will add all the chart objects for easy update
charts = {}

// initial loading function that creates all the chart objects we will need on the page
function createCharts() {
    $(".chart").each(function() {
        var newChart = new Chart(this, {
            type: 'bar',
            data: {},
            options: {
                responsive: true,
                legend: {
                    position: 'top',
                },
                scales: {
                    xAxes: [{
                        ticks: {
                            fontSize: 10
                        }
                    }],
                    yAxes: [{
                        ticks: {
                            beginAtZero:true
                        }
                    }]
                }       
            }
        })
        charts[this.id] = newChart
    })
}

function updateChartReturn(chart_name) {
    return function(data, textStatus,jqXHR) {
        data = JSON.parse(data)
        chartObj = charts[chart_name]
        chartObj["data"].labels = data["labels"]
        district_dataset = {
            label: "District",
            data: data["district_data"],
            backgroundColor : "rgba(55,93,161,0.9)"
        }
        state_dataset = {
            label: "State",
            data: data["state_data"],
            backgroundColor : "rgba(68,114,196,0.35)"
        }
        fed_dataset = {
            label: "Country",
            data: data["fed_data"],
            backgroundColor : "rgba(167,181,219,0.25)"
        }
        chartObj["data"].datasets.length = 0
        chartObj["data"].datasets.push(district_dataset)
        chartObj["data"].datasets.push(state_dataset)
        chartObj["data"].datasets.push(fed_dataset)
        chartObj.update()
    }
}

// simple function to update all the data
// requires state coming in FIPS number
function updateCensusCharts(state="06", district="27") {
    // wipe out all the existing data
    for (var chart in charts) {
        // Eliminate the old data
        chartObj = charts[chart]
        chartObj["data"].datasets.length=0
        chartObj.update()
        // Pull thew new data
        jQuery.get("/getdata/census?chart_name="+chart+"&state="+state+"&district="+district, updateChartReturn(chart))
    }
}

// function recenters the map to the district.
// requires state as USPS code and district as number
function reCenterMap(state="CA", district="27") {
    $("#map").attr('src', 'https://www.govtrack.us/congress/members/embed/mapframe?&bounds='+
        bboxes[state+district][0].toFixed(2)+","+
        bboxes[state+district][3].toFixed(2)+","+
        bboxes[state+district][2].toFixed(2)+","+
        bboxes[state+district][1].toFixed(2))
}

// requires state as a USPS code and district as a string of the number
function loadData(state, district) {
    $(document).attr("title", states[state]["name"]+" "+district);
    $('#title').text(states[state]["name"]+" "+district);
    if (district < 10) {
        district = "0"+district;
    }
    reCenterMap(state, district);
    updateCensusCharts(states[state]["FIPS"], district);

}

function initialLoad(state, district) {
    createCharts();
    $('#state_selector').change(stateSelected)
    $('#change_district_button').click(function() {
        loadData($('#state_selector').val(), $('#district_selector').val());
        $('#districtModal').modal('toggle');
    });
    if(state != '' && district != '') {
        loadData(state, district);
    } else {
        $('#districtModal').modal(show=true);
    }
    $('#district_selector').attr("disabled", "disabled");
    for (var state in states) {
        $('#state_selector').append('<option value=' + state + '>' + states[state]["name"] + '</option>');
    }   
}

function stateSelected() {
    $('#district_selector').find('option').remove()
    districts = states[$('#state_selector').val()]["districts"];
    if (districts == 1) {
         $('#district_selector').append('<option value="0">At Large Distict</option>');
    } else {
        for (var i=1; i<=districts; i++) {
            $('#district_selector').append('<option value="'+i+'">District '+i);
        }
    }
    $('#district_selector').attr("disabled", false);

}

