"""
Synthetic test 1

A Python program to compute a Synthetic test 
Distinct SIs and linear magnetic base level 

This code is released from the paper: 
Correct structural index in Euler deconvolution via base-level estimates

The program is under the conditions terms in the file README.txt

authors: Felipe F. Melo and Valeria C.F. Barbosa, 2019
email: felipe146@hotmail.com, valcris@on.br
"""

"""
Parameters:

Size of the moving data window:    
    winsize - an odd integer number. 
              Ex.: for a moving data window of 5 x 5 grid points -> winsize = 5
                                  
Structural indices used:
    SI_vet - an array that can store any of the four SIs.
             Ex.: to test only the SI = 1 -> SI_vet = [1]
                  to test the four SIs -> SI_vet = [0.01,1,2,3]

The areas to compute the statistics about the mean of the northing,
easting and depth estimates:
    area_cla  - array defining the four vertices of a polygon 
                [south,north,west,east]
"""

import numpy as np
import plot_functions as plt_fc
import euler_python as euler
import estimates_statistics as est_stats

# Input data
data_input=np.loadtxt('input/synthetic_data.dat')
shape = (325, 249)
area = [0,64800, 0, 49800]
xi=data_input[:,0]
yi=data_input[:,1]
zi=data_input[:,2]
data=data_input[:,3]

#Plot input data
plt_fc.plot_input_data(data,xi,yi,zi,shape)
'''
These are the two parameters of our methodology for Euler deconvolution:
window size and the percentage of solutions to keep
'''
#moving data window size
winsize=9
#empty array for multiple SIs
est_plateau=[]
#Define below the SIs to be tested
SI_vet=[1,2,3]
'''
Euler deconvolution for multiple SIs
'''
for SI in (SI_vet):
    plateau=euler.euler_deconv_plt(data,xi,yi,zi,shape,area,SI,winsize)
    est_plateau.append(plateau)         
#Here finishes Euler deconvolution     
'''
Plot Figures 3 and 4 - All depth and base level estimates for all SIs
'''
plt_fc.plot_plateau_xy(est_plateau,xi,yi,zi,shape)
plt_fc.plot_plateau(est_plateau,xi,yi,zi,shape)
''' 
Areas used to get the statistics - Defined after the plateau plot
south,north,west,east
''' 
area_plt1=[15000,65000,33400,36500]
area_plt2=[43200,45200,13800,16000]
area_plt3=[23200,26000,14100,15900]

est_stats.plateau(est_plateau,xi,yi,area_plt1,SI_vet,'plateau_plt1')
est_stats.plateau(est_plateau,xi,yi,area_plt2,SI_vet,'plateau_plt2')
est_stats.plateau(est_plateau,xi,yi,area_plt3,SI_vet,'plateau_plt3')