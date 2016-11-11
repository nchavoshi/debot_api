# DeBot Python API
A Python API for [DeBot](http://cs.unm.edu/~chavoshi/demo/).

## Install instructions

1. Clone this repository and enter the folder:
2. `python setup.py install`


## Get the list of the detected bots
Given a date as the input, the "get_bots_list" function returns all the clusters of bots that Debot detected on that date. In the following example, we want to get the list of the bots detected on December 4th 2015. The output shows 2 clusters containing 8 bots totally. 
```python
import debot

db = debot.DeBot('your_api_key')
db.get_bots_date_range('2015-12-04','2015-12-06')
```

Output:
```xml
<?xml version="1.0"?>
<response status="success">
 <date>2015-12-04</date>
 <cluster cluster_id="1" size="5">
  <user>ma_arrioja</user>
  <user>Napebar23Perez</user>
  <user>HectorGarasUh</user>
  <user>GonzalezVictor_</user>
  <user>GladyoscariS</user>
  </cluster>
 <cluster cluster_id="2" size="3">
  <user>MadridReal</user>
  <user>nada1998</user>
  <user>cup201711</user>
 </cluster>
</response>
```

## Check a Twitter Account
Given a Twitter user name, the "check_user" function checks whether or not DeBot has detected the given account as a bot so far. If yes, it also returns the date of detection and the number of times that account was detected as a bot on that date. In the following example, we query the account "loveforlover_01", and the output shows that DeBot detected this account as a bot once on 2015-10-28, and 4 times on 2015-12-04.  
```python
import debot

db = debot.DeBot('your_api_key')
db.check_user('loveforlover_01')
```

Output:
```xml
<?xml version="1.0"?>
<response status="success">
 <user>loveforlover_01</user>
 <dates>
  <date count="1">2015-10-28</date>
  <date count="4">2015-12-04</date>
 </dates>
</response>
```

## Dependencies

* [requests](http://docs.python-requests.org/en/latest/)

You can install requests via pip (you may need sudo access):

    pip install requests
    
## How to get the API key:
To get the key, please click [here](http://cs.unm.edu/~chavoshi/demo/api.html)


