#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random as r

class Random:
    def __init__(self):
        self.amount = 0
        self.min = 0
        self.max = 0
        
    def random_number(self, amount, min_number, max_number):
        if type(amount) == int and type(min_number) == int and type(max_number) == int:
            self.amount = amount
            self.min = min_number
            self.max = max_number + 1
        else:
            raise TypeError("The values inputted must all be of type integer.")
        
        number_list = []
        for i in range(self.amount):
            number = r.randint(self.min, self.max)
            number_list.append(number)
        
        return number_list

x = Random()

print(x.random_number(10, 10, 20))


print(x.random_number(5, 25, 50))




# In[ ]:





# In[ ]:




