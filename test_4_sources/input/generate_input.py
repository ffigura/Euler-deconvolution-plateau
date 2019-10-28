# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 19:54:37 2019

@author: Felipe
"""

import numpy as np
from fatiando.gravmag import prism
from fatiando import mesher, gridder, utils

# Make some synthetic magnetic data to test our Euler deconvolution.
# The regional field
inc, dec = 60, -20
# Make a model of two spheres magnetized by induction only

#ordem dos prismas -> SI 3, 2,1,0

model = [
    mesher.Prism(6850,7250, 11850,12250, 850, 1250,
                  {'magnetization': utils.ang2vec(25, inc, dec)}),
    mesher.Prism(15850,16150, 11850,12150, 600, 1000000,
                  {'magnetization': utils.ang2vec(10, inc, dec)}),
    mesher.Prism(10000,200000, 21850,22150, 600, 1000000,
                  {'magnetization': utils.ang2vec(2, inc, dec)}),
    mesher.Prism(-200000,200000, -200000,2000, 200, 1000000,
                  {'magnetization': utils.ang2vec(0.3, inc, dec)})]   

# Generate some magnetic data from the model
shape = (120, 140)
area = [0, 24000, 0, 28000]
hvoo=-100
xi, yi, zi = gridder.regular(area, shape, z=hvoo)

data = utils.contaminate(prism.tf(xi, yi, zi, model, inc, dec),0.001,
                       percent=True)
'''
out=np.array([xi,yi,zi,data])        
out=out.T.astype(np.float)
np.savetxt('noise_synthetic_data.dat',out,delimiter=' ',fmt='%1.3f')
out=[]
'''
#linear base-level
b=50
data_cont=data+b

out=np.array([xi,yi,zi,data_cont])        
out=out.T.astype(np.float)
np.savetxt('synthetic_data.dat',out,delimiter=' ',fmt='%1.3f')