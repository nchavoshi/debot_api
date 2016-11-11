# DeBot Python API
A Python API for [DeBot](http://cs.unm.edu/~chavoshi/demo/).

## Install instructions

1. Clone this repository and enter the folder:
2. `python setup.py install`

## How to Use
DeBot API has 2 main functions for the user to get the data: "check_user(user)" and "check_date(date)".<br />
1. check_user(user): Given a Twitter user name, this function checks whether or not DeBot has detected the given account as a bot so far. If yes, it also returns the date of detection and the number of times that account was detected as a bot. In the following example, we query the account "loveforlover_01", and the output shows that DeBot detected this account as a bot on 2015-10-28 once, and on 2015-12-04 4 times.  
```python
import debot

db = debot.DeBot('your_api_key')
db.check_user('loveforlover_01')
```

Result:
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


