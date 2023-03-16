#THIS IS FOR CREATING EXAMPLE TIMESTAMPS FOR TESTING 
import time
import random 

times_ran = 0
f = open('Speedometer/timestamps.csv','w')




# CONTROL CENTER #

#How many times the loop runs, This is how many values you will have
num_of_interactions = 10

#This is the variation between the two speeds
first_speed = 1
second_speed = 2



for _ in range(0, num_of_interactions):

	current_time = round(time.time() * 1000)
	f.write(str(current_time))
	f.write('\n')

	#This is how long between each timestamp, determining speed
	speed = random.randint(first_speed, second_speed)
	time.sleep(speed)


	times_ran = times_ran + 1
	progress = num_of_interactions - times_ran
	print('time left: ' + str(progress))

f.close()
