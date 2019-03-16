# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 16:33:48 2019

@author: whypan
"""

import wave
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as ss
import math


def waveread(filename):
    f = wave.open(filename, "rb")
    params = f.getparams()
    nchannels, samplewidth, framerate, nframes = params[:4]
    str_data = f.readframes(nframes)
    f.close()
    if samplewidth == 2:
        wave_data = np.frombuffer(str_data, dtype=np.int16)
    elif samplewidth == 4:
        wave_data = np.frombuffer(str_data, dtype=np.int32)
    wave_data.shape = -1, nchannels
    return nchannels, samplewidth, framerate, nframes, wave_data

def splcal(x,fs,flen):
    length = len(x)
    M = int(flen*fs/1000)
#    print(length,M)
    if length!= M:
        print("输入信号长度与帧长不等")
    pa = np.sum(np.square(x.astype(np.float64)))/M
    pa = pa**0.5
#    print(pa)
    pp = 2*(10**(-5))
    spl = 20*(math.log10(pa/pp))
    return spl
    

if __name__ == "__main__":
    nchannels, samplewidth, framerate, nframes, wave_data = waveread('C2_3_y.wav')
#    wave_data = wave_data/np.max(abs(wave_data))   
    wave_data = wave_data/32768
    x_data = wave_data[:, 0]
    x = x_data.T
    length = len(x)   
#    计算声压值帧长
# % 每帧大小为M，当语音长度不是帧长的整数倍时：
# % (1)若剩余长度大于等于帧长的二分之一，则补零至帧长
# % (2)若剩余长度小于帧长的二分之一，则舍弃
    framlen = 100
    fm = int(framerate*framlen /1000)
    m = int(length % fm)
    if m > fm/2:
        b = np.frombuffer(np.zeros(fm-m), dtype=np.int16)
        x= np.concatenate((x,b))
        length = len(x)
#        print(length)
    else:
        l = x[:-m]
        
        
    N = int(length/fm)
    s = np.zeros((1,fm))
    spll = np.zeros((1,N))
    for k in range(N):
        k = k+1
#        print(k,fm)
        s = x[(k-1)*fm:k*fm] 
        spll[0,k-1] = np.array(splcal(s,framerate,framlen))
#        print(spll)
    t = np.arange(length)
    tt = np.arange(N)
    spll = spll.T
    plt.figure()
    plt.subplot(2,1,1)
    plt.plot(t/framerate,x)
    plt.subplot(2,1,2)
    plt.step(tt/10,spll,'r')
    plt.show()
        
#    
        
        
#        