# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 16:33:48 2019

@author: whypan
"""

import wave 
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as ss

def waveread(filename):
    f = wave.open(filename,"rb")
    params = f.getparams()
    nchannels,samplewidth,framerate,nframes = params[:4]
    str_data = f.readframes(nframes)
    f.close()
    if samplewidth == 2:
        wave_data = np.frombuffer(str_data, dtype=np.int16)
    elif samplewidth == 4:
        wave_data = np.frombuffer(str_data, dtype=np.int32)
    wave_data.shape = -1, nchannels
    return nchannels,samplewidth,framerate,nframes,wave_data

if __name__ == "__main__":
    nchannels,samplewidth,framerate,nframes,wave_data =waveread('C2_3_y.wav')
    x_data = wave_data[:,0]