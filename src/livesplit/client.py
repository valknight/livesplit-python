import socket
from sys import getfilesystemencodeerrors
from typing import ByteString


class Livesplit():
    def __init__(self, ip="127.0.0.1", port: int = 16834, reset: bool = False, setupGameTimer=None):
        if setupGameTimer is None:
            setupGameTimer = reset
        self.ip = ip
        self.port = port
        if reset:
            self.reset()
        if setupGameTimer:
            self.setupGameTimer()

    def setupGameTimer(self):
        self.initGameTimer()
        self.pauseGameTimer()

    def sendCommand(self, command: str):
        m = "{}\r\n".format(command)
        self.getSocket().send(str.encode(m))

    def pauseGameTimer(self):
        self.sendCommand("pausegametime")

    def startGameTimer(self):
        self.sendCommand("unpausegametime")

    def initGameTimer(self):
        self.sendCommand("initgametime")

    def startTimer(self):
        self.sendCommand("starttimer")

    def startOrSplit(self):
        self.sendCommand("startorsplit")

    def split(self):
        self.sendCommand("split")

    def unsplit(self):
        self.sendCommand("unsplit")

    def skipSplit(self):
        self.sendCommand("skipsplit")

    def pause(self):
        self.sendCommand("pause")

    def resume(self):
        self.sendCommand("resume")

    def reset(self):
        self.sendCommand("reset")

    def getSocket(self) -> socket.socket:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        return s


if __name__ == '__main__':
    import time
    l = Livesplit()

    l.startOrSplit()
    l.startGameTimer()
    time.sleep(0.5)
    l.pauseGameTimer()
    time.sleep(0.5)
    l.startGameTimer()
    time.sleep(0.5)
    l.pauseGameTimer()
    time.sleep(0.5)
    l.startGameTimer()
    l.pause()
