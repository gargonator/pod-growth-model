# Import statements

import math
import random


# Input variables

startingPods = 10
signupFraction = 0.4
matureFraction = 1 - signupFraction
newDBCPU = 0.10 # additional DBU usage from new orgs sign-ups each month
maxThreshold = 0.55 # utilization at which pod requires modification
timescale = 36 # months that the simulation runs for
migratedCapacity = .012 # capacity that is migrated off of the pod
signupThreshold = 0.3  # DB CPU percentage where sign-up pod becomes a mature pod
growthRates = {"sign-up":0.02, "mid-stage":0.015, "mature":0.012} # DB CPU absolute growth per month

mode = "Split" # Split or Migration modes
split_signup = "Yes" # Do new sign-ups go into split pods

def createPods():
	# determine number of signup pods and mature pods
	numSignups = math.floor(signupFraction*startingPods)
	numMature = math.ceil(matureFraction*startingPods)
	
	# create lists of pod names, pod types, and starting DB CPUs
	podNames = ["Pod " + str(x) for x in range(0,startingPods)]
	podTypes = []
	podStartingDBCPU = []
	
	# populate pod type and DB CPU lists
	for pod in range(1,startingPods + 1):
		if pod < numSignups:
			podTypes.append["sign-up"]
			podStartingDBCPU.append[uniform(0,signupThreshold)]
		else:
			podTypes.append["mature"]
			podStartingDBCPU.append[uniform(signupThreshold,maxThreshold)]
			
			
	return dict(zip(podNames,podTypes,podStartingDBCPU)


	
		
		
		

'''
def growthRate(dbCPU):
	dbGrowth = []
	for k in range(0,len(dbCPU))
		if dbCPU >= 0 && dbCPU < 0.15:
			if 
		
		
		


