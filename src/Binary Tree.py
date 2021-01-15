def inorderTreeWalk(x):
    if x is not None:
        inorderTreeWalk(x.left)
        print(x.key)
        inorderTreeWalk(x.right)

def search(x,k):
    while x is not None and x.key !=  k:
        if x.key < key:
            x = x.left
        else:
            x = x.right
    return  x

def minimum(x):
    while x is not None:
        x = x.left
    return x

def maximum(x):
    while x is not None:
        x = x.right
    return x

def succesor(x):
    if x.right is not None:
        return minimum(x.right)
    y = x.p
    while y is not None and x == y.right:
        x = y
        y = y.p
    return y

def predecessor(x):
        if x.left is not None:
            return minimum(x.left)
        y = x.p
        while y is not None and x == y.left:
            x = y
            y = y.p
        return y

def insertion(T,z):
    y = None
    x = T.root
    while x is not None:
        y = x
        if z.key < x.key:
            x  = x.left
        else :
            x = x.right
    z.p = y
    if y is None:
        T.root = z.key
    else:
        if  z.key < y:
            y.left = z.key
        else:
            y.right = z.key

def transplant(T,u,v):
    if u.p is  not None:
        T.root = u
    elif u == u.p.left:
        v = u.p.left
    else:
        v = u.p.right
    if v is not  None:
        v.p = u.p

def delete(T,z):
    if z.left is None:
        transplant(T,z,z.right)
    elif z.right is None:
        transplant(T,z,z.left)
    else:
        y = minimum(z.right)
        if y.p is not z:
            transplant(y,y.right)
            y.right = z.right
            y.right.p = y
        transplant(z,y)
        y.left = z.left
        y.left.p = y

def build_binary_tree(A):
    for i in range(len(A)):
        insertion(A,)