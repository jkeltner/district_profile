// placeholder dictionary where we will add all the chart objects for easy update
charts = {}

// initial loading function that creates all the chart objects we will need on the page
function createCharts() {
    $(".chart").each(function() {
        var newChart = new Chart(this, {
            type: 'bar',
            data: {}
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

// function updateChartsReturn(data, textStatus, jqXHR) {
//     data = JSON.parse(data)
//     for (var chart in data) {
//         chartObj = charts[chart]
//         chartObj["data"].labels = data[chart]["labels"]
//         district_dataset = {
//             label: "District",
//             data: data[chart]["district_data"],
//             backgroundColor : "rgba(55,93,161,0.9)"
//         }
//         state_dataset = {
//             label: "State",
//             data: data[chart]["state_data"],
//             backgroundColor : "rgba(68,114,196,0.35)"
//         }
//         fed_dataset = {
//             label: "Country",
//             data: data[chart]["fed_data"],
//             backgroundColor : "rgba(167,181,219,0.25)"
//         }
//         chartObj["data"].datasets.length = 0
//         chartObj["data"].datasets.push(district_dataset)
//         chartObj["data"].datasets.push(state_dataset)
//         chartObj["data"].datasets.push(fed_dataset)
//         chartObj.update()
//     }
// }

// simple function to update all the data
function updateCensusCharts(state="06", district="27") {
    // wipe out all the existing data
    for (var chart in charts) {
        chartObj = charts[chart]
        chartObj["data"].datasets.length=0
        chartObj.update()
        jQuery.get("/getdata/census?chart_name="+chart+"&state="+state+"&district="+district, updateChartReturn(chart))
    }
}