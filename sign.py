import time
import sys 
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics


fakebus = {u'rt': u'74', u'rtdd': u'74', u'tmstmp': u'20180629 22:51', u'vid': u'8210', u'stpnm': u'Fullerton & Hamlin', u'des': u'Halsted', u'dstp': 21741, u'zone': u'', u'tablockid': u'74 -853', u'prdctdn': u'23', u'rtdir': u'Eastbound', u'tatripid': u'140', u'typ': u'A', u'dly': False, u'prdtm': u'20180629 23:14', u'stpid': u'1317'}
FONT_FILE= '/home/pi/CTAsign/font/4x6.bdf'
#TEXT_COLOR = (53,204,51)
TEXT_COLOR = (0,128,255)
BG_COLOR = (0,0,0)
OUTLINE_COLOR = (128,128,128)

class Sign(object):
    #Handles LED Maxtix Display taking in 2 buses and displaying them on the screen    
    def __init__(self):
        self.options = RGBMatrixOptions()
        self.options.rows = 16
        self.options.chain_length = 2
        self.options.parallel = 1
        self.options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
        self.matrix = RGBMatrix(options = self.options) 
        self.outlineColor = graphics.Color(128,128,128)
        self.textColor = graphics.Color(0,128,255)
        self.font = graphics.Font()
        self.font.LoadFont(FONT_FILE)
           

    def makeBus(self,topBus,botBus):
        #set up canvas blank canvas 
        self.canvas = self.matrix.CreateFrameCanvas()
        #Draw boarders around each line of text       
        graphics.DrawLine(self.canvas, 0, 7,63, 7,self.outlineColor)
        graphics.DrawLine(self.canvas, 0, 8,63, 8,self.outlineColor)
        graphics.DrawLine(self.canvas, 0, 0,63, 0,self.outlineColor)
        graphics.DrawLine(self.canvas, 0,15,63,15,self.outlineColor)
        graphics.DrawLine(self.canvas, 0, 0, 0,15,self.outlineColor)
        graphics.DrawLine(self.canvas, 63,0,63,15,self.outlineColor)
        #draw Top Bus 
        if topBus:
            print 'making bus'
            busString = '{} {}: {}'.format(topBus[u'rt'],topBus[u'des'],topBus[u'prdctdn'])
            graphics.DrawText(self.canvas,self.font,2,7,self.textColor,busString)
        #Draw Bottom Bus
        if botBus:
            busString = '{} {}: {}'.format(botBus[u'rt'],botBus[u'des'],botBus[u'prdctdn'])
            graphics.DrawText(self.canvas,self.font,2,15,self.textColor,busString)
        
          
           
    def display(self):
        self.canvas = self.matrix.SwapOnVSync(self.canvas)     
      

def testMatrix():
    mat = Sign()
    mat.makeBus(fakebus,fakebus)
    mat.display()
    try:
        print("Press CTRL-C to stop.")
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        sys.exit(0)

if __name__=='__main__':
    print 'Testing Matrix'
    testMatrix()
    
