class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, id):
        for observer in self._observers:
            observer.check_id(id)


class Observer():
    def __init__(self, id):
        self._id = id

    def check_id(self, id):
        if self._id == id:
            print("¡Coincidencia encontrada! ID:", id)


# Implementación específica del Observer
class id1(Observer):
    def __init__(self):
        super().__init__("ABCD")


class id2(Observer):
    def __init__(self):
        super().__init__("ACBD")


class id3(Observer):
    def __init__(self):
        super().__init__("ADCB")


class id4(Observer):
    def __init__(self):
        super().__init__("BACD")


# Uso del patrón Observer
subject = Subject()

ID1 = id1()
ID2 = id2()
ID3 = id3()
ID4 = id4()

subject.attach(ID1)
subject.attach(ID2)
subject.attach(ID3)
subject.attach(ID4)


vec = ["ADCB","ERTY","QWER","ABCD","POOO","BACD","ACBD","PATH"]

for id in vec:
    subject.notify(id)

#
#subject.notify("Evento 1")
#
#subject.detach(email_observer)
#
#subject.notify("Evento 2")