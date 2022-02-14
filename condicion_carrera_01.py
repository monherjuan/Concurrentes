from threading import Thread, Semaphore
import random
import time


class general():
    def __init__(self, conta=0):
        self.semaphoreleer = Semaphore(0)
        self.semaphorellenar = Semaphore(0)
        self.vector = []
        self.conta = conta

    def llenarVector(self):

        if len(self.vector) > 0:
            self.semaphorellenar.acquire()
        else:
            
            self.conta += 1
            self.vector.append(self.conta)
            print("Entra : llenar Vector V=", len(self.vector))
            self.semaphoreleer.release()

    def leerVector(self):

        if len(self.vector) == 0:
            print("Entra : leer Vector en 0")
            self.semaphorellenar.release()
            self.semaphoreleer.acquire()

        else:
            # self.semaphorellenar.acquire()
            print("Entra : leer Vector +1")
            print(self.vector)
            self.vector.pop()
            self.semaphorellenar.release()


def func_conta(x):
    for y in range(13):
        time_f = random.random()
        time.sleep(time_f)
        x.leerVector()


def funci(x):
    for y in range(13):
        time_f = random.random()
        time.sleep(time_f)
        x.llenarVector()


if __name__ == "__main__":
    General = general()
    tstar1 = Thread(target=funci, args=(General, ))
    tstar = Thread(target=func_conta, args=((General, )))
    tstar.start()
    tstar1.start()





# import threading
# import time
# import random


# class General():

#     def __init__(self, conta=0):
#         self.Leer = threading.Lock()
#         self.Llenar = threading.Lock()
#         self.vector = []
#         self.conta = conta

#     def llenarVector(self):
#         self.Leer.acquire()

#         print("Entra : llenar Vector")
#         self.conta += 1
#         self.vector.append(self.conta)
#         # self.Llenar.acquire()
#         self.Leer.release()


#     def leerVector(self):

#         if len(self.vector) == 0:
#             print("Entra : leer Vector en 0")
#             # self.Llenar.release()
#             self.Llenar.acquire()

#         else:
#             # self.Llenar.acquire()
#             print("Entra : leer Vector +1")
#             print(self.vector)
#             self.vector.pop()
#             self.Llenar.release()


# def func_conta(x):
#     for y in range(4):
#         time_f = random.random()
#         time.sleep(time_f)
#         x.leerVector()

# def funci(x):
#     for y in range(4):
#         time_f = random.random()
#         time.sleep(time_f)
#         x.llenarVector()


# if __name__ == "__main__":
#     general = General()
#     for y in range(2):
#         tstar = threading.Thread(target=func_conta, args=((general, )))
#         tstar1 = threading.Thread(target = funci,args = (general, ))
#         tstar.start()
#         tstar1.start()
