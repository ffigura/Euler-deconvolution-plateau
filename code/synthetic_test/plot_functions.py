"""
Plot functions 

A Python program to plot the total-field anomaly and the estimates
on classic plot. 

This code plot the figures 1-4 in the folder 'figures'.

Figure 1 - input data. Black polygons define the location of the sources.

Figure 2 - horizontal estimates - x and y. Red polygons define the selected
           plateaus.

Figure 3 - depth estimates for the SI = 1, 2 and 3. Red polygons define the
           selected plateaus.

Figure 4 - base-level estimates for the SI = 1, 2 and 3. Red polygons define
           the selected plateaus.

This code is released from the paper: 
Correct structural index in Euler deconvolution via base-level estimates

The program is under the conditions terms in the file README.txt

authors: Felipe F. Melo, 2019
email: felipe146@hotmail.com
"""

import numpy as np
import matplotlib.pylab as plt
import gc
import matplotlib.patches as patches

#######################################################################

def plot_input_data(data,xi,yi,zi,shape):

    '''
    Plot the input data - Figure 1
    '''
    fig=plt.figure(figsize=(5, 5))
    
    
    ax = plt.subplot(111)
    rect1 = patches.Rectangle((34.900,15),0.2,50,linewidth=1,
                              edgecolor='black',facecolor='none',
                              linestyle='-',zorder=2)
    rect2 = patches.Rectangle((14.800,44.800),0.4,0.4,linewidth=1,
                              edgecolor='black',facecolor='none',
                              linestyle='-',zorder=2)
    rect3 = patches.Rectangle((14.500,24.500),0.5,0.5,linewidth=1,
                              edgecolor='black',facecolor='none',
                              linestyle='-',zorder=2)
    im=plt.contourf(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                   data.reshape(shape), 30, cmap='rainbow')
    ax = plt.gca()
    ax.set_ylabel('Northing (km)', fontsize = 14)
    ax.set_xlabel('Easting (km)', fontsize = 14)
    ax.tick_params(labelsize=13)
    cbar=fig.colorbar(im,pad=0.01,shrink=1)
    cbar.set_label('nT',labelpad=-30,y=-0.04, rotation=0,fontsize=13)
    ax.add_patch(rect1)
    ax.add_patch(rect2)
    ax.add_patch(rect3)
    cbar.ax.tick_params(labelsize=13)
    ax.set_xlim(np.min(yi/1000.),np.max(yi/1000.))
    ax.set_ylim(np.min(xi/1000.),np.max(xi/1000.))
    plt.text(43,35,'P1',color='k', size='large')
    plt.text(15,52,'P2',color='k', size='large')
    plt.text(15,18,'P3',color='k', size='large')
        
    plt.subplots_adjust(wspace=0.15,hspace=0.3)
    
    plt.savefig('figures/FIG1.png', bbox_inches='tight', dpi = 600)
    plt.close('all')
    
    return

def plot_plateau_xy(est_plateau,xi,yi,zi,shape):
    '''
    Plateau plot of horizontal estimates - Figure 5
    '''
    fig=plt.figure(figsize=(13, 5))
    
    
    plt.subplot(1,2,1)  
    
    rect_plt1=patches.Rectangle((33.4,15),3.1,49.8,linewidth=2,
                                edgecolor='crimson',facecolor='none',
                                linestyle='-',zorder=2)
    rect_plt2=patches.Rectangle((13.8,43.2),2.2,2.,linewidth=2,
                                edgecolor='crimson',facecolor='none',
                                linestyle='-',zorder=2)
    rect_plt3=patches.Rectangle((14.1,23.2),1.8,2.2,linewidth=2,
                                edgecolor='crimson',facecolor='none',
                                linestyle='-',zorder=2)
    plt.title("(a)", fontsize = 14, loc='center',y=-0.30)
    im=plt.contourf(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                    est_plateau[2][:,0].reshape(shape)/1000., 30,
                    cmap='terrain_r')
    ax = plt.gca()
    ax.contour(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                  est_plateau[2][:,0].reshape(shape)/1000.,10, colors='k',
                  linestyles='solid')
    ax.set_ylabel('Northing (km)', fontsize = 14)
    ax.set_xlabel('Easting (km)', fontsize = 14)
    ax.tick_params(labelsize=13)
    cbar=fig.colorbar(im,pad=0.01,shrink=1,format='%d') 
    cbar.set_label('$\^x_o $ (km)',labelpad=-9,y=-0.03,rotation=0,fontsize=13)
    cbar.ax.tick_params(labelsize=13)
    ax.set_xlim(np.min(yi/1000.),np.max(yi/1000.))
    ax.set_ylim(np.min(xi/1000.),np.max(xi/1000.))
    ax.add_patch(rect_plt1)
    ax.add_patch(rect_plt2)
    ax.add_patch(rect_plt3)
    plt.text(43,35,'P1',color='k', size='large')
    plt.text(15,52,'P2',color='k', size='large')
    plt.text(15,18,'P3',color='k', size='large')     
    
    plt.subplot(1,2,2)  
    rect_plt1=patches.Rectangle((33.4,15),3.1,49.8,linewidth=2,
                                edgecolor='crimson',facecolor='none',
                                linestyle='-',zorder=2)
    rect_plt2=patches.Rectangle((13.8,43.2),2.2,2.,linewidth=2,
                                edgecolor='crimson',facecolor='none',
                                linestyle='-',zorder=2)
    rect_plt3=patches.Rectangle((14.1,23.2),1.8,2.2,linewidth=2,
                                edgecolor='crimson',facecolor='none',
                                linestyle='-',zorder=2)  
    plt.title("(b)", fontsize = 14, loc='center',y=-0.30)
    im=plt.contourf(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                    est_plateau[2][:,1].reshape(shape)/1000., 30,
                    cmap='terrain_r')
    ax = plt.gca()
    ax.contour(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                  est_plateau[2][:,1].reshape(shape)/1000.,10, colors='k',
                  linestyles='solid')
    ax.set_ylabel('Northing (km)', fontsize = 14)
    ax.set_xlabel('Easting (km)', fontsize = 14)
    ax.tick_params(labelsize=13)
    cbar=fig.colorbar(im,pad=0.01,shrink=1,format='%d') 
    cbar.set_label('$\^y_o $ (km)',labelpad=-9,y=-0.03,rotation=0,fontsize=13)
    cbar.ax.tick_params(labelsize=13)
    ax.set_xlim(np.min(yi/1000.),np.max(yi/1000.))
    ax.set_ylim(np.min(xi/1000.),np.max(xi/1000.))
    ax.add_patch(rect_plt1)
    ax.add_patch(rect_plt2)
    ax.add_patch(rect_plt3)    
    plt.text(43,35,'P1',color='k', size='large')
    plt.text(15,52,'P2',color='k', size='large')
    plt.text(15,18,'P3',color='k', size='large')  
        
    plt.subplots_adjust(wspace=0.15)
        
    plt.savefig('figures/FIG2.png', bbox_inches='tight', dpi = 600)
    plt.close('all')
    gc.collect()
    
    return


def plot_plateau(est_plateau,xi,yi,zi,shape):
    '''
    Plateau plot of the depth and base level estimates for all SIs
    '''
    
    '''
    Figure 3 - Depth estimates
    '''
    vet_title=["(a)","(b)","(c)"]
    
    fig=plt.figure(figsize=(20, 6))
    for i in range (3):
        plt.subplot(1,3,i+1)  
        rect_plt1=patches.Rectangle((33.4,15),3.1,49.8,linewidth=2,
                                    edgecolor='black',facecolor='none',
                                    linestyle='-',zorder=2)
        rect_plt2=patches.Rectangle((13.8,43.2),2.2,2.,linewidth=2,
                                    edgecolor='black',facecolor='none',
                                    linestyle='-',zorder=2)
        rect_plt3=patches.Rectangle((14.1,23.2),1.8,2.2,linewidth=2,
                                    edgecolor='black',facecolor='none',
                                    linestyle='-',zorder=2) 
        
        plt.title(vet_title[i], fontsize = 14, loc='center',y=-0.27)
        im=plt.contourf(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                        est_plateau[i][:,2].reshape(shape)/1000., 30,
                        cmap='terrain_r')
        ax = plt.gca()
        ax.set_ylabel('Northing (km)', fontsize = 14)
        ax.set_xlabel('Easting (km)', fontsize = 14)
        ax.tick_params(labelsize=13)
        cbar=plt.colorbar(im,pad=0.01,
                          shrink=1,format='%.1f') 
        cbar.set_label('$\^z_o $ (km)',labelpad=-11,y=-0.03,rotation=0,
                       fontsize=13)
        cbar.ax.tick_params(labelsize=13)
        ax.set_xlim(np.min(yi/1000.),np.max(yi/1000.))
        ax.set_ylim(np.min(xi/1000.),np.max(xi/1000.))
        ax.add_patch(rect_plt1)
        ax.add_patch(rect_plt2)
        ax.add_patch(rect_plt3)
        plt.text(43,35,'P1',color='k', size='large')
        plt.text(15,52,'P2',color='k', size='large')
        plt.text(15,18,'P3',color='k', size='large')     
        
    plt.subplots_adjust(wspace=0.3,hspace=0.32)
      
    plt.savefig('figures/FIG3.png',bbox_inches='tight', dpi = 600)
    plt.close('all')
    gc.collect()
    
    '''
    Figure 4 - Base-level estimates
    '''
    
    fig=plt.figure(figsize=(20, 6))
    for i in range (3):
        rect_plt1=patches.Rectangle((33.4,15),3.1,49.8,linewidth=2,
                                    edgecolor='black',facecolor='none',
                                    linestyle='-',zorder=2)
        rect_plt2=patches.Rectangle((13.8,43.2),2.2,2.,linewidth=2,
                                    edgecolor='black',facecolor='none',
                                    linestyle='-',zorder=2)
        rect_plt3=patches.Rectangle((14.1,23.2),1.8,2.2,linewidth=2,
                                    edgecolor='black',facecolor='none',
                                    linestyle='-',zorder=2) 
        plt.subplot(1,3,i+1) 
        plt.title(vet_title[i], fontsize = 14, loc='center',
                  y=-0.27)
        im=plt.contourf(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                     est_plateau[i][:,3].reshape(shape), 30, 
                     cmap="rainbow")
        ax=plt.gca()
        ax.set_ylabel('Northing (km)', fontsize = 14)
        ax.set_xlabel('Easting (km)', fontsize = 14)
        ax.tick_params(labelsize=13)
        cbar=plt.colorbar(im,pad=0.01,shrink=1,
                          format='%d')
        cbar.set_label('$\^b$ (nT)',labelpad=-35,y=-0.03, rotation=0,
                       fontsize=13)
        cbar.ax.tick_params(labelsize=13)
        ax.set_xlim(np.min(yi/1000.),np.max(yi/1000.))
        ax.set_ylim(np.min(xi/1000.),np.max(xi/1000.))
        ax.add_patch(rect_plt1)
        ax.add_patch(rect_plt2)
        ax.add_patch(rect_plt3)            
        plt.text(43,35,'P1',color='k', size='large')
        plt.text(15,52,'P2',color='k', size='large')
        plt.text(15,18,'P3',color='k', size='large')  
                        
    plt.subplots_adjust(wspace=0.3,hspace=0.30)
        
    plt.savefig('figures/FIG4.png',bbox_inches='tight', dpi = 600)
    plt.close('all')
    gc.collect()
    
    return