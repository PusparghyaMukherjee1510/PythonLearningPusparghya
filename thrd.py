from threading import *
# def sjkl():
#     print("child")
# t=Thread(target=sjkl())
# t.start()
# print("parent")

# class Mythread(Thread):
#     def run(self):
#         for i in range(5):
#             print("Child")


# r=Mythread()
# r.start()
# for i in range(5):
#     print("parent")

# class Demj():
#     def show(self):
#         for i in range(5):
#             print("Child")
# opu=Demj()
# t=Thread(target=opu.show())
# t.start()
# for i in range(5):
#     print('Main')

#Multithreading
import time
class Demo:
    def numbr(self):
        for i in range(1,6):
            print(i)
            time.sleep(1)
    def numbrdbl(self):
        for i in range(1,6):
            print("double is: ",i*2)
            time.sleep(1)
    def numbrsqr(self):
        for i in range(1,6):
            print("square is: ",i*i)
            time.sleep(1)

obg=Demo()
t1=Thread(target=obg.numbr)
t2=Thread(target=obg.numbrdbl)
t3=Thread(target=obg.numbrsqr)

t1.start()
time.sleep(0.2)
t2.start()
time.sleep(0.2)
t3.start()
time.sleep(0.2)

t1.join()
t2.join()
t3.join()

print("Main Thread")