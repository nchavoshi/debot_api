# DeBot Python API
A Python API for [DeBot](http://cs.unm.edu/~chavoshi/demo/).

## Quickstart

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

## Install instructions

1. Clone this repository and enter the folder:
2. `python setup.py install`

## Dependencies

### Python dependencies
* [requests](http://docs.python-requests.org/en/latest/)

You can install requests via pip:

    pip install requests tweepy
    
### How to get the API key:
To get the key, please click [here](http://cs.unm.edu/~chavoshi/demo/api.html)


