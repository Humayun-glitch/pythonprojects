import sounddevice

from scipy.io.wavfile import write

fs=44100 #sample rate

second=int(input("Enter the time duration in seconds: "))

print("Recording....\n")

recordVoice=sounddevice.rec(int(second * fs),samplerate=fs,channels=2)

sounddevice.wait()

write("output.wav",fs,recordVoice) #outputs the recorded voice in a .wav file

print("Done....\nPlease Check...")