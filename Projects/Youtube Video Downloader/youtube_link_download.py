qual=0
all=[]    
def download_youtube (link):
    from pytube.cli import on_progress,YouTube
    from click import clear
    

    vid=YouTube(link,on_progress_callback=on_progress)
    global qual
    print (f"Checking available qualities for {vid.title}")
    f_vid=vid.streams.filter(file_extension='mp4',progressive=True)
    clear()


    #to prevent asking for input again
    if qual==0:
        print(f"{vid.title} is availabe in 360p and 720p.")
        qual=input("Which quality do you want : ")
    else:
        pass


    #to make the wuality of video to be in 720p format
    if qual[-1]=='p':
        pass
    else:
        qual=qual+'p'


    #checking if the input quality is available in mp4
    f_vid_stream=f_vid.get_by_resolution(qual)
    if f_vid_stream==None:
        print (f"{qual} is not available")
        print(f"{vid.title} is availabe in 360p and 720p")
        qual=0
    else:
        print (f"Downloading {vid.title} in {qual}")
        print(f"{vid.title} is getting downloaded at {os.getcwd()}/Videos")
        f_vid_stream.download("Videos")
        clear()
        
        
        all.append(vid.title)
        for i in range(len(all)):
            print (f"{all[i]} has been downloaded in {qual}\n")


if __name__=="__main__":
    import pytube
    import os
    where=(input("How many videos are there ? "))
    if where == '1' or where == 'single':
        link=input("Please enter the link : ")
        download_youtube(link)
    else:
        typ=input("Is it a playlist : ")
        if typ=='yes':
            playlist_link=input("Kindly paste the link : ")
            playlist_list=pytube.Playlist(playlist_link)
            f=open('data.txt','a')
            for i in playlist_list:
                f.writelines(f"{i}\n")
            f.close()
            fdata=open('data.txt','r')
            while True:
                link = fdata.readline()
                if not link:
                    break
                else:    
                    download_youtube(link)
            fdata.close()
        else:
            print ("Kindly add the links in data.txt file")
            fdata=open('data.txt','r')
            while True:
                link = fdata.readline()
                if not link:
                    break
                else:    
                    download_youtube(link)
            fdata.close()
    os.remove('data.txt')