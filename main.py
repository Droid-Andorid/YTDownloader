import customtkinter as tk
from ytdl import Downloader


class MainFrame(tk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class SecondFrame(tk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.url_var = tk.StringVar(self)
        self.linked_allowed = ["https://www.youtube.com/", "https://youtu.be/", "http://youtu.be/",
                               "https://youtube.com/", "https://m.youtube.com/", "http://m.youtube.com/"]

        self.frame = tk.CTkFrame(self)

        self.lb_title = tk.CTkLabel(self, text="Youtube downloader", font=("title", 20))
        self.lb_select_format = tk.CTkLabel(self.frame, text="Select format")
        self.list_format = tk.CTkOptionMenu(self.frame, values=["mp4", "mp3", "m4a", "ogg", "wav"])
        self.lb_opt_quality = tk.CTkLabel(self.frame, text="Select quality")
        self.list_quality = tk.CTkOptionMenu(self.frame, values=["1080", "720", "480", "360"])
        self.field_filename = tk.CTkEntry(self,
                                          placeholder_text="Enter how be name file without .(format) (not necessarily)", width=300)
        self.lb_url = tk.CTkLabel(self, text="Enter url on video")
        self.field_url = tk.CTkTextbox(self, height=10, width=250)
        self.btn = tk.CTkButton(self, text="Download", command=self.btn_download)
        self.lb_info = tk.CTkLabel(self, text=" ", text_color="#BE4D4D")

        self.lb_title.pack(ipadx=5)
        self.frame.pack(pady=15)
        self.lb_select_format.grid(row=1, column=1, padx=10)
        self.list_format.grid(row=2, column=1, padx=10, pady=5)
        self.lb_opt_quality.grid(row=1, column=2, padx=10)
        self.list_quality.grid(row=2, column=2, padx=10, pady=5)
        self.field_filename.pack()
        self.lb_url.pack()
        self.field_url.pack()
        self.btn.pack(pady=10)
        self.lb_info.pack()

    def check_link(self, url):
        for i in self.linked_allowed:
            if url.startswith(i):
                return True
            elif url.startswith("https://youtu.be/") or url.startswith("http://youtu.be/"):
                return True
            else:
                return False

    def btn_download(self):
        dl = Downloader(self.field_url.get("0.0", tk.END))

        if not self.check_link(self.field_url.get("0.0", tk.END)):
            self.lb_info.configure(text="Wrong url")
            self.lb_info.update()
            return

        self.lb_info.configure(text="Please wait", text_color="white")
        self.lb_info.update()

        try:
            dl.download(self.list_quality.get(), self.list_format.get(), self.field_filename.get())
            self.lb_info.configure(text="Successful download in directory ")
        except Exception as e:
            self.lb_info.configure(text=f"Unknown error\n {e}", text_color="red")


class App(tk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("650x450")
        self.title("YTDownloader")
        self.minsize(340, 400)
        self._set_scaled_min_max()

        self.frame = MainFrame(self, bg_color="grey", width=70)
        self.second_frame = SecondFrame(self.frame, height=70, corner_radius=15)
        self.frame.pack(pady=50)
        self.second_frame.pack()


app = App()
app.mainloop()
