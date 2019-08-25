from pirc522 import RFID
from time import sleep

from lifxlan import LifxLAN

rdr = RFID()
util = rdr.util()

util.debug = True

DEFAULT_KEY = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

with open('./.keys') as fyl:
  keyA = tuple([x for x in bytearray(fyl.readline().strip().decode('hex'))])
  keyB = tuple([x for x in bytearray(fyl.readline().strip().decode('hex'))])




while True:
  # Wait for tag
    rdr.wait_for_tag()

    # Request tag
    (error, data) = rdr.request()
    if not error:
      (error, uid) = rdr.anticoll()
      if not error:
        print(uid)
        if (uid == [43,107,171,33,202]):
          