from attribute import Attribute
from attribute_id import AttributeId

class StatCollection:

    def __init__(self):
        self.attribute_dict = {}
    
    def add_to_dict(self, attribute_id: AttributeId, attribute: Attribute):
        self.attribute_dict[attribute_id] = attribute

    def get_attribute(self, attribute_id: AttributeId):
        return self.attribute_dict[attribute_id]
    
    def print_attributes(self):
        for key, value in self.attribute_dict.items():
            print(f"{key}, {value.base_value}")
