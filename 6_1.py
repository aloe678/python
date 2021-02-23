import time


class TrafficLight:

    __color = ["red", "yellow", "green"]

    def running(self):
        for i in self.__color:
            if i == "red":
                print("RED")
                time.sleep(7)
            if i == "yellow":
                print("YELLOW")
                time.sleep(2)
            if i == "green":
                print("GREEN")
                time.sleep(8)


start = TrafficLight()
start.running()
