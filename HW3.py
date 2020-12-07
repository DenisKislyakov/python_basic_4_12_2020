time = 10417
hour = time // 3600
min = (time % 3600) // 60
sec = time - (hour * 3600) - (min * 60)
print("%02d:%02d:%02d" % (hour, min, sec))