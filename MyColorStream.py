import sys
STD_INPUT_HANDLE = -10 
STD_OUTPUT_HANDLE= -11 
STD_ERROR_HANDLE = -12 
FOREGROUND_WHITE = 0x0007 
FOREGROUND_BLUE = 0x01 # text color contains blue. 
FOREGROUND_GREEN= 0x02 # text color contains green. 
FOREGROUND_RED  = 0x04 # text color contains red. 
FOREGROUND_INTENSITY = 0x08 # text color is intensified. 
FOREGROUND_YELLOW = FOREGROUND_RED | FOREGROUND_GREEN 
BACKGROUND_BLUE = 0x10 # background color contains blue. 
BACKGROUND_GREEN= 0x20 # background color contains green. 
BACKGROUND_RED  = 0x40 # background color contains red. 
BACKGROUND_INTENSITY = 0x80 # background color is intensified. 

import ctypes 
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_ERROR_HANDLE) 
def set_color(color, handle=std_out_handle): 
    """(color) -> BOOL     
    Example: set_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY) 
    """ 
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color) 
    return bool

def reset_color():
    set_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)

def _ColorWritelnDecorator(stream = sys.stderr):
    myStream = MyColorStream(stream)
    return myStream

class MyColorStream:
    def __init__(self,stream=sys.stderr):
        self.stream = stream
        
    def write(self,content):
        self.stream.write(content)
        self.stream.flush()
        
    def writeln(self,content=""):
        self.stream.write(content+'\n')
    
    def yellow(self,content):
        set_color(FOREGROUND_YELLOW | FOREGROUND_INTENSITY)
        self.write(content)
        reset_color()
    
    def red(self,content):
        set_color(FOREGROUND_RED | FOREGROUND_INTENSITY)
        self.write(content)
        reset_color()
    
    def green(self,content):
        set_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)
        self.write(content)
        reset_color()
        
        
        