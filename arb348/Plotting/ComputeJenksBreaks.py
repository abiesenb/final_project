'''
Module that computes the Jenks breaks, used in the heatmap chart.

NOTE: The code written below for Natural_Breaks class and the natural_breaks 
function are part of the pysal.esda.mapclassify  release, and were not written 
by me. I needed to add them explicitly here (as opposed to just importing 
them) because I wanted to remove some automatic print statements that the 
function produces when the number of observations is small. 

Created on Apr 11, 2015
@author: Adam Biesenbach
'''
from pysal.esda.mapclassify import Map_Classifier
import pandas as pd
import numpy as np 

def ComputeJenksBreaks(df_map):
    '''This module calculates the Jenks natural breaks for density. We'll use these in
    creating out heatmap charts later on.'''

    breaks = Natural_Breaks(df_map[df_map['density_km'].notnull()].density_km.values, k=5)
    #the notnull method lets us match indices when joining.
    jb = pd.DataFrame({'jenks_bins': breaks.yb}, index=df_map[df_map['density_km'].notnull()].index)
    df_map = df_map.join(jb)
    df_map.jenks_bins.fillna(-1, inplace=True)
    
    jenks_labels = ["<= %0.1f/km$^2$(%s Communities)" % (b, c) for b, c in zip(breaks.bins, breaks.counts)]
    jenks_labels.insert(0, 'No complaints (%s \n Communities)' % len(df_map[df_map['density_km'].isnull()]))          

    return (breaks, df_map, jenks_labels)

class Natural_Breaks(Map_Classifier):
    """
    Natural Breaks Map Classification

    Parameters
    ----------
    y       : array (n,1)
              values to classify
    k       : int
              number of classes required
    initial : int (default=100)
              number of initial solutions to generate

    Attributes
    ----------

    yb      : array (n,1)
              bin ids for observations,
    bins    : array (k,1)
              the upper bounds of each class 
    k       : int
              the number of classes
    counts  : array (k,1)
              the number of observations falling in each class

    """
    def __init__(self,y,k=5,initial=100):
        self.k=k
        self.initial=initial
        Map_Classifier.__init__(self,y)
        self.name='Natural_Breaks'
        
    def _set_bins(self):

        x=self.y.copy()
        k=self.k
        res0=natural_breaks(x,k)
        fit=res0[2].sum()
        for i in xrange(self.initial):
            res=natural_breaks(x,k)
            fit_i=res[2].sum()
            if fit_i< fit:
                res0=res
        self.bins=res0[-1]
        self.k=len(self.bins)
        self.iterations=res0[-2]
    
def natural_breaks(values, k=5, itmax=100):
    """
    natural breaks helper function
    """
    values = np.array(values)
    n = len(values)
    uv = np.unique(values)
    uvk = len(uv)
    if  uvk < k:
        k = uvk
    sids = np.random.permutation(range(len(uv)))[0:k]
    seeds = uv[sids]
    seeds.sort()
    diffs = abs(np.matrix([values - seed for seed in seeds]))
    c0 = diffs.argmin(axis=0)
    c0 = np.array(c0)[0]
    solving = True
    solved = False
    rk = range(k)
    it = 0
    while solving:
        # get centroids of clusters
        seeds = [np.median(values[c0 == c]) for c in rk]
        seeds.sort()
        # for each value find closest centroid
        diffs = abs(np.matrix([values - seed for seed in seeds]))
        # assign value to that centroid
        c1 = diffs.argmin(axis=0)
        c1 = np.array(c1)[0]
        #compare new classids to previous
        d = abs(c1 - c0)
        if d.sum() == 0:
            solving = False
            solved = True
        else:
            c0 = c1
        it += 1
        if it == itmax:
            solving = False
    class_ids = c1
    cuts = [max(values[c1 == c]) for c in rk]
    return sids, seeds, diffs, class_ids, solved, it, cuts