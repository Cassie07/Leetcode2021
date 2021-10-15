Notebook

1. if val
//if val = if bool(val)
//explain: if val != 0 or val != None , bool(val) = True. So sometimes, if val = None, you can use 【if not val】to replace 【if val is None】, the running time will be fast in leetcode.


2. BFS --> Queue: FIFO
deque()
append(): This function is used to insert the value in its argument to the right end of deque.
popleft(): This function is used to delete an argument from the left end of deque.

3. DFS --> Stack: FILO
deque()
append(): This function is used to insert the value in its argument to the right end of deque.
pop(): This function is used to delete an argument from the right end of deque.

4. top k --> Heap
max_heap = [(-val, key) for key, val in dic.items()]
min_heap = [(val, key) for key, val in dic.items()]
heapq.heapify(max_heap)

5. Tree traversal:
  Inorder: left --> mid --> right;
  Preorder: mid --> left --> right;
  Postorder: left --> right --> mid;
  
6. Stack: LIFO (So the order of stack.append() need to be reverse for tree traversal. See iterative methods for 144)
