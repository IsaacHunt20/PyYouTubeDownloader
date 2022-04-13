from pytube import YouTube

SAVE_PATH = r"C:\Users\isaac\OneDrive\Desktop\OpenGLTutorial"

link = open(r'ytlinks.txt', 'r')

for i in link:
    try:
        yt = YouTube(i)
    except:
        print("CONNECTION ERROR")

    try: 
        stream = yt.streams.get_highest_resolution()
        stream.download(SAVE_PATH)
    except:
        print("Something went wrong")
print("Task Completed!")