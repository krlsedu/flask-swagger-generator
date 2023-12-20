# Flask Swagger Generator
Flask swagger generator is a library to create Swagger Open API definitions 
for Flask based applications. Swagger is an Interface Description Language for describing REST 
APIs expressed using JSON and YAML. 

## Installing 
Install and update using pip:

```
pip install flask-swagger-init
```

## Documentation and Examples
COMING SOON

## A Simple Example

```python

from flask import Flask
from flask_swagger_generator.generators.swagger_view import SwaggerView


# Create the flask app
app = Flask(__name__)
...
# Create all the routes for the app
...

# Note: The swagger view must be created after all the routes have been created
# Create and publish the swagger view
SwaggerView.init(app=app, 
                 application_version='1.0.0', 
                 application_name='My API', 
                 application_description='My API description')
```

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Based on
This application is based on the [flask-swagger-generator](https://github.com/coding-kitties/flask-swagger-generator) project by [Coding Kitties](https://github.com/coding-kitties).
