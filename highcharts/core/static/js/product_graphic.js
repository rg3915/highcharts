$(function () {
    var url = "/product_json/";

    $.getJSON(url, function(res){
        console.log(res);
        /* Transformando o dicionário em lista.
           Com o comando map eu coloco uma lista dentro da outra,
           necessário para este tipo de gráfico. */
        var data = res.products.map(function (v) {
            return [v.categoria, v.porcentagem]
        });

        console.log(data);

        $('#product-chart').highcharts({
            chart: {
                type: 'pie'
            },
            title: {
                text: 'Porcentagem de produtos por categoria'
            },
            tooltip: {
                pointFormat: '<b>{point.percentage:.1f}%</b>'
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: true,
                        format: '<b>{point.name}</b>: {point.percentage:.1f} %'
                    }
                }
            },
            series: [{
                name: 'Categoria',
                colorByPoint: true,
                data: data
            }],
        });
    });
});