# ERC-20_web-scraper
Created a web-scraper to pull all ERC-20 token names and their 7 day transfer totals. These two data sets are then graphed against each other matplotlib.

This web-scraper is built to run on https://bloxy.info/list_tokens/ERC20?page=1

It has the functionality to run on all pages 1-50 by changing the range in the for loop on line 10. (axes might overflow into each other for the more pages pulled in)

Enjoy!
