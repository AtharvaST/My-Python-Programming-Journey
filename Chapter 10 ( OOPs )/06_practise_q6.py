from random import randint


class train :

    def __init__(self,trainNo):
        self.trainNo=trainNo

    def book(self, fro, to):
        print(f"Ticket is booked for Train no : {self.trainNo}  from {fro} to {to}\n Happy Journey !!!! ")

    def getStatus(self, trainNo):
        print(f"Train no {self.trainNo} is running on time. ")
        

    def getFair(self , trainNo, fro, to):
        print(f"Ticket fare for Train no : {self.trainNo}  from {fro} to {to} is {randint(666,5000)}")

t = train(12399)
t.getFair(12399,"mumbai" , "Ambala")
t.book("Mumbai" , "Ambala")
t.getStatus(12399)



        