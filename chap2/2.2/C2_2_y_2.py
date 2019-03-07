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
    channel,samplewidth,framerate,nframes,wave_data=waveread("C2_2_y.wav")
    s= np.arange(1,nframes+1)
    t = s/framerate
    x = wave_data /np.max(abs(wave_data))
    y = np.transpose(np.random.randn(1,nframes))
    y = y /np.max(abs(y))
    z=ss.convolve(x,y)
    z = z/np.max(abs(z))
    t2 = (np.arange(1,len(z)+1))/framerate
    
    
    plt.figure()
    plt.subplot(3,1,1)
    plt.plot(t,x)
    plt.xlabel("time/s")
    plt.ylabel("归一化幅值",fontproperties="SimSun")
    plt.title("原始信号",fontproperties="SimSun")
    
    plt.subplot(3,1,2)
    plt.plot(t,y)
    plt.xlabel("time/s")
    plt.ylabel("归一化幅值",fontproperties="SimSun")
    plt.title("随机序列",fontproperties="SimSun")
    
    plt.subplot(3,1,3)
    plt.plot(t2,z)
    plt.xlabel("time/s",fontproperties="SimSun")
    plt.ylabel("归一化幅值",fontproperties="SimSun")
    plt.title("信号卷积",fontproperties="SimSun")
    plt.show()