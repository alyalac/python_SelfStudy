import numpy as nu
import time

class NumericalMethods:
    
# iteration 
    def root_finding(self):
        x = 0
        while x <= 5: # or True
            if x * x == 9:
                print("Root Finding: ", x)
            x += 1  


# Square Root Approximation 

    def sr_approximation(self):
        number = 25
        guess = 1
        for i in range(10):
            guess = (guess + number / guess) / 2 
            print ( "Step ", i,  "Guess: " , guess )

#array
    def array_number(self):
         numbers = nu.array([5, 2, 8])

         numbers = numbers * 2

         print (numbers[0])
         print (numbers[1])
         print (numbers[2])


    def car_distance(self):
            
            speed = 60
        
            for hour in range(1, 6):

                 distance = speed * hour

                 print("After", hour, "hours:", distance, "km")



    def ball_falling(self):
         
         height = 5
         seconds = 0

         while height >= 0:
           
            if height == 0:
                print("Time:", seconds, "seconds,  The ball hit the ground!")
            else:
                print("Time:", seconds, "seconds, Ball is at", height, "meters")
                
          
            height = height - 1
            seconds = seconds + 1


            time.sleep(1)



out = NumericalMethods()

# out.root_finding()

# out.sr_approximation()

# out.array_number()

# out.car_distance()

out.ball_falling()