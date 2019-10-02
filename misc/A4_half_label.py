import time
import datetime
import os
from reportlab.pdfgen.canvas import Canvas
import reportlab.lib.pagesizes
import sys
try:
    TEXT=sys.argv[1]
except IndexError:
    print( 'please supply a string to print' )
    exit()
FILENAME = 'tmp.pdf'
A4 = reportlab.lib.pagesizes.A4
WIDTH,HEIGHT = A4

def main():
    canvas = Canvas(FILENAME)
    canvas.setFont("Courier", 8)
    canvas.setPageSize(A4)
    c = canvas
    canvas.line(0,HEIGHT/2, WIDTH,HEIGHT/2)
    canvas.setFont("Courier", 30)
    canvas.drawString(10,(HEIGHT/2)-20, TEXT)
    canvas.showPage()
    canvas.save()
    print( 'canvas is auto saved to file', canvas._filename )
    time.sleep(1)
    os.system( 'open %s' % canvas._filename )
if __name__=='__main__':
    main()
