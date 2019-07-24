class car:
  def __init__(self, regno, no_gears):
      self.regno = regno
      self.no_gears = no_gears
      self.is_started = False
      self.gear = 0
  def start(self):
        if self.is_started:
             print(f"{self.regno} car is already started")
        else: 
             print(f"{self.regno} car is  started")


  def change_gear(self):
    if self.is_started:
         if self.change_gear< self.no_gears
             print(f"car with regno:{self.regno}")
  def stop(self):
        if self.is_started:
              print(f"car with regno{self.regno} changed the gear")
              self.is_started = False
        else:
             print(f"car with regno{self.regno} car is stopped")


