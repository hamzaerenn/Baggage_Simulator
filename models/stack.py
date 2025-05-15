class BagajStack:
    def __init__(self):
        self.stack = []
    def push(self, bagaj, yolcu_id):
        self.stack.append((bagaj, yolcu_id))
    def pop(self):
        return self.stack.pop() if self.stack else None
    def peek(self):
        return self.stack[-1] if self.stack else None
    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
    def tum_bagajlar(self):
        return self.stack.copy()
