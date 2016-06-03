$(function () {
    var url = "/euro_json/";

    $.getJSON(url, function(res){
        var data = res.euro;
        console.log(data);

        $('#euro-chart').highcharts({
            chart: {
                type: 'line'
            },
            title: {
                text: 'Variação do Euro'
            },
            xAxis: {
                type: 'category'
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Valor'
                },
                plotOptions: {
                    line: {
                        dataLabels: {
                            enabled: true
                        },
                    }
                },
            },
            legend: {
                enabled: false
            },
            series: [{
                data: data,
                dataLabels: {
                    enabled: true,
                    align: 'center',
                    style: {
                        fontSize: '15px'
                    }
                }
            }],
        });
    });
});