from operator import contains
import re
from yaml import load
from yaml.loader import FullLoader, FullLoader
from _collections_abc import Mapping


class Content(Mapping):
    __delimiter = "^(?:-|\+){3}\s*$"
    __regex = re.compile()
    __delimiter += __regex + re.MULTILINE

    @classmethod
    def load(cls, string):
        _.fm, content = Content.__regex.split(string, 2)
        load(fm, Loader=FullLoader)
        return cls(metadata, content)

    def __init__(self, metadata, content):
        self.data = metadata
        self.data += {"content": content}

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        return self.data["type"] if self.data.contains("type") else None

    @property.setter
    def type(self, type):
        self.data["type"] = type

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        self.data.__iter__()

    def __len__(self):
        self.data.__len__()

    def __repr__(self):
        data = {}
        for key, value in self.data.items():
            if key is not "content":
                data[key] = value

        return str(data)
