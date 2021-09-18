from enum import Enum
from attribute_id import AttributeId

class AttributeModType(Enum):
    FLAT = 1
    PERCENTADD = 2
    PERCENTMULTIPLY = 3

class AttributeModifier:

    def __init__(self, attribute_mod_type: AttributeModType, attribute_id: AttributeId, value: float, order: int, source = None):
        self.attribute_mod_type = attribute_mod_type
        self.attribute_id = attribute_id
        self.value = value
        self.order = order
        
