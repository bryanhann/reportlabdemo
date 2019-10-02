#!/usr/bin/python

import md5
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def make_hhmm(hours, minutes):
    hours = int(hours)
    minutes = int(minutes)
    assert 0 <= hours < 24
    assert 0 <= minutes < 60
    hh = `100+hours`[-2:]
    mm = `100+minutes`[-2:]
    return hh+mm

def code4hhmm(hhmm):
    m = md5.new()
    m.update(hhmm)
    return m.hexdigest()[:4]

def hhmm4code(code):
    for hour in range(24):
        for minute in range(0,60,5):
            hhmm = make_hhmm(hour,minute)
            if code==code4hhmm(hhmm):    
                return hhmm

def test():
    for hh in range(24):
        for mm in range(0,60,5):
            hhmm1 = make_hhmm(hh,mm)
            code = code4hhmm(hhmm1)
            hhmm2 = hhmm4code(code)
            print hhmm1, hhmm2, code4hhmm(hhmm1), code4hhmm(hhmm2)
            assert hhmm1==hhmm2






def drawpage_one_column(c):
    def yyy(ii):
        SEP = 8.5
        MARGIN =9 
        return 840 - (ii+1)* SEP - MARGIN
    basehour=0
    c.setFont("Courier",8)
    c.drawRightString(830,yyy(0)+12, 'YYMMDD')
    c.line(0, yyy(-1), 850, yyy(-1))
    for ii in range(96):
        c.line(0, yyy(ii), 850, yyy(ii))
        h, m = divmod(ii,4)
        hour = basehour + h
        minute = m * 15
        hhmm = make_hhmm(hour,minute)
        code = code4hhmm(hhmm)
        show = '%s %s' % (hhmm, code4hhmm(hhmm))
        c.drawString(40,yyy(ii)+1.5, show)
        c.drawString(300,yyy(ii)+1.5, show)
    c.showPage()




def show(h,m):
        hour = h
        minute = m * 15
        hhmm = make_hhmm(hour,minute)
        code = code4hhmm(hhmm)
        show = '%s %s' % (hhmm, code4hhmm(hhmm))
        return show

def drawpage(c,title):
    def yyy(ii):
        SEP = 17
        MARGIN =18 
        return 840 - (ii+1)* SEP - MARGIN
    c.setFont("Courier",20)
    c.drawString(40,yyy(-1)+4, title)
    basehour=4
    c.setFont("Courier",12)
    c.drawRightString(830,yyy(0)+12, 'YYMMDD')
    c.line(0, yyy(-1), 850, yyy(-1))
    for ii in range(0,48):
        c.line(0, yyy(ii), 850, yyy(ii))
    for ii in range(0,48):
        h, m = divmod(ii,4)
        h = h + basehour
        c.drawString(40,yyy(ii)+4, show(h,m))

    for ii in range(0,48):
        h, m = divmod(ii,4)
        h =  (h + basehour+ 12) % 24  
        print h
        c.drawString(300,yyy(ii)+4, show(h,m))
    c.showPage()

        

OUTFILE='foo.pdf'
if __name__=='__main__':
    title = sys.argv[1]
    c= canvas.Canvas(OUTFILE, pagesize=A4)
    
    drawpage(c,title)
    c.save()
    print "output written to %s" % OUTFILE
