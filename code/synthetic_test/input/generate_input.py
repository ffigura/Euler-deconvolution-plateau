# -*- coding: utf-8 -*-
"""
A Python program to generate the total field anomaly of the sources 1, 2 and 3
on the first synthetic test. 

This code is released from the paper: 
Correct structural index in Euler deconvolution via base-level estimates

The program is under the conditions terms in the file README.txt

authors: Felipe F. Melo, 2019
email: felipe146@hotmail.com

"""

import numpy as np
from fatiando.gravmag import prism
from fatiando import mesher, gridder, utils

# Make some synthetic magnetic data to test our Euler deconvolution.
# The regional field
inc, dec = 59, 10

#order of the prism -> SI 3, 2,1
#needed to increase the intensity of magnetization of some sources because
#they were modeled as spheres to the paper and now they are modeled as prisms

model = [
    mesher.Prism(24500,25500, 14500,15500, 1000, 2000,
                  {'magnetization': utils.ang2vec(3, 9, -32)}),
    mesher.Prism(44800,45200, 14800,15200, 2000, 1000000,
                  {'magnetization': utils.ang2vec(12, inc, dec)}),
    mesher.Prism(15000,94000,34900,35100, 1800, 3000e3,
                  {'magnetization': utils.ang2vec(5, inc, dec)})]
# Generate some magnetic data from the model
shape = (325, 249)
area = [0,64800, 0, 49800]
hvoo=0
xi, yi, zi = gridder.regular(area, shape, z=hvoo)

data = utils.contaminate(prism.tf(xi, yi, zi, model, inc, dec),0.1, seed=0)

#linear base-level
b=47500
data_cont=data+b

out=np.array([xi,yi,zi,data_cont])        
out=out.T.astype(np.float)
np.savetxt('synthetic_data.dat',out,delimiter=' ',fmt='%1.3f')

