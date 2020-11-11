<h3>stack</h3>

<h5>API</h5>

- Stack()
  - Description: Constructor
  - Complexity: O(1)

- boolean empty()
  - Description: Tests if stack is empty
  - Complexity: O(1)
  
- Object peek()
  - Description: Looks at the top of the stack without removing it. Returns null if no such element exists
  - Complexity: O(1)
  
- Object pop()
  - Description: Looks at the top of the stack and removes it. Returns null if no such element exists
  - Complexity: O(1)
  
- void push(Object o)
  - Description: Push an item to the top of the stack
  - Complexity: O(1)
  
- Object search(Object o)
  - Description: Return the 1-based position from the top of the stack where the item is located. Returns null if no such element exists
  - Complexity: O(n) where 'n' is the number of elements in the Stack
