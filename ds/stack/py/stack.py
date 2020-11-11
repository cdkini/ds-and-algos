class Stack:
    def __init__(self):
        self.__contents = []

    def empty(self):
        return len(self.__contents) == 0

    def peek(self):
        if self.empty():
            return None
        return self.__contents[-1]

    def pop(self):
        if self.empty():
            return None
        return self.__contents.pop()

    def push(self, item):
        self.__contents.append(item)

    def search(self, item):
        i = len(self.__contents) - 1
        while i >= 0:
            if self.__contents[i] == item:
                return len(self.__contents) - i
            i -= 1
        return None

    @property
    def contents(self):
        return self.__contents

