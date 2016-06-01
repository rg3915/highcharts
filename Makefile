shell_dollar:
	python manage.py shell < highcharts/shell/shell_dollar.py

shell_euro:
	python manage.py shell < highcharts/shell/shell_euro.py

shell_category:
	python manage.py shell < highcharts/shell/shell_category.py

shell_product:
	python manage.py shell < highcharts/shell/shell_product.py

screenshot:
	python highcharts/selenium/selenium_screenshot.py