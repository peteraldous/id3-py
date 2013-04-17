from ID3 import *

tags = ID3("test.mp3")
print(tags.title)
print(tags.artist)
print(tags.album)
print(tags.year)
print(tags.comment)
print(tags.track)
print(tags.genre)
