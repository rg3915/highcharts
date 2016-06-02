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

pdf:
	latexmk -pdf -shell-escape highcharts.tex

pvc:
	latexmk -pdf -shell-escape -pvc highcharts.tex

pdf43:
	latexmk -pdf -shell-escape highcharts43.tex

pvc43:
	latexmk -pdf -shell-escape -pvc highcharts43.tex

clear:
	latexmk -c
	rm *.nav *.snm *.vrb
