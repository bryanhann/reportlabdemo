import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
width, height = A4 
OUTPUT='output.pdf'

class Move:
    def __init__(self, canvas, dx=0.0, dy=0.0, zx=1.0, zy=1.0, theta=0.0):
        self.canvas = canvas
        self.dx=dx
        self.dy=dy
        self.zx=zx
        self.zy=zy
        self.theta=theta
    def __enter__(self):
#        print( self.dx, self.dy )
        self.canvas.translate(self.dx, self.dy)
        self.canvas.scale(self.zx, self.zy)
        self.canvas.rotate(self.theta)
    def __exit__(self, aType, aValue, aTraceback):
#        print( -self.dx, -self.dy )
        self.canvas.rotate(-self.theta)
        self.canvas.scale(1.0/self.zx, 1.0/self.zy)
        self.canvas.translate(-self.dx, -self.dy)

c = canvas.Canvas(OUTPUT)
c.setPageSize(A4)
    
def bush(n=0):
    if n <= 0:
        return
    n = n - 1
    my_height=100
    my_scale=0.7
    my_theta=20
    c.line(0,0,0,my_height)
    c.circle(0,my_height,5)
    c.drawString(0,my_height,repr(n))
    with Move(c, 0,my_height, my_scale,my_scale, -my_theta):
        bush( n )
    with Move(c, 0,my_height, my_scale,my_scale, my_theta):
        bush(n)
    c.line(0,0,20,0)

c.translate(width/2, height/2)
bush(14)
c.showPage()
c.save()
print('canvas saved to %s' % OUTPUT) 
