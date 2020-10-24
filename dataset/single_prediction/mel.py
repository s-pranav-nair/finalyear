import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

def mel_spectrogram(filename,i):
    ambulance_song,_,y,sr = get_wav_details(filename)
    plt.figure(figsize=(2.24, 2.24))
    n_mels = 128
    n_fft = 2048
    hop_length = 512
    S = librosa.feature.melspectrogram(ambulance_song, sr=sr, n_fft=n_fft, hop_length=hop_length, n_mels=n_mels)
    S_DB = librosa.power_to_db(S, ref=np.max)
#     librosa.display.specshow(S_DB, sr=sr, hop_length=hop_length, x_axis='time', y_axis='mel');
    librosa.display.specshow(S_DB, sr=sr, hop_length=hop_length)
#     plt.colorbar(format='%+2.0f dB');
    out_file = 'ambulance_or_traffic_11.png'
    plt.savefig(out_file)
    

def get_wav_details(filename):    
    y, sr = librosa.load(filename)
    # trim silent edges
    ambulance_song, _ = librosa.effects.trim(y)
    # To plot time domain graph
#     librosa.display.waveplot(ambulance_song, sr=sr)
    return ambulance_song, _,y,sr

#for i in range(1,201):
#    filename = 'sound_'+ str(i) +'.wav'
#    mel_spectrogram(filename,i)
mel_spectrogram('traffic2.wav',1)
