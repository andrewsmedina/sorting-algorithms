class QuickUnion:
    def __init__(self):
        self.n = 20
        self.ids = []
        for i in range(self.n):
            self.ids.append(i)

    def add(self, p, q):
        i = p
        while i != self.ids[i]:
            i = self.ids[i]

        j = q
        while j != self.ids[j]:
            j = self.ids[j]

        if i == j:
            return True

        self.ids[i] = j
        return False
