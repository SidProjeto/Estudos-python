from pygame import mixer
mixer.init()
mixer.music.load(r'D:\downloads\kakaist-rain-sfx-352275.mp3')
mixer.music.play(-1)
input('Aperte ENTER para encerrar')
