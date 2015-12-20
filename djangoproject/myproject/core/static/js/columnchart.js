$(function () {
    var url = "/population/json";
    var categories_data = new Array();
    var year1800_data = new Array();
    var year1900_data = new Array();
    var year2008_data = new Array();

    $.getJSON(url, function(res){
        console.log(res);
        // 5 Continents
        for (i = 0; i < 5; i++) {
            categories_data.push(res[i]['fields']['continent']);
        };
        // 5 populations by year
        for (i = 5; i < 10; i++) {
            year1800_data.push(res[i]['fields']['population']);
        };
        // 5 populations by year
        for (i = 10; i < 15; i++) {
            year1900_data.push(res[i]['fields']['population']);
        };
        // 5 populations by year
        for (i = 15; i < 20; i++) {
            year2008_data.push(res[i]['fields']['population']);
        };

        $('#container').highcharts({
            chart: {
                type: 'column'
            },
            title: {
                text: 'Monthly Average Rainfall'
            },
            subtitle: {
                text: 'Source: WorldClimate.com'
            },
            xAxis: {
                categories: categories_data,
                crosshair: true
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Rainfall (mm)'
                }
            },
            tooltip: {
                headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
                pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                    '<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>',
                footerFormat: '</table>',
                shared: true,
                useHTML: true
            },
            plotOptions: {
                column: {
                    pointPadding: 0.2,
                    borderWidth: 0
                }
            },
            series: [{
                name: 'Year 1800',
                data: year1800_data

            }, {
                name: 'Year 1900',
                data: year1900_data

            }, {
                name: 'Year 2008',
                data: year2008_data

            }]
        });
    });
});