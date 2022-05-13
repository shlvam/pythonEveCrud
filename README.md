# pythonEveCrud

## get request
curl -i http://127.0.0.1:5000

## get request for individual collections
curl -i http://127.0.0.1:5000/product

## for post request
curl -d '[{"product_name": "Coco", "price": 120.45}, {"product_name": "Lays", "price": 120}]' -H 'Content-Type: application/json' http://127.0.0.1:5000/product

## passing query paramete
http://127.0.0.1:5000/product?sort=price

## put request


