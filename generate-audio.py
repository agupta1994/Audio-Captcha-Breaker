#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 22:36:39 2019

@author: divyanshumarwah
"""

#!/usr/bin/env python3

import os
import numpy
import random
import string
import cv2
import argparse
import captcha.image
import captcha.audio
from gtts import gTTS

def scramble_image_name(image_name):
    import hashlib
    m = hashlib.sha1()
    m.update(image_name.encode('utf-8'))
    return m.hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--length', help='Length of captchas in characters', type=int)
    parser.add_argument('--count', help='How many captchas to generate', type=int)
    parser.add_argument('--scramble', help='Whether to scramble image names', default=False, action='store_true')
    parser.add_argument('--output-dir', help='Where to store the generated captchas', type=str)
    parser.add_argument('--symbols', help='File with the symbols to use in captchas', type=str)
    args = parser.parse_args()

    if args.length is None:
        print("Please specify the captcha length")
        exit(1)

    if args.count is None:
        print("Please specify the captcha count to generate")
        exit(1)

    if args.output_dir is None:
        print("Please specify the captcha output directory")
        exit(1)

    if args.symbols is None:
        print("Please specify the captcha symbols file")
        exit(1)

    symbols_file = open(args.symbols, 'r')
    captcha_symbols = symbols_file.readline().strip()
    symbols_file.close()

    print("Generating captchas with symbol set {" + captcha_symbols + "}")

    if not os.path.exists(args.output_dir):
        print("Creating output directory " + args.output_dir)
        os.makedirs(args.output_dir)

    for i in range(args.count):
        captcha_text = ''.join([random.choice(captcha_symbols) for j in range(args.length)])
        audio_name_scrambled = captcha_text
        if args.scramble:
            audio_name_scrambled = scramble_image_name(captcha_text)
        file_path = os.path.join(args.output_dir, audio_name_scrambled+'.wav')
        if os.path.exists(file_path):
            version = 1
            while os.path.exists(os.path.join(args.output_dir, audio_name_scrambled + '_' + str(version) + '.wav')):
                version += 1
            file_path = os.path.join(args.output_dir, audio_name_scrambled + '_' + str(version) + '.wav')

        #audio_data = numpy.array(captcha_generator.generate(captcha_text))
        #captcha_generator.write(captcha_text,file_path)
        tts=gTTS(text=captcha_text, lang='en')
        tts.save(file_path)
    

if __name__ == '__main__':
    main()
