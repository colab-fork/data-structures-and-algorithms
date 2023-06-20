class Dog:
    
    species = 'mammal' #default value for all objects
    
    def __init__(self, age, name): #initializer, adding attributes to the class
        self.age = age
        self.name = name
    
    def speak(self, sound): #Behaviours are called instant methods, adding instant methods to the class
        print(f"{self.name} says {sound}")

philo = Dog(3, "Doge")
print(philo.age) # Accessing attributes using dot notation

philo.speak("wuff gruff")


"""
>>> %Run -c $EDITOR_CONTENT
3
Doge says wuff gruff

"""
