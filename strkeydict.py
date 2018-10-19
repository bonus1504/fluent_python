from collections import UserDict


class StrKeyDict(UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    
    def __contains__(self, key):
        return str(key) in self.data
    
    def __setitem__(self, key, item):
        self.data[str(key)] = item


if __name__ == '__main__':
    d = StrKeyDict()
    d['a'] = 1
    d[1] = 2
    print(d)
    print(3 in d)
    print(d['4'])
