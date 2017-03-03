class Index(object):
    def __init__(self):
        self.len = 0
        self.docs = []

    def add_doc(self,num):
        if num not in self.docs:
            self.docs.append(num)
            self.docs.sort()
            self.len += 1
