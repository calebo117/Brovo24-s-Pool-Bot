
#Class definition for a betting pool
class pool:

  def __init__(self, name, startingValue):
    self.name = name
    self.currentValue = startingValue

  def addValue(self, value):
    self.currentValue = (self.currentValue + value)

  def getValue(self):
    return self.currentValue

  def getName(self):
    return self.name
