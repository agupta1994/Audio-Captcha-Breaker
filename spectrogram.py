import os
import matplotlib.pyplot as plt

#for loading and visualizing audio files
import librosa
import librosa.display

#to play audio
import IPython.display as ipd


	#parser = argparse.ArgumentParser()
	#parser.add_argument('--output-dir', help='Where to store the generated captchas', type=str)
	#args = parser.parse_args()

	audio_fpath = "Downloads/wav files/"
	audio_clips = os.listdir(audio_fpath)
	print("No. of .wav files in audio folder = ",len(audio_clips))



	x, sr = librosa.load(audio_fpath+audio_clips[0], sr=44100)

	print(type(x), type(sr))
	print(x.shape, sr)

	plt.figure(figsize=(14, 5))
	print('test')
	librosa.display.waveplot(x, sr=sr)

	X = librosa.stft(x)
	Xdb = librosa.amplitude_to_db(abs(X))
	plt.figure(figsize=(14, 5))
	librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
	plt.colorbar()

	plt.figure(figsize=(14, 5))
	librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
	plt.colorbar()

 	#if args.output_dir is None:
        #print("Please specify the captcha output directory")
        #exit(1)

 	#if not os.path.exists(args.output_dir):
        #print("Creating output directory " + args.output_dir)
        #os.makedirs(args.output_dir)









