"""
Estimates statistics

A Python program to compute the standard deviation of depth and base-level
estimates and the mean of the northing, easting and depth estimates
 on plateau plots. 

The outputs are placed at the folder 'results'.
The nomenclature is 'plateau_pltX.txt', where
X stands for the area corresponding to the SI plotted.

This code is released from the paper: 
Correct structural index in Euler deconvolution via base-level estimates

The program is under the conditions terms in the file README.txt

authors: Felipe F. Melo, 2019
email: felipe146@hotmail.com
"""

import numpy as np

def plateau(est_plateau,xi,yi,area_plt,SI_vet,name):
    
    results=[]
    
    for i in range (len(est_plateau)):
        estimates=np.stack((xi,yi,est_plateau[i][:,2],est_plateau[i][:,3]),
                           axis=-1)
        
        masked =np.ma.array(estimates,mask=np.repeat(estimates[:,0]<=
                                            area_plt[0],estimates.shape[1]))
        masked = np.ma.array(masked, mask=np.repeat(masked[:,0]>=area_plt[1],
                                                        estimates.shape[1]))
        masked = np.ma.array(masked, mask=np.repeat(masked[:,1]<=area_plt[2],
                                                        estimates.shape[1]))
        masked = np.ma.array(masked, mask=np.repeat(masked[:,1]>=area_plt[3],
                                                        estimates.shape[1]))
        
        stdz=(np.std(masked[:, 2]/1000.))
        stdb=(np.std(masked[:, 3]))
        meanx=(np.mean(masked[:, 0]/1000.))
        meany=(np.mean(masked[:, 1]/1000.))
        meanz=(np.mean(masked[:, 2]/1000.))   
        meanb=(np.mean(masked[:, 3]))   
        results.append([SI_vet[i],stdz,stdb,meanx,meany,meanz,meanb])
        
    output=np.array([(results[i]) for i in range (0,len(SI_vet))])             
    np.savetxt('results/'+str(name)+'.txt',output,fmt='%.3f',\
               header="SI, std z, std b, mean x, mean y, mean z, mean b",
               comments='')              
    return