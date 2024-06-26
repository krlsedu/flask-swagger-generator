import inspect

from flask_swagger_generator.components.swagger_models import SwaggerModel
from flask_swagger_generator.utils import PropertyType


class SwaggerSchemaAttribute(SwaggerModel):

    def __init__(self, name, value=None, type=None, reference=None):
        super(SwaggerSchemaAttribute, self).__init__()
        self.name = name
        self.reference = reference

        if type is not None:
            self.type = type
        else:
            if reference is not None:
                self.type = PropertyType.OBJECT.value
            else:
                self.type = PropertyType.from_value(value)

        self.value = value

    def perform_write(self, file):

        if PropertyType.ARRAY.equals(self.type):
            item_type_ = PropertyType.from_value(self.value)
            if item_type_.equals(PropertyType.OBJECT):
                entry = inspect.cleandoc(
                    """
                        {name}:
                          type: {type}  
                          items:
                            $ref: {ref}
                    """.format(
                            name=self.name,
                            type=self.type.value,
                            example=self.value,
                            ref=self.reference
                    )
                )
            else:
                entry = inspect.cleandoc(
                    """
                        {name}:
                          type: {type}  
                          items:
                            type: {items_type}
                    """.format(
                            name=self.name,
                            type=self.type.value,
                            example=self.value,
                            items_type=item_type_.value
                    )
                )
            entry = self.indent(entry, 4 * self.TAB)
            file.write(entry)
            file.write('\n')
        else:

            if self.reference:
                entry = inspect.cleandoc(
                    """
                        {name}:
                          $ref: {ref}  
                    """.format(
                            name=self.name,
                            ref=self.reference
                    )
                )
            elif self.value is not None:
                entry = inspect.cleandoc(
                    """
                        {name}:
                          type: {type}  
                          example: {example}  
                    """.format(
                            name=self.name,
                            type=self.type.value,
                            example=self.value
                    )
                )
            else:
                entry = inspect.cleandoc(
                    """
                        {name}:
                          type: {type}  
                    """.format(
                        name=self.name,
                        type=self.type.value,
                    )
                )

            entry = self.indent(entry, 4 * self.TAB)
            file.write(entry)
            file.write('\n')
