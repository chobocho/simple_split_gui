import wx
from simpleguipanel import *
from simpleguimenu import * 

WINDOW_SIZE = 480

class SimpleGuiFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(SimpleGuiFrame, self).__init__(*args, **kw)
 
        self.splitter = wx.SplitterWindow(self, -1, wx.Point(0, 0), wx.Size(WINDOW_SIZE, WINDOW_SIZE), wx.SP_3D | wx.SP_BORDER)
        self.leftPanel = SimpleGuiPanel(self.splitter)
        self.rightPanel = SimpleGuiPanel(self.splitter)
        self.splitter.SplitVertically(self.leftPanel, self.rightPanel)
        self.splitter.SetMinimumPaneSize(20)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.splitter, 1, wx.EXPAND)
        self.SetSizer(sizer)

        self._addMenubar()

    def _addMenubar(self):
        self.menu = SimpleGuiMenu(self)

    def OnQuit(self, event):
        self.Close()

    def OnAbout(self, event):
        msg = 'Simeple GUI Template V0.1\nhttp://chobocho.com'
        title = 'About'
        wx.MessageBox(msg, title, wx.OK | wx.ICON_INFORMATION)
