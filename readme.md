# Chicken Price Scraper
Markets
* Deinze
* ABC

## Install
* `docker build . -t chicken-price-api`
* `docker compose up -d`  
For some reason the cron service fails
* `docker exec -it chicken-price-api sh -c "service cron start"`
