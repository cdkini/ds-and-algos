<h3>singly-linked-list</h3>

<h5>API</h5>

- void append(Object o)
  - Description: Appends the specified element to the end of the list
  - Complexity: O(n) where 'n' is the number of elements if we do not have a pointer to the tail. Otherwise, it will be O(1)
  
- void insert(Object o, int i)
  - Description: Inserts the specified element at the specified position of the list
  - Complexity: O(n) where 'n' is the number of elements in the list
  
- void clear()
  - Description: Removes all the elements from the list
  - Complexity: O(1)
  
- boolean contains(Object o)
  - Description: Returns true if the list contains the specified element
  - Complexity: O(n) where 'n' is the number of elements in the list
  
- int get(int i)
  - Description: Returns the element at the specified position in the list
  - Complexity: O(n) where 'n' is the number of elements in the list
  
- int indexOf(Object o)
  - Description: Returns the index of the first occurrence of the specified item in the list or -1 fi the list does not contain the element
  - Complexity: O(n) where 'n' is the number of elements in the list
  
- boolean isEmpty()
  - Description: Returns true if the list is empty
  - Complexity: O(1)
  
- void remove(int i)
  - Description: Removes the element at the specified position in the list
  - Complexity: O(n) where 'n' is the number of elements in the list

- boolean remove(Object o)
  - Description: Removes the first occurrence of the specified element from the list. Returns true if an element is removed
  - Complexity: O(n) where 'n' is the number of elements in the list

- boolean removeAll(Object o)
  - Description: Removes all occurrences of the specified elemen from the list. Returns true if an element is removed
  - Complexity: O(n) where 'n' is the number of elements in the list

- void sort()
  - Description: Sorts the list in ascending order
  - Complexity: O(nlogn) where 'n' is the number of elements in the list
  
- int size()
  - Description: Returns the number of elements in the list
  - Complexity: O(1)
