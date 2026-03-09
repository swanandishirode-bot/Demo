def dfs(jug1,jug2,target):
    stack=[]
    visited=[]

    stack.append((0,0))
    visited.append((0,0))

    while len(stack)>0:
        (x,y)=stack.pop()
        print("Current state:",x,y)

        if x==target or y==target:
            print("Target Reached")
            return
        
        moves=[
            (jug1,y),
            (x,jug2),
            (0,y),
            (x,0)
        ]

        transfer=min(x,jug2-y)
        moves.append((x-transfer,y+transfer))

        transfer=min(y,jug1-x)
        moves.append((x+transfer,y-transfer))

        for state in moves:
            if state not in visited:
                stack.append(state)
                visited.append(state)

jug1=int(input("Enter First jug Capacity:"))
jug2=int(input("Enter second Jug Capacity:"))
goal=int(input("Enter goal amount:"))

dfs(jug1,jug2,goal)