# Pricing Module

## Development

 - Python 3.8.10
 - pip 21.3.1
 - Git
 - Django

### Running locally

  - Clone the Pricing module repository.
        ```$git clone git@github.com:Sarathsathyan/Pricing_Module-.git```
  - Create virtualenv & activate.
  - Install the requirements
        ```pip install -r requirements.txt```
  - Makemigrations and Migrate
    - python manage.py makemigrations
    - python manage.py migrate

###Documentation

  - API for create Base price config
    - http://127.0.0.1:8001/api/price_info/
    - method : POST
    - params
      - {
    "base_distance":3,
    "dbp":80,
    "tbp":20,
    "dap":30
}
  - List all base prices
    - http://127.0.0.1:8001/api/price_info/
    - method : GET
  - API for calculating Total price
    - http://127.0.0.1:8001/api/price_info/{base_price_id}/price_calculate/
    - method : POST
    - params
      - {"distance":10 }

