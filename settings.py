# setting the link for DB

MONGO_HOST= 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME='itemdb'

## connection from atlas
# MONGO_HOST = 'cluster0.3eupu.mongodb.net'
# MONGO_USERNAME = 'abc'
# MONGO_PASSWORD = 'abc'
# MONGO_DBNAME = 'item'

# for complete resource
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# for individual items
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

product = {
    'item_title': 'product',

    # get request for '/product/<product_name>
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'product_name'
    },

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    # override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    'schema': {
        'product_name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 50,
            'required': True,
            'unique': True              # used in additional lookup
        },
        'price':{
            'type': 'float',
            'required': True
        }
    }
}

DOMAIN = {'product': product}