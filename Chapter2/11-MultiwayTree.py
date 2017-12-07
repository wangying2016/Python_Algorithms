class Tree:
    def __init__(self, kids, next=None):
        self.kids = self.val = kids
        self.next = next


t = Tree(Tree('a', Tree('b', Tree('c', Tree('d')))))
t.kids.next.next.next.val
