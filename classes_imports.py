#!/usr/bin/env python
# coding: utf-8

# In[ ]:




class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.food = cuisine_type
        
    def describe_restaurant(self):
        print(self.name)
        print(self.food)
        
    def open_restaurant(self):
        print('The restaurant is open')
        
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

class Admin(User):
    def __init__(self,privileges):
        self.privs = privileges
    
    def show_privileges(self):
        print(self.privs)

class Privileges():
    def __init__(self, privileges):
        self.privs = privileges
    
    def show_privileges(self):
        print(self.privs)

