import inspect
from datetime import datetime
from typing import get_args, TypeVar

from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from marshmallow import Schema, fields

from flask_swagger_generator.generators import Generator
from flask_swagger_generator.utils import SwaggerVersion
from flask_swagger_generator.utils.utils import Utils

T = TypeVar('T')


class SwaggerView:
    @staticmethod
    def init(app: Flask, gerador: Generator = None, application_root: str = "", swagger_destination_path: str = None):
        if gerador is None:
            gerador = Generator.of(SwaggerVersion.VERSION_THREE)

        if swagger_destination_path is None:
            swagger_destination_path = 'static/swagger.yaml'

        SwaggerView.__init_swagger(app, gerador, swagger_destination_path, application_root)

    @staticmethod
    def __create_schema_from_class(annotation, is_sub_type=False):
        schema_dict = {}
        sub_type = None
        if hasattr(annotation, '__origin__'):
            # ddddd = annotation.__origin__
            if not is_sub_type:
                try:
                    sub_type = get_args(annotation)[0]
                    is_sub_type = True
                except TypeError:
                    pass
                class_obj = annotation.__origin__
            else:
                class_obj = annotation.__origin__
        else:
            class_obj = annotation
        try:
            annotations = class_obj.__annotations__
            for attribute, typ in annotations.items():
                if typ == str or typ == fields.String:
                    schema_dict[attribute] = fields.String(example="Abc 123")
                elif typ == int:
                    schema_dict[attribute] = fields.Int(example=1)
                elif typ == bool:
                    schema_dict[attribute] = fields.Bool(example=True)
                elif typ == datetime:
                    schema_dict[attribute] = fields.Str(example="2021-01-01T00:00:00.000Z")
                elif typ == float:
                    schema_dict[attribute] = fields.Float(example=1.0)
                elif Utils.is_list(typ):
                    from_class = SwaggerView.__create_schema_from_class(sub_type, is_sub_type)
                    schema_dict[attribute] = fields.List(fields.Nested(from_class), example=[from_class])
                else:
                    if sub_type is None:
                        schema_dict[attribute] = typ
                    else:
                        from_class = SwaggerView.__create_schema_from_class(sub_type, is_sub_type)
                        schema_dict[attribute] = fields.Nested(from_class)
            dynamic_schema = type(f"{class_obj.__name__}Schema", (Schema,), schema_dict)
        except AttributeError:
            dynamic_schema = type(f"defaultSchema", (Schema,), schema_dict)
        return dynamic_schema()

    @staticmethod
    def __init_swagger(app: Flask, generator: Generator, swagger_destination_path: str, application_root: str = ""):
        funcs = []
        for rule in app.url_map.iter_rules():
            http_methods = rule.methods
            if 'GET' in http_methods:
                status_code_ = 200
            else:
                status_code_ = 201

            func = app.view_functions[rule.endpoint]
            func_signature = inspect.signature(func)
            annotation = func_signature.return_annotation
            name__ = func.__name__
            if name__ in funcs:
                continue
            if annotation is not None and annotation != inspect.Signature.empty:
                schema_ = SwaggerView.__create_schema_from_class(annotation)
                generator.specifier.add_response(name__, status_code_, schema=schema_)
            else:
                generator.specifier.add_response(name__, status_code_, schema={})

            funcs.append(name__)

        generator.generate_swagger(app,
                                   destination_path=swagger_destination_path,
                                   application_name='fgl-py-check-order-integration',
                                   application_version='1.0.0',
                                   )
        swagger_url = f'{application_root}/swagger-ui'
        api_url = f'{application_root}/swagger'
        swagger_ui_blueprint = get_swaggerui_blueprint(
            swagger_url,
            api_url,
            config={}
        )
        app.register_blueprint(swagger_ui_blueprint, url_prefix=swagger_url)

        @app.route(f'{application_root}/swagger')
        def swagger():
            with open(swagger_destination_path, 'r') as f:
                swagger_yaml = f.read()
            return swagger_yaml
