# a class is like a blueprint, instances are objects of a class
class Person:
    def __init__(self, name, age):
        self.name = name #Instance variable
        self.age = age
        
person1= Person("Abdullah", 9)
person2 = Person("Shahid", 18)

print(person1.name, person1.age)
print(person2.name, person2.age)


"""
>>> %Run -c $EDITOR_CONTENT
Abdullah 9
Shahid 18

Why?
- To represent the characteristic or state of indidividual objects.
- To store data unique to each instance.
- To provide a way for instances to maintain their own data.

"""
