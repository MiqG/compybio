# classes for modeling
# load libraries
import pandas as pd
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

class StoichMat:
    """operations with stoichiometric matrices"""
    # plot results
    def plotSolODE(self, t, y, xlab='time',
                   ylab='y(t)',labels=None):
        # init
        if labels is None:
            labels=np.arange(y.shape[1])
        # make lines and label them accordingly
        for i in range(y.shape[1]):
            plt.plot(t,y[:,i],label=labels[i])
        # display
        plt.xlabel(xlab)
        plt.ylabel(ylab)
        plt.title('ODE solution')
        plt.legend()
        plt.show()


    # functions
    def getSign(self, mat):
        # init output
        outmat = np.zeros(mat.shape)

        # mask positive and negative values
        idxpos = mat > 0
        idxneg = mat < 0

        # substitute accordingly
        outmat[idxpos] = 1
        outmat[idxneg] = -1

        return outmat

    def getAlphas(self, mat):
        outmat = mat.copy()
        # mask positive and negative values
        idxpos = outmat > 0
        idxneg = outmat < 0

        # substitute accordingly
        outmat[idxpos] = 0
        outmat[idxneg] = np.abs(outmat[idxneg])

        return outmat

    def getVelocitiy(self, mat, ratesvec, conc):
        # indicate whether a compund is a substrate/product (-1/1) within each reaction
        rxsigns = self.getSign(mat)
        # get substrates coefficients
        rxalphas = self.getAlphas(mat)
        # compute velocities
        velocities = ratesvec.T * np.prod(conc**rxalphas,axis=0)

        return velocities.T


    def computeODE(self, conc, t, mat, ratesvec):
        dconc = self.getSign(mat).dot(self.getVelocitiy(mat,ratesvec,conc.reshape(conc.shape[0],1)))
        return dconc.reshape(dconc.shape[0],)