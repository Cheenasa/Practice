#!/usr/bin/env python
# coding: utf-8

# In[1]:


def collatz(n):
    if n%2==0:
        print(n//2)
        return n//2
    else:
        print(3*n+1)
        return 3*n+1

print("Please input a number: ")
n = int(input())


while n!=1:
    n = collatz(n)


# In[ ]:




