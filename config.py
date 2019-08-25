from pirc522 import RFID
from time import sleep

rdr = RFID()
util = rdr.util()

util.debug = True

DEFAULT_KEY = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

with open('./.keys') as fyl:
  keyA = [hex(x) for x in bytearray(fyl.readline().strip().decode('hex'))]
  keyB = [hex(x) for x in bytearray(fyl.readline().strip().decode('hex'))]


while True:
  # Wait for tag
    rdr.wait_for_tag()

    # Request tag
    (error, data) = rdr.request()
    if not error:
      (error, uid) = rdr.anticoll()
      if not error:
        print("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
        util.set_tag(uid)
        util.auth(rdr.auth_b, DEFAULT_KEY)
        for i in range(1,15):
          util.write_trailer(i, key_a=keyA, key_b=keyB)
        util.dump()
        sleep(2)



