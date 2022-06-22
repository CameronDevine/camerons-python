__all__ = ["AttrDict"]


class AttrDict:
    def __init__(self, data):
        self.__data = data

    def __getattr__(self, key):
        return self.transform_output(self.__data.get(key, None))

    @classmethod
    def transform_output(cls, data):
        if isinstance(data, dict):
            return AttrDict(data)
        elif isinstance(data, list):
            return [self.transform_output(val) for val in data]
        else:
            return data
