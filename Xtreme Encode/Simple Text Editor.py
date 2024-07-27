class TextEditor:
    def __init__(self):
        self.text = ""
        self.history = []

    def append(self, string):
        self.history.append(self.text)
        self.text += string

    def delete(self, k):
        self.history.append(self.text)
        self.text = self.text[:-k]

    def print_char(self, k):
        print(self.text[k-1])

    def undo(self):
        self.text = self.history.pop()

def main():
    q = int(input())
    editor = TextEditor()
    for _ in range(q):
        ops = input().split()
        if ops[0] == "1":
            editor.append(ops[1])
        elif ops[0] == "2":
            editor.delete(int(ops[1]))
        elif ops[0] == "3":
            editor.print_char(int(ops[1]))
        elif ops[0] == "4":
            editor.undo()

if __name__ == "__main__":
    main()