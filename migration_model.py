# Import statements

import math
import random
import sys
import numpy as np
import matplotlib.pyplot as plt


# Input variables

startingPods = 20
signupFraction = 0.4
matureFraction = 1 - signupFraction
newDBCPU = 0.05 # additional DBU usage from new orgs sign-ups each month
maxThreshold = 0.55 # utilization at which pod requires modification
timescale = 36 # months that the simulation runs for
migratedCapacity = .012 # capacity that is migrated off of the pod
signupThreshold = 0.3  # DB CPU percentage where sign-up pod becomes a mature pod
# growthRates = {"sign-up":0.02, "mid-stage":0.015, "mature":0.012} # DB CPU absolute growth per month

mode = "Split" # Split or Migration modes
split_signup = "Yes" # Do new sign-ups go into split pods

pods = {} # dictionary of pod names, pod types, and db cpus

def createPods():
  # determine number of signup pods and mature pods
  numSignups = math.floor(signupFraction*startingPods)
  numMature = math.ceil(matureFraction*startingPods)
  
  # create lists of pod names, pod types, and starting DB CPUs
  podNames = ["Pod " + str(x) for x in range(0,startingPods)]
  podTypes = []
  podStartingDBCPU = []
  
  # dictionary of pod names, pod types, starting DB CPU
  pods = {}
  
  # populate pod type and DB CPU lists
  for pod in range(1,startingPods + 1):
    if pod < numSignups:
      podTypes.append("sign-up")
      podStartingDBCPU.append(random.uniform(0,signupThreshold))
    else:
      podTypes.append("mature")
      podStartingDBCPU.append(random.uniform(signupThreshold,maxThreshold))
  
  for tuple in zip(podNames,podTypes,podStartingDBCPU):
    pods.update({tuple[0]:[tuple[1],tuple[2]]})
  
  return pods
  
def growthRate(dbCPU):
    if (dbCPU >= 0) and (dbCPU <= 0.15):
      return 0.02
    elif dbCPU <= 0.40:
      return 0.015
    else:
      return 0.012


def simulate():
  
  # create the initial pods
  pods = createPods()
  
  # dictionary for new pods
  newpods = {}
  
  # calculate initial average utilization
  print "The initial mean is", np.mean([pods[value][1] for value in pods])
  
  # initialize a list of average utilizations
  utilization = [np.mean([pods[value][1] for value in pods])]
  
  # initialize a list of pod counts
  counts = [startingPods]
  
  # model the growth
  for t in range(1,timescale+1):
    
    for name in pods:
      
      if pods[name][0] == "sign-up":
        pods[name][1] += newDBCPU # new DBCPU from new org sign-ups
        pods[name][1] += growthRate(pods[name][1]) # new DBCPU from seat growth
      
      if pods[name][0] == "mature":
        pods[name][1] += growthRate(pods[name][1])
        if pods[name][1] > maxThreshold: # check if the pod should split
          if mode == "Split":
            pods[name][1] /= 2.0
            pods[name][0] == "split"
            newpods.update({"Pod" + str(counts[t-1]+1):["split",pods[name][1]]})
      
      if pods[name][0] == "split":
        if split_signup == "Yes":
          pods[name][1] += newDBCPU
        pods[name][1] += growthRate(pods[name][1])
        if pods[name][1] > maxThreshold: # check if the pod should split
          if mode == "Split":
            pods[name][1] /= 2.0
            newpods.update({"Pod" + str(counts[t-1]+1):["split",pods[name][1]]})
   
      if  pods[name][1] > signupThreshold and pods[name][0] == "sign-up":
        pods[name][0] = "mature"
    
    pods.update(newpods)
    
    counts.append(len(pods))
    utilization.append(np.mean([pods[value][1] for value in pods]))
    
  return pods, counts, utilization

 
 
for k in range(0,11):

  pods,counts,utilization = simulate()  

  # plotting the results
  x = np.arange(0,timescale+1)
  y1 = counts
  y2 = utilization

  plt.figure(1)
  plt.plot(x,y1,'b-')

  plt.figure(2)
  plt.title("Average DB CPU %")
  plt.plot(x,y2,'b-')

  
plt.show()
