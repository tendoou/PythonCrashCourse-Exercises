class Cipher(object):
    def __init__(self, map1, map2):
        self.map1 = list(map1)
        self.map2 = list(map2)

    def encode(self, s):
        s1 = []
        s = list(s)
        for x in s:
            temp = self.map1.index(x)
            s1.append(self.map2[temp])
        return ''.join(s1)

    def decode(self, s):
        s1 = []
        s = list(s)
        for x in s:
            temp = self.map2.index(x)
            s1.append(self.map1[temp])

        return ''.join(s1)


map1 = "abcdefghijklmnopqrstuvwxyz"
map2 = "etaoinshrdlfwypvbgkjqxz"
cipher = Cipher(map1, map2)
print(cipher.encode("!@#"))
print(cipher.encode("xyz"))
print(cipher.decode("eirfg"))
print(cipher.decode("erlang"))