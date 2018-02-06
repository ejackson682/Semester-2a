import time

def HelloAndGoodbye(personName, secsToWait):
    print ("Hello, " + personName)
    time.sleep(secsToWait)
    print ("Goodbye, " + personName)
HelloAndGoodbye("Mario" , 10)
HelloAndGoodbye("Steve" , 23) 
