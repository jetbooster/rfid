from lifxlan import LifxLAN

class Lifx(LifxLAN):
  def __init__(self,*args,**kwargs):
    super().__init__(args, kwargs)

    self.bulb = self.getLights()[0]

    
  def toggle_power(self):
      original_power_state = self.bulb.get_power()
      self.bulb.set_power("on" if original_power_state==0 else "off")

lifx = Lifx(1)
lifx.toggle_power()