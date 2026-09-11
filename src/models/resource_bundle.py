from src.constants.resource import Resource
from collections import Counter

class ResourceBundle:
    def __init__(self, **kwargs):
        resources = {}
        for resource, quantity in kwargs.items():
            standardized_resource = Resource[resource]
            resources[standardized_resource] = quantity
        self.resources = Counter(resources)