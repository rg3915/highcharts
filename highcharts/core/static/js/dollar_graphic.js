$(function () {
    var url = "/dollar_json/";

    $.getJSON(url, function(res){
        console.log(res);
        /* Transformando o dicionário em lista.
           Com o comando map eu coloco uma lista dentro da outra,
           necessário para este tipo de gráfico. */
        var data = res.dollar.map(function (v) {
            return [v.dia, v.valor]
        });

        console.log(data);

        $('#dollar-chart').highcharts({
            chart: {
                type: 'line'
            },
            title: {
                text: 'Variação do Dólar'
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