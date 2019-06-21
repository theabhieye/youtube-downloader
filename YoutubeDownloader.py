import youtube_dl
print("_"*45)
print()
print("Welcome to youtube Audio/Video downloader")
print()
print("_"*45)
print()
print("Enter url of the video you want to download:",end='')
url=input()

print('\n')
print("-"*5,"Choose Your Option","-"*5,"\n")
print(" "*5,'Enter 1 for Audio only'," "*5)
print()
print(" "*5,'Enter 2 for Video+Audio'," "*5)
print('\n')
a=input("Enter your choice:")



if a=='1':
    option={'format': 'bestaudio/best','extractaudio' : True}
elif a== '2':
    option = {}
else:
    print("invliad number")

with youtube_dl.YoutubeDL(option) as ydl:
    ydl.download([url])
