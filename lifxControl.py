from lifxlan import LifxLAN

class Lifx():
  def __init__(self, num_lights):
    self.lifx=LifxLAN(1)

    self.bulb = self.lifx.get_lights()[0]

    
  def toggle_power(self):
      original_power_state = self.bulb.get_power()
      self.bulb.set_power("on" if original_power_state==0 else "off")

lifx = Lifx(1)
lifx.toggle_power()