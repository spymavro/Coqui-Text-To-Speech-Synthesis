# -*- coding: utf-8 -*-
"""coqui_TTS.py
"""

## Install Coqui TTS
! pip install -U pip
! pip install TTS
! pip install -U tensorflow
# ! pip install git+https://github.com/coqui-ai/TTS@dev

!tts --list_models

!tts --use_cuda True --model_name tts_models/multilingual/multi-dataset/xtts_v2 --language_idx en --speaker_idx 'Ana Florence' --text "Don't you agree that the last two weeks at the university were very tiring?" --out_path test1.wav # --vocoder_name vocoder_models/en/ljspeech/univnet

import IPython
IPython.display.Audio("test1.wav")

!tts --use_cuda True --model_name tts_models/multilingual/multi-dataset/xtts_v2 --language_idx en --speaker_idx 'Ana Florence' --text "I went shopping at the supermarket at 6 pm because I was missing a lot of things and then I came home and cooked lasagna." --out_path test2.wav # --vocoder_name vocoder_models/en/ljspeech/univnet
IPython.display.Audio("test2.wav")

!tts --use_cuda True --model_name tts_models/multilingual/multi-dataset/xtts_v2 --language_idx en --speaker_idx 'Ana Florence' --text "Do not use ready-made solutions from the internet. This way you will not learn to handle TTS systems correctly." --out_path test3.wav # --vocoder_name vocoder_models/en/ljspeech/univnet
IPython.display.Audio("test3.wav")

!tts --use_cuda True --model_name tts_models/multilingual/multi-dataset/xtts_v2 --language_idx en --speaker_idx 'Ana Florence' --text "Every year on May 1st there are 24-hour strikes, as it is International Workers' Day, which began in 1886 with the strikes of 600,000 workers in the USA and over 80,000 in Chicago." --out_path test4.wav # --vocoder_name vocoder_models/en/ljspeech/univnet
IPython.display.Audio("test4.wav")

!tts --use_cuda True --model_name tts_models/multilingual/multi-dataset/xtts_v2 --language_idx en --speaker_idx 'Ana Florence' --text "Do you remember when I asked you if John got married? Well, he did! I met him on the street and he told me." --out_path test5.wav # --vocoder_name vocoder_models/en/ljspeech/univnet
IPython.display.Audio("test5.wav")

!tts --use_cuda True --model_name tts_models/en/ljspeech/fast_pitch --text "Don't you agree that the last two weeks at the university were very tiring?" --out_path test6.wav # --vocoder_name vocoder_models/en/ljspeech/univnet
IPython.display.Audio("test6.wav")

!tts --use_cuda True --model_name tts_models/en/ljspeech/fast_pitch --text "I went shopping at the supermarket at 6 pm because I was missing a lot of things and then I came home and cooked lasagna." --out_path test7.wav # --vocoder_name vocoder_models/en/ljspeech/univnet
IPython.display.Audio("test7.wav")

!tts --use_cuda True --model_name tts_models/en/ljspeech/fast_pitch --text "Do not use ready-made solutions from the internet. This way you will not learn to handle TTS systems correctly." --out_path test8.wav # --vocoder_name vocoder_models/en/ljspeech/univnet
IPython.display.Audio("test8.wav")

!tts --use_cuda True --model_name tts_models/en/ljspeech/fast_pitch --text "Every year on May 1st there are 24-hour strikes, as it is International Workers' Day, which began in 1886 with the strikes of 600,000 workers in the USA and over 80,000 in Chicago." --out_path test9.wav # --vocoder_name vocoder_models/en/ljspeech/univnet
IPython.display.Audio("test9.wav")

!tts --use_cuda True --model_name tts_models/en/ljspeech/fast_pitch --text "Do you remember when I asked you if John got married? Well, he did! I met him on the street and he told me." --out_path test10.wav # --vocoder_name vocoder_models/en/ljspeech/univnet
IPython.display.Audio("test10.wav")

!tts --use_cuda True --model_name tts_models/en/multi-dataset/tortoise-v2 --text "Don't you agree that the last two weeks at the university were very tiring?" --out_path test11.wav # --vocoder_name vocoder_models/en/ljspeech/univnet
IPython.display.Audio("test11.wav")

!tts --use_cuda True --model_name tts_models/en/multi-dataset/tortoise-v2 --text "I went shopping at the supermarket at 6 pm because I was missing a lot of things and then I came home and cooked lasagna." --out_path test12.wav # --vocoder_name vocoder_models/en/ljspeech/univnet
IPython.display.Audio("test12.wav")

!tts --use_cuda True --model_name tts_models/en/multi-dataset/tortoise-v2 --text "Do not use ready-made solutions from the internet. This way you will not learn to handle TTS systems correctly." --out_path test13.wav # --vocoder_name vocoder_models/en/ljspeech/univnet
IPython.display.Audio("test13.wav")

!tts --use_cuda True --model_name tts_models/en/multi-dataset/tortoise-v2 --text "Every year on May 1st there are 24-hour strikes, as it is International Workers' Day, which began in 1886 with the strikes of 600,000 workers in the USA and over 80,000 in Chicago." --out_path test14.wav # --vocoder_name vocoder_models/en/ljspeech/univnet
IPython.display.Audio("test14.wav")

!tts --use_cuda True --model_name tts_models/en/multi-dataset/tortoise-v2 --text "Do you remember when I asked you if John got married? Well, he did! I met him on the street and he told me." --out_path test15.wav # --vocoder_name vocoder_models/en/ljspeech/univnet
IPython.display.Audio("test15.wav")
