# Fleet of Things
# You have the Thing class
# You have the Fleet class
# You have the fleet_of_things.py file
# Download those, use those
# In the fleet_of_things file create a fleet
# Achieve this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch

from fleet import Fleet
from thing import Thing

fleet = Fleet()
things = []
t1 = Thing("Get milk",)
t2 = Thing("remove the obstacles")
t3 = Thing("stand up")
t3.complete()
t4 = Thing("eat lunch")
t4.complete()

things.append(t1)
things.append(t2)
things.append(t3)
things.append(t4)

for thing in things:
    fleet.add(thing)
# Create a fleet of things to have this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch

print(fleet)
