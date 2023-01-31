import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Colormap
import scipy.io
# from PyEMD import EMD
import emd

data = {}
for i in range(1, 5):
    data = scipy.io.loadmat('L ({}).mat'.format(i))
    m=data['A']
    imfs = emd.sift.sift( m )
    s=imfs[:,2]
    









    # fig = plt.figure()
    # plt.plot(imf)
    
    
    
    
    
    
    
    # N = imf.shape[0]+1
    # plt.subplot(N,1,1)
    # plt.plot(m, 'r')
    # plt.title("Input signal")
    # plt.xlabel("Time [s]")
    # for n, imf in enumerate(imf):
    #     plt.subplot(N,1,n+2)
    #     plt.plot( imf, 'g')
    #     plt.title("IMF "+str(n+1))
    # #     plt.xlabel("Time [s]")
    # # plt.tight_layout()
    # # plt.savefig('simple_example')
    # # plt.show()
    
    


    

    
    
    
    
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''
fs=1000;
for i in range(1,501):
    mat = scipy.io.loadmat('L (%d).mat')
    m=mat['A']

'''




    
'''
mat = scipy.io.loadmat('L (1).mat')
m=mat['A']
fig = plt.figure()
plt.plot(m)
'''

