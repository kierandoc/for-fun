import time 

john_doing_his_job = False
seconds = 0
minutes = 0
minute_count = 0 
while john_doing_his_job is not True:
    seconds +=1
    minute_count+= 1 
    time.sleep(1)
    print('john has not done his job in :' + str(minutes) + ' minutes; ' + str(seconds) + ' seconds.' )
    
    if minute_count >= 59:
        minutes += 1
        minute_count = 0
        seconds = 0
    
    if minutes == 5:
        print("John is staring of into space questioning his life decisions.")
    
    if minutes == 10:
        print("John is day dreamig about going outside and using his vape")
    
    if minutes == 15:
        print('John is deppressing me with how long he is taking to start the lesson')
    
    if minutes == 20:
        print("John realises that literally anything else would be a better use of our time")
    
    if minutes == 30:
        print("I am now rethinking my whole life, thank's john")
    
    if minutes == 60:
        print("i want to fucking kill myself")
