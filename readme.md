**Notebook**

**1. if val<br>**
if val = if bool(val)<br>
explain: if val != 0 or val != None , bool(val) = True. So sometimes, if val = None, you can use 【if not val】to replace 【if val is None】, the running time will be fast in leetcode.


**2. BFS --> Queue: FIFO<br>**
deque()<br>
append(): This function is used to insert the value in its argument to the right end of deque.<br>
popleft(): This function is used to delete an argument from the left end of deque.

**3. DFS --> Stack: FILO<br>**
deque()<br>
append(): This function is used to insert the value in its argument to the right end of deque.<br>
pop(): This function is used to delete an argument from the right end of deque.

**4. top k --> Heap<br>**
max_heap = [(-val, key) for key, val in dic.items()]<br>
min_heap = [(val, key) for key, val in dic.items()]<br>
heapq.heapify(max_heap)

**5. Tree traversal:<br>**
  Inorder: left --> mid --> right;<br>
  Preorder: mid --> left --> right;<br>
  Postorder: left --> right --> mid;<br>
  
**6. Stack**: LIFO (So the order of stack.append() need to be reverse for tree traversal. See iterative methods for 144)


**7. Two pointers**: Floyid-cycle detection algorithm/ find mid in the linked list: <br>
slow = slow.next, fast = fast.next.next<br>
An animation is shown in 202.happy number
