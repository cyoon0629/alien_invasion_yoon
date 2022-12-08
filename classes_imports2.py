#!/usr/bin/env python
# coding: utf-8

# In[ ]:



class User:
    
    def __init__(self, first_name, last_name, age, sex, weight, login_attempts):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.sex = sex
        self.weight = weight
        self.log_attempts = login_attempts
    
    def describe_user(self):
        print(f'first name: {self.first}')
        print(f'last name: {self.last}')
        print(f'age: {self.age}')
        print(f'sex: {self.sex}')
        print(f'weight: {self.weight}')
    
    def greet_user(self):
        print(f'Hi {self.first} {self.last}, good to see you')
        
    def increment_login_attempts(self):
        self.log_attempts +=1
    
    def reset_login_attempts(self):
        self.log_attempts = 0

