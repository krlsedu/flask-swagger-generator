from datetime import datetime, timezone
import os
import tempfile
from typing import List
import unittest

from flask import Flask, jsonify

from flask_swagger_generator.generators.swagger_view import SwaggerView
from tests.resources.utils import yaml_as_dict


class ChildItem:
    code: str
    active: bool


class SamplePayload:
    title: str
    count: int
    enabled: bool
    ratio: float
    created_at: datetime
    children: List[ChildItem]
    extra: dict


class TestSwaggerView(unittest.TestCase):

    def test_swagger_view_init_with_marshmallow_v4_and_endpoints(self):
        app = Flask(__name__)

        @app.route('/items', methods=['POST'])
        def create_item(body: SamplePayload) -> SamplePayload:
            return jsonify({'status': 'ok'}), 201

        with tempfile.TemporaryDirectory() as tmp_dir:
            swagger_path = os.path.join(tmp_dir, 'swagger.yaml')
            SwaggerView.init(
                app,
                swagger_destination_path=swagger_path,
                application_name='TestApp',
                application_version='1.0.0',
            )

            self.assertTrue(os.path.exists(swagger_path))
            generated = yaml_as_dict(swagger_path)
            schemas = generated['components']['schemas']
            self.assertIn('create_item', schemas)
            self.assertIn('create_item_response_schema', schemas)

            props = schemas['create_item']['properties']
            self.assertEqual(props['title']['example'], 'Abc 123')
            self.assertEqual(props['count']['example'], 1)
            self.assertEqual(props['enabled']['example'], True)
            self.assertEqual(props['ratio']['example'], 1.0)
            self.assertEqual(
                props['created_at']['example'],
                datetime(2021, 1, 1, 0, 0, tzinfo=timezone.utc),
            )
            self.assertEqual(props['children']['type'], 'array')
            self.assertIn('children_create_item', schemas)
            self.assertIn('extra_create_item', schemas)

            client = app.test_client()
            swagger_resp = client.get('/swagger')
            self.assertEqual(swagger_resp.status_code, 200)
            self.assertIn(b'title: TestApp', swagger_resp.data)

            ui_resp = client.get('/swagger-ui/', follow_redirects=True)
            self.assertEqual(ui_resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()
