from pirc522 import RFID
from time import sleep

rdr = RFID()
util = rdr.util()

util.debug = True

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
        util.auth(rdr.auth_b, [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF])
        rdr.write(11, [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00])
        util.dump()
        sleep(2)