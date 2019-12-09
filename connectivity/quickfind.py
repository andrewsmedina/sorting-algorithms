class QuickFind:
    def __init__(self):
        self.n = 20
        self.ids = []
        for i in range(self.n):
            self.ids.append(i)

    def add(self, p, q):
        t = self.ids[p]
        if t == self.ids[q]:
            return True

        for idx, _id in enumerate(self.ids):
            if _id == t:
                self.ids[idx] = self.ids[q]

        return False
