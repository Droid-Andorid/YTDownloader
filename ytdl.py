from yt_dlp import YoutubeDL
from os import rename, getcwd, listdir


class Downloader:
    def __init__(self, url):
        self._YTDL_options = {
            'format': 'mp4/bv+ba',
            'outtmpl': '%(title)s.%(ext)s',
            'restrictfilenames': True,
            'noplaylist': True,
            'nocheckcertificate': True,
            'ignoreerrors': False,
            'logtostderr': False,
            'no_warnings': True,
            "keepvideo": False,
        }
        self._url = url

    def set_filename(self, old_name, new_name, form):
        if new_name is None or new_name in ["", " "]:
            return

        if old_name not in ["", " "] or old_name is not None:
            for file in listdir(getcwd()):
                if file.endswith(f"{old_name}.{form}"):
                    rename(file, f"{new_name.replace(' ', '_')}.{form}")

    def set_quality(self, quality, format_file):
        if quality is None:
            raise ValueError("Please enter quality video!")

        if format_file == "ogg" or format_file == "wav" or format_file == "mp3":
            self._YTDL_options["format"] = f"{format_file}/ba"

        self._YTDL_options["format"] = f"{format_file}/{quality}"

    def download(self, quality: str, format_file: str = 'mp3', name: str = None):
        self.set_quality(quality, format_file)

        with YoutubeDL(self._YTDL_options) as ydl:
            INFO = ydl.extract_info(self._url, download=False)

            name_out_file = str(INFO["title"])

            ydl.download(self._url)

        self.set_filename(name_out_file.replace(" ", "_"), name, format_file)
