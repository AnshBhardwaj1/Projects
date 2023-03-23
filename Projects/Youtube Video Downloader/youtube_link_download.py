qual=0
all=[]    
def download (link):
    from pytube.cli import on_progress,YouTube
    from click import clear
    vid=YouTube(link,on_progress_callback=on_progress)
    global qual
    print (f"Checking available qualities for {vid.title}")
    f_vid=vid.streams.filter(file_extension='mp4',progressive=True)
    clear()

    if qual==0:
        print(f"{vid.title} is availabe in 360p and 720p")
        qual=input("Which quality do you want : ")
    else:
        pass
    if qual[-1]=='p':
        pass
    else:
        qual=qual+'p'
    print (f"Downloading {vid.title} in {qual}")
    f_vid_stream=f_vid.get_by_resolution(qual)
    if f_vid_stream==None:
        print (f"{qual} is not available")
        print(f"{vid.title} is availabe in 360p and 720p")
        qual=0
    else:
        f_vid_stream.download("Videos")
        clear()
        all.append(vid.title)
        for i in range(len(all)):
            print (f"{all[i]} has been downloaded in {qual}\n")
if __name__=="__main__":
    where=(input("How many videos are there ? "))
    if where == '1' or where == 'single':
        link=input("Please enter the link : ")
        download(link)
    else:
        print ("Kindly add the links in data.txt file")
        fdata=open('data.txt','r')
        while True:
            link = fdata.readline()
            if not link:
                break
            else:    
                download(link)
        fdata.close()