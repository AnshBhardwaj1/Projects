from youtube_link_download import download
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