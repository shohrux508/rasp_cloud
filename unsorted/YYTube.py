from pytube import YouTube
url = 'https://youtube.com/shorts/-F4WJCQsyEg?si=7v5Q19-YaGnpvGxP'
yt = YouTube(url)
while True:
    try:
        print('trying...')
        streams = yt.streams.filter(only_audio=True)
        break
    except:
        print('error!')
        pass
for i in streams:
    print(f"{i.abr} and {i.mime_type}")

a = int(input('Input number: '))


