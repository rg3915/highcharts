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
                type: 'bar'
            },
            title: {
                text: 'Historic World Population by Region'
            },
            subtitle: {
                text: 'Source: Wikipedia.org'
            },
            xAxis: {
                // categories: ['Africa', 'America', 'Asia', 'Europe', 'Oceania'],
                categories: categories_data,
                title: {
                    text: null
                }
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Population (millions)',
                    align: 'high'
                },
                labels: {
                    overflow: 'justify'
                }
            },
            tooltip: {
                valueSuffix: ' millions'
            },
            plotOptions: {
                bar: {
                    dataLabels: {
                        enabled: true
                    }
                }
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'top',
                x: -40,
                y: 100,
                floating: true,
                borderWidth: 1,
                backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
                shadow: true
            },
            credits: {
                enabled: false
            },
            series: [{
                name: 'Year 1800',
                // data: [107, 31, 635, 203, 2]
                data: year1800_data
                // data: [{% for item in Year1800 %}{{ item.population }},{% endfor %}]
            }, {
                name: 'Year 1900',
                // data: [133, 156, 947, 408, 6]
                data: year1900_data
            }, {
                name: 'Year 2008',
                // data: [973, 914, 4054, 732, 34]
                data: year2008_data
            }]
        }); // end of chart
    }); // end of getJSON
});
