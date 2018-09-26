[![Build Status](https://travis-ci.org/brandonemma/fastfood_api.svg?branch=develop)](https://travis-ci.org/brandonemma/fastfood_api)

[![Coverage Status](https://coveralls.io/repos/github/brandonemma/fastfood_api/badge.svg?branch=develop)](https://coveralls.io/github/brandonemma/fastfood_api?branch=develop)



# fastfood_api
An online Food delivery application

#### view app on heroku
[HEROKU](https://fast-food-api-v2.herokuapp.com/api/v1/users/ORDERS).


# Technology
Api is a flask app 

## setup to run on local environment
To run in python version 3.6 
  - pip3.6 install -r requirements.txt
  - python3.6 routes.py

## To run in python version 2.7
  - pip install -r requirements.txt
  - python routes.py
  

|Method|EndPoint                       |Functionality                |
|------|-------------------------------|-----------------------------|     
|GET   |/api/v1/users/ORDERS           |Get all the orders           |          
|POST  |/api/v1/users/ORDERS           |Place a new order            |          
|GET   |/api/v1/users/ORDERS/<order_id>|Fetch a specific order       |          
|PUT   |/api/v1/users/ORDERS/<order_id>|Update the status of an order|          


# Usage
### When you make a get request to /api/v1/users/ORDERS you will recieve a json response like below.
```
[
    {
        "name": "oranges",
        "orderId": "1",
        "picture": "oranges.png",
        "price": 500,
        "status": "new order"
    },
    {
        "name": "peaches",
        "orderId": "2",
        "picture": "peaches.png",
        "price": 600,
        "status": "new order"
    }
]
 
```

### To fetch a specific order with a unique order_Id of 1
make a get request to /api/v1/users/ORDERS/1 and this is the response you will get
```
{
    "name": "oranges",
    "orderId": "1",
    "picture": "oranges.png",
    "price": 500,
    "status": "new order"
}
```

### To Update an order_item status you are required to enter:
Make a put request to /api/v1/users/ORDERS/<order_id>
With a status field.



### Rest Api Testing tools
```
Postman 
Insomnia
Pau
Advanced Rest Client(ARC)
```

### Tests
pytest 










