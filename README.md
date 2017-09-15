# Sites Monitoring Utility

A scripts shows status of sites from file in project directory. Criteria of checking:
  
  - Status code of site is 200;
  - Expiration date of site's domain will be valid 1 month or more.
  
  
# Using

For checking sites you should have file with domain names in root of project

```
$ python3 check_sites_health.py urls.txt
  
  https://devman.org - status code is 200, domain expiration date 1 month or more
  https://meduza.io - status code is 200, domain expiration date 1 month or more
```  


# Requirements

For installing requirements in root of project make:

`$ pip install -r requirements.txt`


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
