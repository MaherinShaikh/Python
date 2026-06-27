# Greeting according to timestamp

import time

timestamp = time.strftime("%H:%M:%S")
print("Current time:", timestamp)
hour = int(time.strftime("%H"))
if hour < 12:
    print("Good morning!")
elif hour < 18:
    print("Good afternoon!")        
else:    print("Good evening!") 
