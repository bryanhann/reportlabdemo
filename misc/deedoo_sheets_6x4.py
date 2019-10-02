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





def drawpage(basehour,c):
    def yyy(ii):
        SEP = 36
        MARGIN = 9
        return -(ii+1)* SEP - MARGIN

    c.rotate(90)
    c.setFont("Courier",22)
    c.drawRightString(830,yyy(0)+12, YYMMDD)
    for ii in range(16):
        c.line(0, yyy(ii), 850, yyy(ii))
        h, m = divmod(ii,4)
        hour = basehour + h
        minute = m * 15
        hhmm = make_hhmm(hour,minute)
        code = code4hhmm(hhmm)
        show = '%s %s' % (hhmm, code4hhmm(hhmm))
        c.drawString(5,yyy(ii)+12, show)
    c.showPage()

        

if __name__=='__main__':
    c= canvas.Canvas('foo.pdf', pagesize=A4)
    YYMMDD = sys.argv[1]                               
    for hour in range(0,24,4):
        drawpage(hour,c)
    c.save()

