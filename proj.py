import tkinter
import customtkinter
from pytube import YouTube

def startd():
    try:
        ytlink = link.get()
        ytob = YouTube(ytlink,on_progress_callback=on)
        video = ytob.streams.get_highest_resolution()
        #they did not fucking work
        #title2.configure(Text=ytob.title)
        #labe.configure("")
        video.download()
        

        labe.configure(text="DOWNLOAD COMPLETE say thank you ",text_color="#00FF00")
    except :
        labe.configure(text="somthing went Wrong FUCKhead", text_color="red")

       
    
def on(stream, chunk, bytes_remaining):
    totalS = stream.filesize
    bytesD = totalS - bytes_remaining
    pret =bytesD/totalS * 100
    pre = str(int(pret))
    pe.configure(text=pre +'%')
    pe.update()

    pro.set(float(pret)/100)


    



   
         

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube downloader mo")

#

title2 = customtkinter.CTkLabel(app,text="Insert a youtube link " ,font=("impact",44))
title2.pack(padx=10,pady=10)

url = tkinter.StringVar()
link = customtkinter.CTkEntry(app,width=600,height=50,textvariable=url)
link.pack()

#finished
labe =customtkinter.CTkLabel(app, text=" ")
labe.pack() 
#p
pe = customtkinter.CTkLabel(app, text="0%")
pe.pack()

pro = customtkinter.CTkProgressBar(app, width=500)
pro.set(0)
pro.pack(padx=12,pady=12)
#D
download2 = customtkinter.CTkButton(app, text="Download",command=startd)
download2.pack(padx=7,pady=7)

app.mainloop()