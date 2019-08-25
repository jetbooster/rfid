from pirc522 import RFID
from time import sleep

from lifxControl import Lifx

class RfidListener:
  def __init__(self, debug=False):
    self.lifx = Lifx(1)
    self.rdr = RFID()
    self.util = self.rdr.util()
    self.util.debug = debug
    self.DEFAULT_KEY = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
    with open('./.keys') as fyl:
      line1 = fyl.readline().strip()
      line2 = fyl.readline().strip()
      self.keyA = tuple([x for x in bytes.fromhex(line1)])
      self.keyB = tuple([x for x in bytes.fromhex(line2)])
  def listen(self):
    while True:
      # Wait for tag
        self.rdr.wait_for_tag()

        # Request tag
        (error, data) = self.rdr.request()
        if not error:
          (error, uid) = self.rdr.anticoll()
          if not error:
            print(uid)
            if (uid == [43,107,171,33,202]):
              self.lifx.toggle_power()
            sleep(2)


if __name__ == "__main__":
  RfidListener().listen()      