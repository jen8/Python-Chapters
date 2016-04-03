
current_time = int(input("What is the current time?[0-23] "))
wait_hours = int(input("How many hours do you want to wait before your alarm goes off? "))
alarm = (wait_hours % 24) + current_time
print ("Alarm time: " + str(alarm))
  
#put on GitHub? foo3
   
