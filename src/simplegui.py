import wx
from simpleguiframe import *

SW_TITLE = "SIMPLE GUI"
WINDOW_SIZE = 480

def main(): 
    app = wx.App()
    frm = SimpleGuiFrame(None, title=SW_TITLE, size=(WINDOW_SIZE,WINDOW_SIZE))
    frm.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()