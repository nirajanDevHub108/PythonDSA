class Solution:
    def __init__(self):
        self.document=[]
        self.stack=[]
    def append(self, x):
        # append x into document
        self.document.append(x)
        self.stack.clear()

    def undo(self):
        # undo last change
        self.stack.append(self.document.pop())
        

    def redo(self):
        # redo changes
        self.document.append(self.stack.pop())

    def read(self):
        # read the document
        return "".join(self.document)