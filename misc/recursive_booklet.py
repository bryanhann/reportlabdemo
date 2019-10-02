import time
import datetime
import os
from reportlab.pdfgen.canvas import Canvas
import reportlab.lib.pagesizes

FILENAME = 'out.booklet.pdf'
A4 = reportlab.lib.pagesizes.A4

WIDTH,HEIGHT = A4
RATIO = HEIGHT/WIDTH
TOP = HEIGHT - 50
BOT = 30
LEFT = 50
RIGHT = WIDTH-30
QUARTER = (TOP-BOT)/(24*4)
a = datetime.datetime.now() 
date = a.strftime('%Y-%m-%d (%a)') 





def main():
    canvas = Canvas(FILENAME)
    global L  
    global R  
    R = LeftHalfCM(canvas)
    L = RightHalfCM(canvas)
    CCM = StateCM(canvas)
    canvas.setFont("Courier", 8)
    canvas.setPageSize(A4)
    c = canvas


    with L: compass4canvas(canvas,'L')
    with R,L: compass4canvas(canvas,'L')
    with R,R,L: compass4canvas(canvas,'L')
    with R,R,R,L: compass4canvas(canvas,'L')
    with R,R,R,R,L: compass4canvas(canvas,'L')
    with R,R,R,R,R,L: compass4canvas(canvas,'L')
    with R,R,R,R,R,R,L: compass4canvas(canvas,'L')
    with R,R,R,R,R,R,R,L: compass4canvas(canvas,'L')
    with R,R,R,R,R,R,R,R,L: compass4canvas(canvas,'L')
    with R,R,R,R,R,R,R,R,R,L: compass4canvas(canvas,'L')
    ##canvas.translate(WIDTH/2,HEIGHT/2)
    canvas.showPage()
    canvas.save()
    print( 'canvas is auto saved to file', canvas._filename )
    time.sleep(1)
    os.system( 'open %s' % canvas._filename )

def compass4canvas(canvas, label='anon'):
    canvas.setLineWidth(0)
    RR = 30
    canvas.circle(0,0,RR)
    canvas.drawString(0,RR,'N')
    canvas.drawString( RR, RR,'NE')
    canvas.drawString(-RR,-RR,'SW')
    canvas.drawString(-RR, RR,'NW')
    canvas.drawString( RR,-RR,'SE')
    canvas.drawString(0,-RR,'S')
    canvas.drawString(RR,0,'E')
    canvas.drawString(-RR,0,'W')
    for ii in range(0,30,5):
        canvas.rect(0,0,WIDTH-ii, HEIGHT-ii)   
    canvas.setFont("Courier", 128)
    canvas.drawCentredString(WIDTH/2,HEIGHT/2,'open')
class StateCM(Canvas):
    """Context manager to restore state"""

    def __init__(s,canvas): 
        s.canvas = canvas

    def __enter__(s): 
        s.canvas.saveState()

    def __exit__(s, aType, aValue, aTraceback): 
        s.canvas.restoreState()

class LeftHalfCM(StateCM):
    def __enter__(self):
        StateCM.__enter__(self)
        self.canvas.translate(WIDTH,0)
        self.canvas.rotate(90)
        self.canvas.scale( 1/RATIO, 1/RATIO )    

class RightHalfCM(StateCM):
    def __enter__(self):
        StateCM.__enter__(self)
        self.canvas.translate(WIDTH,0)
        self.canvas.rotate(90)
        self.canvas.scale( 1/RATIO, 1/RATIO )    
        self.canvas.translate(WIDTH,0)

if __name__=='__main__':
    main()

