class TextEditorStack:
    def __init__(self):
        self.history = []
    #1. PUSH: Add an action to the top of the stack
    def push_action(self,action):
        self.history.append(action)
        print(f"Performed action: '{action}'")
    
    #2. POP: Remove and return the top action from the stack
    def pop_action(self):
        if len(self.history)==0:
            print("Nothing to undo! The stack is empty.")
            return None
        
        removed_action = self.history.pop() #Removes the last item
        print(f"Undid Action:    '{removed_action}'")
        return removed_action
    
    #3. PEEK: Look at the top item without removing it
    def peek_top(self):
        if len(self.history) > 0:
            return self.history[-1]
        return None
    
#testing time
editor= TextEditorStack()
print("---Typing Text---")
editor.push_action("Typed: 'Hello'")
editor.push_action("Typed: 'Hello World'")
editor.push_action("Added Emoji: 'Rocket")

print("\n---Current State---")
print(f"Top of the stack is currently: {editor.peek_top()}")

print("\n--- Pressing Ctrl + Z (Undo) ---")
editor.pop_action() # Removes the emoji
editor.pop_action() # Removes 'Hello World'

print("\n--- Final Stack Content ---")
print(f"Remaining history: {editor.history}")