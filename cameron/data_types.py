import json

__all__ = ["AttrDict"]


class AttrDict:
    def __init__(self, data):
        self.__data = data

    def __getattr__(self, key):
        return self.transform_output(self.__data.get(key, None))

    @classmethod
    def transform_output(cls, data):
        if isinstance(data, dict):
            return cls(data)
        elif isinstance(data, list):
            return [cls.transform_output(val) for val in data]
        else:
            return data

    def __repr__(self):
        return "{}({})".format(type(self).__name__, self.__data)

    def __str__(self):
        return str(self.__data)

    @classmethod
    def json_load(cls, filename):
        with open(filename) as f:
            return cls(json.load(f))

    @classmethod
    def json_loads(cls, json_data):
        return cls(json.loads(f))
