
class dog():
        
    def __init__(self, age):
        self.barking_sound = "bauuuuuu"
        self.age = age


    def bark(self):
        print(self.barking_sound)

    def modify_barking():
        self.barking_sound = "baubau"

    def go_to_sleep():
        print("zzZzzzZz")
    
    def tellage():
        print(self.age)

dog(12)
dog.bark()
dog.go_to_sleep()
