import gtts
from playsound import playsound

short_break = gtts.gTTS("short break")
short_break.save("short_break.mp3")

long_break = gtts.gTTS("long break")
long_break.save("long_break.mp3")

work_break = gtts.gTTS("Работа", lang="ru")
work_break.save("rabota.mp3")

playsound("short_break.mp3")
playsound("long_break.mp3")
playsound("rabota.mp3")