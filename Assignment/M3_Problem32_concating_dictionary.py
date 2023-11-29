d1={'k1':1,'k2':2,'k3':5}
d2={'k4':4,'k5':6,'k6':7}
d3=dict(d1)   # storing first dictionary in temp dictionary
d3.update(d2) # using update to add second dictionary to temp dictionary

print(d3)
