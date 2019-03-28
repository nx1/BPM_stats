#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 17:27:17 2019

@author: x1
"""

from pydub import AudioSegment

song = AudioSegment.from_mp3('Circles.mp3')

memes = song[0:1000]
print(memes)