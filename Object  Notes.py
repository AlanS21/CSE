class Laptop(object):
    def __init__(self, screen_resolution, extra_space, colour):
        # Things that a laptop has.
        # Everything in this list should be relevant to the program
        self.processor = "Intel i5"
        self.screen_resolution = screen_resolution
        self.battery_left = 100
        self.space_left = extra_space
        self.color = colour
        self.os = "Linux"

     def charge(self, time):
         # Charge is already charged
         if self.battery_left >= 100:
             print("The computer is already charged.")
             return

             self.battery_left += time
         # Computer is mostly charged
         if self.battery_left > 100:
             print("The computer completely charges.")

         # Computer is not charged at all
         else:
             print("The computer is now at %d%%" % self.battery_left)
