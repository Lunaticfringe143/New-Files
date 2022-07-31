import wikipedia as wiki
import ctypes

word = input()

info = wiki.summary(word)

print(info)

#ctypes.windll.user32.MessageBoxW(0, info[:400], word, 0)