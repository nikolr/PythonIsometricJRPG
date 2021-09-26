class StatCollection:

    def __init__(self):
        self.attribute_dict = {}
    
    def add_to_dict(self, attribute_id, attribute):
        self.attribute_dict[attribute_id] = attribute

    def get_attribute(self, attribute_id):
        return self.attribute_dict[attribute_id]
    
    def print_attributes(self):
        for key, value in self.attribute_dict.items():
            print(f"{key}, {value.base_value}")
