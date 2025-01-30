from collections import deque
def water_jug_problem(cap1,cap2,target):
    visited = set()  #track visited states
    queue = deque([(0,0)]) #start both jugs empty

    while queue:
        x, y = queue.popleft()
        # if target is achieved, return True
        if x == target or y == target:
            return True
        
        if (x,y) in visited:
            continue
        visited.add((x,y))
        # add all possible states to the queue
        queue.extend([
            (cap1,y), # fill jug 1
            (x,cap2),   # fill jug 2
            (0,y), # empty jug 1
            (x,0),  # empty jug 2
            (x-min(x,cap2-y),y+min(x,cap2-y)), # pour jug 1 to jug 2
            (x+min(y,cap1-x),y-min(y,cap1-x)) # pour jug 2 to jug 1
        ])
    return False  #no solution found

cap1, cap2, target = 10000, 999999999, 4
if water_jug_problem(cap1,cap2,target):
    print(f"It is possible to measure {target} liters of water")
else:
    print(f"It is not possible to measure {target} liters of water")
