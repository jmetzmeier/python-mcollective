"""
Security providers base
-----------------------
Provides YAML [de]serialization.
"""
from __future__ import print_function
from __future__ import absolute_import

from . import SerializerBase

try:
    import yaml
except ImportError as exc:
    print("You must install PyYAML in order to use YAML serializer.")
    raise exc


def construct_ruby_object(loader, suffix, node):
    return loader.construct_yaml_map(node)


def construct_ruby_sym(loader, node):
    return loader.construct_yaml_str(node)


class Serializer(SerializerBase):
    def __init__(self):
        yaml.add_multi_constructor(u"!ruby/object:", construct_ruby_object)
        yaml.add_constructor(u"!ruby/sym", construct_ruby_sym)

    """YAML specific serializer."""
    def serialize(self, msg):
        return yaml.safe_dump(dict(msg))

    def deserialize(self, msg):
        return yaml.load(msg)
