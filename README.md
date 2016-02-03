# fenero
A Python module for the Fenero Cloud Contact Center API

Written and tested in Python 3.5

## Usage

Save fenero.py into the same directory as your pyhton script

```python
from fenero import APICall
# set user ID and API token, as they are passed with every method
user_id = 1234 
app_token_id = "b4v6sdf484ca9s8d4csdac654dgkg"

# Instantiate the class
results = APICall()

# Call any class method
print(results.get_dids(user_id, app_token_id))
```

## API Reference

https://support.fenero.com/portal/helpcenter/articles/interaction-api-for-admin-functions


