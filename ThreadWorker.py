import pytube
from PyQt5.QtCore import QThread, pyqtSignal


class ThreadWorker(QThread):
    finished = pyqtSignal(pytube.streams.Stream, str)
    progress = pyqtSignal(pytube.streams.Stream, bytes, int)

    def __init__(self, yt, res):
        QThread.__init__(self)
        self.yt = yt
        self.res = res

    def run(self):
        self.yt.register_on_progress_callback(self.progress.emit)
        self.yt.register_on_complete_callback(self.finished.emit)
        self.yt.streams.filter(file_extension='mp4', progressive=True).get_by_resolution(self.res).download()
