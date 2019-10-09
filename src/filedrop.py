import wx

class FileDrop(wx.FileDropTarget):
    def __init__(self, parent):
        super(FileDrop, self).__init__()
        self.window = parent

    def OnDropFiles(self, x, y, filenames):
        self.window.OnCallback(filenames)
        return True