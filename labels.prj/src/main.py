import time
import os
import datetime
import reportlab
from reportlab.lib import colors 
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4

OUT='deleteme.pdf'
START=datetime.date(2016, 10, 5) # oct10 
DAYDELTA = datetime.timedelta(days=1)
CANVAS = canvas.Canvas(OUT, pagesize=A4)
TIMES = ['0400', '0800', '1200', '1600', '2000']

#try:
#        os.mkdir(TMP)
#except:
#        pass

RAINBOW=[
        colors.red,
        colors.orange,
        colors.yellow,
        colors.lightgreen,
        colors.lightblue,
        colors.lavender,
        colors.violet,
]



def box(myCanvas, the_date, jj, day  ):
    BOX_WIDTH=68.0
    BOX_HEIGHT=82.0
    hhmm = TIMES[jj]
    dx=day*BOX_WIDTH
    dy=A4[1]-BOX_HEIGHT*(jj+1)
    myCanvas.translate(dx,dy)
    myCanvas.setFillColor( RAINBOW[the_date.weekday()])
    
    myCanvas.rect(0,0,BOX_WIDTH,BOX_HEIGHT, stroke=1, fill=1)
    xx = BOX_WIDTH/2.0
    yy = BOX_HEIGHT
    myCanvas.setFillColorRGB(0,0,0)
    myCanvas.setFont('Courier', 20)
    myCanvas.drawCentredString(xx, yy-20,hhmm)
    myCanvas.setFont('Courier', 10)
    myCanvas.drawCentredString(xx,yy-40,the_date.strftime("%A"))
    myCanvas.drawCentredString(xx,yy-50,the_date.strftime("%b %d"))
    myCanvas.drawCentredString(xx,yy-60,the_date.strftime("week %W"))
    myCanvas.translate(-dx,-dy)

def main():
    for ii in range(7):
        theDate = START + DAYDELTA*ii 
        for jj in range(5):
            box(CANVAS, theDate, jj,ii,  )
    CANVAS.showPage()
    CANVAS.save()
if __name__ == '__main__':
    main()
