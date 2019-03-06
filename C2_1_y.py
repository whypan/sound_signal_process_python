# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:40:20 2019

@author: whypan
"""
import wave 
import matplotlib.pyplot as plt
import numpy as np
import pyaudio
import threading
import time 
print("start")
class Recorder():
    def __init__(self, chunk=1024, channels=1, rate=16000):
        self.CHUNK = chunk
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = channels
        self.RATE = rate
        self._running = True
        self._frames = []
    def start(self):
        threading._start_new_thread(self.__recording, ())
    def __recording(self):
        self._running = True
        self._frames = []
        p = pyaudio.PyAudio()
        stream = p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)
        while(self._running):
            data = stream.read(self.CHUNK)
            self._frames.append(data)
        stream.stop_stream()
        stream.close()
        p.terminate()
 
    def stop(self):
        self._running = False
 
    def save(self, filename):
        p = pyaudio.PyAudio()
        if not filename.endswith(".wav"):
            filename = filename + ".wav"
        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self._frames))
        wf.close()
        print("Saved")
        return filename

if __name__=="__main__":
    print("start")
    a = int (input("Press any key to start recording"))
    rec = Recorder()
    begin = time.time()
    print("start recording")
    rec.start()
    b = int(input("Press any key to stop recording"))
    print ("stop recording")
    rec.stop()
    fina = time.time()
    ti = int(fina - begin)
    print('录音时间为%ds'%ti)
    save_name = str(ti)+"_c1.wav"
    audio = rec.save(save_name)
    f1 = wave.open(audio,"rb")
    params = f1.getparams()
    nchannels,sampwidth,framerate,nframes = params[:4]
    str_data = f1.readframes(nframes)
    f1.close()
    wave_data = np.frombuffer(str_data, dtype=np.short)
    wave_data.shape = -1, nchannels
    wave_data = wave_data.T
    time = np.arange(0, nframes) * (1.0 / framerate)
    plt.subplot(111) 
    plt.plot(time, wave_data[0])
#    pl.subplot(212) 
#    pl.plot(time, wave_data[1], c="g")
    plt.xlabel("time (seconds)")
    plt.show()
