from collections import deque

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
    
def BFS(root):
    

    if(root == None):
        return []
    
    q = deque()
    q.append((root,0))
    current_level = 0
    dicty = {}
   
    while(q):
        #Accessing the level of front element of queue, checking whether current
        #level is updated or not with respect to the queue's first element level
        if(q[0][1] == current_level): 
            #Node at front of queue
            node = q[0][0]
            #If left child is not NULL, append it to the queue
            if(node.left != None):
                q.append((node.left,current_level + 1))
            #If right child is not NULL, append it to the queue
            if(node.right != None):
                q.append((node.right,current_level + 1))
            
            #Pop the front element(relative root of left and right child above)
            q.popleft()
   
            
            if(current_level >= len(dicty)):
                if (current_level) not in dicty:
                    dicty[current_level] = []
                    dicty[current_level].append(node.val)
                else:
                    dicty[current_level].append(node.val)
            else:
                dicty[current_level].append(node.val)
        else:
            current_level = current_level + 1
            
    
    result = []
    for k,v in dicty.items():
        if(k%2 == 0):
            result.append(v)
        else:
            result.append(v[::-1])
        
    return result
