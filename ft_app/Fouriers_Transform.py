# Python example - Fourier transform using numpy.fft method

import numpy as np

import matplotlib.pyplot as plotter


import tkinter as Filetracker
from tkinter import filedialog,Text,Tk

import os

root = Filetracker.Tk(screenName='Helllo World!!!')

root.title("FOURIER'S TRANSFORM VISUALIZATION")

apps =[]


def openApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File(s)",
                                      filetypes=(("executables", "*.exe"), ("All Files", "*.*")))
    apps.append(filename)
    print(filename)

    for app in apps:
        label = Filetracker.Label(frame, text=app, bg="red")
        label.pack()

def runApp():
    for app in apps:
        os.startfile(app)
def ft_options():
    #root2 = Filetracker.Tk(screenName='Helllo World!!!')

    #root2.title("<<<FOURIRER'S TRANSFORM VISUALIZATION>>>")

    #canvas1 = Filetracker.Canvas(root2, height=400, width=400, background="aquamarine")
    #canvas1.pack()

    #frame1 = Filetracker.Frame(root2, bg="orange")
    #frame1.place(relheight=0.5, relwidth=0.5, relx=0.2, rely=0.2)
    #def FT_input():



    def cosine_ft():
        # How many time points are needed i,e., Sampling Frequency
        samplingFrequency = 100


        # At what intervals time points are sampled

        samplingInterval = 1 / samplingFrequency

        # Begin time period of the signals

        beginTime = 0

        # End time period of the signals

        endTime = 10

        # Frequency of the signals

        signal1Frequency = 4

        signal2Frequency = 7

        # Time points

        time = np.arange(beginTime, endTime, samplingInterval)

        # Create two sine waves

        amplitude1 = np.cos(2 * np.pi * signal1Frequency * time)

        amplitude2 = np.cos(2 * np.pi * signal2Frequency * time)

        # Create subplot

        figure, axis = plotter.subplots(4, 1)

        plotter.subplots_adjust(hspace=2)

        # Time domain representation for sine wave 1
        axis[0].set_title('Cosine wave with a frequency of 4 Hz')

        axis[0].plot(time, amplitude1)

        axis[0].set_xlabel('Time')

        axis[0].set_ylabel('Amplitude')

        # Time domain representation for sine wave 2

        axis[1].set_title('Cosine wave with a frequency of 7 Hz')

        axis[1].plot(time, amplitude2)

        axis[1].set_xlabel('Time')

        axis[1].set_ylabel('Amplitude')

        # Add the sine waves

        amplitude = amplitude1 + amplitude2

        # Time domain representation of the resultant sine wave

        axis[2].set_title('Cosine wave with multiple frequencies')

        axis[2].plot(time, amplitude)

        axis[2].set_xlabel('Time')

        axis[2].set_ylabel('Amplitude')

        # Frequency domain representation

        fourierTransform = np.fft.fft(amplitude) / len(amplitude)  # Normalize amplitude

        fourierTransform = fourierTransform[range(int(len(amplitude) / 2))]  # Exclude sampling frequency

        tpCount = len(amplitude)

        values = np.arange(int(tpCount / 2))

        timePeriod = tpCount / samplingFrequency

        frequencies = values / timePeriod

        # Frequency domain representation

        axis[3].set_title('Fourier transform depicting the frequency components')

        axis[3].plot(frequencies, abs(fourierTransform))

        axis[3].set_xlabel('Frequency')

        axis[3].set_ylabel('Amplitude')

        plotter.show()

    def sine_ft():
        # How many time points are needed i,e., Sampling Frequency
        samplingFrequency = 100

        # At what intervals time points are sampled

        samplingInterval = 1 / samplingFrequency

        # Begin time period of the signals

        beginTime = 0

        # End time period of the signals

        endTime = 10

        # Frequency of the signals

        signal1Frequency = 4

        signal2Frequency = 7

        # Time points

        time = np.arange(beginTime, endTime, samplingInterval)

        # Create two sine waves

        amplitude1 = np.sin(2 * np.pi * signal1Frequency * time)

        amplitude2 = np.sin(2 * np.pi * signal2Frequency * time)

        # Create subplot

        figure, axis = plotter.subplots(4, 1)

        plotter.subplots_adjust(hspace=2)

        # Time domain representation for sine wave 1
        axis[0].set_title('Sine wave with a frequency of 4 Hz')

        axis[0].plot(time, amplitude1)

        axis[0].set_xlabel('Time')

        axis[0].set_ylabel('Amplitude')

        # Time domain representation for sine wave 2

        axis[1].set_title('Sine wave with a frequency of 7 Hz')

        axis[1].plot(time, amplitude2)

        axis[1].set_xlabel('Time')

        axis[1].set_ylabel('Amplitude')

        # Add the sine waves

        amplitude = amplitude1 + amplitude2

        # Time domain representation of the resultant sine wave

        axis[2].set_title('Sine wave with multiple frequencies')

        axis[2].plot(time, amplitude)

        axis[2].set_xlabel('Time')

        axis[2].set_ylabel('Amplitude')

        # Frequency domain representation

        fourierTransform = np.fft.fft(amplitude) / len(amplitude)  # Normalize amplitude

        fourierTransform = fourierTransform[range(int(len(amplitude) / 2))]  # Exclude sampling frequency

        tpCount = len(amplitude)

        values = np.arange(int(tpCount / 2))

        timePeriod = tpCount / samplingFrequency

        frequencies = values / timePeriod

        # Frequency domain representation

        axis[3].set_title('Fourier transform depicting the frequency components')

        axis[3].plot(frequencies, abs(fourierTransform))

        axis[3].set_xlabel('Frequency')

        axis[3].set_ylabel('Amplitude')

        plotter.show()



    cosine = Filetracker.Button(root, width=20, text="Cosine Transform", command=cosine_ft)
    cosine.pack()

    sine = Filetracker.Button(root, width=20, text="sine Transform", command=sine_ft)
    sine.pack()




canvas = Filetracker.Canvas(root, height=400, width=400, background="aquamarine")
canvas.pack()

frame = Filetracker.Frame(root, bg="orange")
frame.place(relheight=0.5, relwidth=0.5, relx=0.2, rely=0.2)

#open = Filetracker.Button(root, width=10, text="App Open", command=openApp)
#open.pack()

#run = Filetracker.Button(root, width=10, text="App Run", command=runApp)
#run.pack()

#fot = Filetracker.Button(root, width=20, text="Fourier's Transform", command=ft)
#fot.pack()

ftoptions = Filetracker.Button(root, width=30, text="Fourier's Transform Visualization", command=ft_options)
ftoptions.pack()

for app in apps:
    l = Filetracker.Button(frame, text=apps.seek, width=10, command=runApp)
    l.pack()

root.mainloop(n=0)


