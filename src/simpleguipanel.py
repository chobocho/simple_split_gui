import wx
from filedrop import *

WINDOW_SIZE = 480

class SimpleGuiPanel(wx.Panel):
    def __init__(self, *args, **kw):
        super(SimpleGuiPanel, self).__init__(*args, **kw)
        filedrop = FileDrop(self)
        self.SetDropTarget(filedrop)
        self._initUi()
        self.SetAutoLayout(True)


    def _initUi(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.text = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER|wx.TE_MULTILINE, size=(WINDOW_SIZE/2,WINDOW_SIZE))
        self.text.SetValue("")
        sizer.Add(self.text, 1, wx.EXPAND)
        
        btnBox = wx.BoxSizer(wx.HORIZONTAL)

        clearBtnId = wx.NewId()
        clearBtn = wx.Button(self, clearBtnId, "Clear", size=(50,30))
        clearBtn.Bind(wx.EVT_BUTTON, self.OnClearBtn)
        btnBox.Add(clearBtn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        sizer.Add(btnBox, 0, wx.ALIGN_CENTER_VERTICAL, 5)
        self.SetSizer(sizer)

    def OnCallback(self, filelist):
        self._printFileList(filelist)

    def _printFileList(self, files):
        fileList = ""
        for file in files:
            fileList += file + "\n"
        self.text.SetValue(fileList)

    def OnClearBtn(self, event):
        self.text.SetValue("")