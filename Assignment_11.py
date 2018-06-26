#Question 1
import threading
import time
class mythread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

for i in range(5):
    time.sleep(5)
    thread1=mythread()
    thread1.start()
    print("Hello.!! How are you..?")

#Question 2

import threading
import time

class mythread(threading.Thread):

    def __init__(self, i):
        self.i = i
        threading.Thread.__init__(self)

    def run(self):
        print (self.i)

for i in range(1,11):
    time.sleep(1)
    mythread(i).start()


#Question 3

import threading
import time
import math

class Threads(threading.Thread):
    def __init__(self,list1):
        threading.Thread.__init__(self)
        self.list1=list1
    def run(self):
        count =0
        for i in self.list1:
          count+=2
          time.sleep(count)
          print(i)

list1=[]
n=int(input("Enter total number of elements: "))
for i in range(n):
    j=input("enter elements: ")
    list1.append(j)

t=Threads(list1)
t.start()



#Question 4

import threading
import time
import math

class Factorial(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.f=f
    def run(self):
        print("Factorial of ",self.f,"is",math.factorial(self.f))
f=int(input("Enter a number: "))
f1=Factorial(f)
f1.start()





