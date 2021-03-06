# https://www.youtube.com/watch?v=9HFbhPscPU0&t=1s

class HashTable:

    def __init__(self):
        self.size = 100
        self.hashmap = [[] for _ in range(0, self.size)]
        # print(self.hashmap)

    def hash_func(self, key):
        hashed_key = hash(key) % self.size
        return hashed_key

    def set(self, key, value):
        hash_key = self.hash_func(key)
        key_exists = False
        slot = self.hashmap[hash_key]
        for i, kv in enumerate(slot):
            k, v = kv
            if key == k:
                key_exists = True
                break

        if key_exists:
            slot[i] = ((key, value))
        else:
            slot.append((key, value))

    def get(self, key):
        hash_key = self.hash_func(key)
        slot = self.hashmap[hash_key]
        for kv in slot:
            k, v = kv
            if key == k:
                return v
            else:
                raise KeyError('Key does not exist.')




if __name__ == "__main__":

    H = HashTable()
    H.set('key1','value1')
    H.set('key2','value2')
    H.set('key3','value3')

    H.set(10,'value10')
    H.set(20, 'value20')



    print(H.hashmap)


