import sys
import random

class Pod:

  def __init__(self,name="",type="",dbcpu=0):
    self.name = name
    self.dbcpu = dbcpu
    self.type = type
    
  def set_dbcpu(self,min,max):
    self.dbcpu = random.uniform(min,max)
  
  def get_dbcpu(self):
    return self.dbcpu
    
  
  
