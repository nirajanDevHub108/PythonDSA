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
    
    
'''
Intuition
We need to simulate a text editor with undo and redo operations.

append(x) → add a character to the document
undo() → remove the last appended character
redo() → restore the last undone character
To support undo/redo efficiently, we use two stacks:

Undo stack (st1) → stores characters currently present in the document
Redo stack (st2) → stores characters removed by undo (so they can be restored)
The string s represents the current document content.

Approach
append(char x)

Add x to the string s
Push x into the undo stack (st1)
(Redo stack is not touched)
undo()

If undo stack is not empty:
Pop the top character from st1
Push it into redo stack (st2)
Remove the last character from string s using substring
redo()

If redo stack is not empty:
Pop a character from st2
Push it back into undo stack (st1)
Append it again to string s
read()

Simply return the current string s
This mirrors how real editors manage undo/redo actions.

java solution-stack 
class Solution {
    String s = "";
    Stack<Character> st1 = new Stack<>(); // for undo
    Stack<Character> st2 = new Stack<>(); // for redo
    public void append(char x) {
        // append x into document
        s = s + x;
        st1.push(x);
    }

    public void undo() {
        if(!st1.isEmpty()){
            st2.push(st1.pop()); // remove from undo and push to redo
            s = s.substring(0, s.length()-1);
        }
    }

    public void redo() {
        if(!st2.isEmpty()){
            char c = st2.pop(); // remove from redo
            st1.push(c); // push to undo
            s = s + c;
        }
    }

    public String read() {
        return s;
    }
}
'''