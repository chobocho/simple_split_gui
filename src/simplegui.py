import wx
import logging
import logging.handlers
from simpleguiframe import *

SW_TITLE = "SIMPLE GUI"
WINDOW_SIZE = 480

def initLogger():
    logger = logging.getLogger("simple_gui")
    logger.setLevel(logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s [%(levelno)d] %(filename)s %(funcName)s > %(message)s')
    
    stream_hander = logging.StreamHandler()
    stream_hander.setFormatter(formatter)
    logger.addHandler(stream_hander)
    
    max_log_size = 128 * 1024

    file_handler = logging.handlers.RotatingFileHandler(filename='./simple_gui.log', maxBytes=max_log_size)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    logger.info('=== ' + SW_TITLE + ' ===')

def printEnd():
    logger = logging.getLogger("simple_gui")
    logger.info('=== END ===')

def printEnd():
    logger = logging.getLogger("simple_gui")
    logger.info('=== END ===')

def main(): 
    app = wx.App()
    frm = SimpleGuiFrame(None, title=SW_TITLE, size=(WINDOW_SIZE,WINDOW_SIZE))
    frm.Show()
    app.MainLoop()

if __name__ == '__main__':
    initLogger()
    main()
    printEnd()