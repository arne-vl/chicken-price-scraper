# Chicken Price Scraper
Markets
* Deinze
* ABC

## Install (using cloned code)
* `docker compose up -d`
  
For some reason the cron service fails (sometimes)
* `docker exec -it chicken-price-api sh -c "service cron status"`
* `docker exec -it chicken-price-api sh -c "service cron start"`

## Install (Image)
Dockerhub: `arnevl/chicken-price-api`
