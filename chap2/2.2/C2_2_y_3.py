#语音信号采样频率变换
"""
Created on Tue Mar  6 19:40:20 2019

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
    wave_data = np.frombuffer(str_data, dtype=np.int16)
    wave_data.shape = -1, nchannels
#    wave_data = wave_data.T
    return nchannels,samplewidth,framerate,nframes,wave_data

if __name__== "__main__":
    print("start")
    channel,samplewidth,framerate,nframes,wave_data=waveread("C2_2_y.wav")
    s= np.arange(1,nframes+1)
    t = s/framerate
    x = wave_data /np.max(abs(wave_data))
    
    plt.figure()
    plt.subplot(3,1,1)
    plt.plot(t,x)
    plt.xlabel("time/s")
    plt.ylabel("归一化幅值")
    plt.title("原始信号")
    
    p= 2*len(x)
    x2 = ss.resample(x,p)
    x2 = x2/np.max(abs(x2))
    f2 = framerate*p
    t2 = np.arange(1,len(x2)+1) / f2
    
    plt.subplot(3,1,2)
    plt.plot(t2,x2)
    plt.xlabel("time/s")
    plt.ylabel("归一化幅值")
    plt.title("2倍采样率")
    
    q= int((1/2)*len(x))
    x3 = ss.resample(x,q)
    x3 = x3/np.max(abs(x3))
    f3 = framerate*q
    t3 = np.arange(1,len(x3)+1) / f3
    
    plt.subplot(3,1,3)
    plt.plot(t3,x3)
    plt.xlabel("time/s")
    plt.ylabel("归一化幅值")
    plt.title("1/2倍采样率")
#    
    