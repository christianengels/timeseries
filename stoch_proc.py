# FLAME Copyright 2014 The University of Texas at Austin
#
# For FLAME licensing information see
#                http://www.cs.utexas.edu/users/flame/license.html
#
# Programmed by: Christian Engels
#                engels.chr@gmail.com

import flame
import numpy as np
import pylab as pl

def ar(first, mu, alpha, x):

    xT, \
    xB  = flame.part_2x1(x, \
                         0, 'TOP')

    last = first
    
    while xT.shape[0] < x.shape[0]:

        x0,   \
        chi1, \
        x2    = flame.repart_2x1_to_3x1(xT, \
                                        xB, \
                                        1, 'BOTTOM')

        #------------------------------------------------------------#
	chi1 = mu + alpha * last + chi1
        last = chi1
        #------------------------------------------------------------#

        xT, \
        xB  = flame.cont_with_3x1_to_2x1(x0,   \
                                         chi1, \
                                         x2,   \
                                         'TOP')

    flame.merge_2x1(xT, \
                    xB, x)


def sp(length, first=0, mu=0, alpha=1, std=1):

    x = std * np.random.randn(length-1, 1)
    
    ar(first, mu, alpha, x)
    
    first = np.array([first])
    
    x = np.append(first, x).reshape(length, 1)
    
    return x


def sp_many(length, rep=10, first=0, mu=0, alpha=1, std=1):
    
    for i in range(rep):

        x = sp(length, first, mu, alpha, std)

        pl.plot(x)

    pl.show()


def rtot(x):

    xT, \
    xB  = flame.part_2x1(x, \
                         0, 'TOP')

    sum = 0.0

    while xT.shape[0] < x.shape[0]:

        x0,   \
        chi1, \
        x2    = flame.repart_2x1_to_3x1(xT, \
                                        xB, \
                                        1, 'BOTTOM')

        #------------------------------------------------------------#
        chi1 += sum
        sum = chi1
        #------------------------------------------------------------#

        xT, \
        xB  = flame.cont_with_3x1_to_2x1(x0,   \
                                         chi1, \
                                         x2,   \
                                         'TOP')

    flame.merge_2x1(xT, \
                    xB, x)

def rmean(x):

    m, n = np.shape(x)

    rtot(x)

    x = x * (1.0 * np.arange(1, (m+1)).reshape(m, 1))     
    
    
 
 