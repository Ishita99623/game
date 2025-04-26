print("welcome to my first game! ")
name = input("what is your name? ")
age = int(input("What is your age? "))
health = 10
if age >= 18:
     print ("you are old enough to play! ")
     wants_to_play = input("Do you want to play?").lower()
     if wants_to_play == "yes":
          print("you are starting with" ,health, "health")
          print("Let's play!")
          left_or_right = input("First choice... left or right(left/right)?")
          if left_or_right == "left":
               print("Nice, you follow the path and reach a lake...Do you swim across or go around(across/around)?")
         elif left_or_right == "right":
               print("Ypu fell down off the cliff")
