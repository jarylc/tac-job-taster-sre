#!/bin/ash
echo "30" > balance.txt
echo "5" > expense.txt
echo "0" > income.txt

sed -i "s/PAGERDUTY_SERVICE_KEY/${PAGERDUTY_SERVICE_KEY}/g" alertmanager.yml

python3 main.py &
mkdocs serve -q --no-livereload &
alertmanager --config.file=alertmanager.yml &
karma --alertmanager.uri http://127.0.0.1:9093 --alertmanager.interval 10s --alertmanager.proxy true &
prometheus --config.file=prometheus.yml
