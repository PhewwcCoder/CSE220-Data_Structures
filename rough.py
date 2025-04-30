def count(t,r,remove,percentage):
    if percentage < 0.97:
        return remove
    return count(t-1,r-1,remove+1,(r-1)/(t-1))
print(count(100,99,0,0.99))


