# ###################################################################
#
# points are the canvas points and change with the font size
#
# --> let me know if you have ideas for improving
# --> Mark Froemberg aka DeutschMark @ GitHub <--
#
# ToDO: - set and bind UPM with font size
#     - scale after for paper fit
#     - wait for solution for wrong vertical metrics*
#
# *) there is an apple issue with the font metrics. look for
# 'Querying Font Metrics' on
# https://developer.apple.com/library/mac/documentation/TextFonts/Conceptual/CocoaTextArchitecture/FontHandling/FontHandling.html
#
# ###################################################################

width, height = 400, 300
size(width, height)
string = "Iypl"
theFont = "Times"
fontS = 220
translate(10, 80)

### point colors
c1 = 1, 0, 0, .5
c2 = 0, .5, .5, .2

### label settings
shiftX = -2
shiftY = 4
labelSize = 4

# create a bezier path
path = BezierPath()
path.closePath()
fill(0,0,0, .3)
drawPath(path)

path.text(string, font=theFont, fontSize=fontS)

def drawPoints(fyll, strouk, dm, label):
    fill(*fyll)
    stroke(strouk)
    strokeWidth(.3)
    x, y = point
    oval(x-(dm/2), y-(dm/2), dm, dm)
    ### labels
    fontSize(labelSize)
    stroke(None)
    if label:
        text(str(int(x)) + "/" + str(int(y)), (x + shiftX, y + shiftY))

for point in path.onCurvePoints:
    drawPoints(c1, None, 4, True)

for point in path.offCurvePoints:
    drawPoints(c2, (.6), 3, False)
    
#################
### reset to displayed font instead of the label font
font(theFont)
fontSize(fontS)
lA = 0
lB = width
strokeWidth(.2)
stroke(2, 0, 0, .5)
for metric in (0, fontDescender(), fontAscender(), fontXHeight(), fontCapHeight()):
    line((lA, metric), (lB, metric))
    print metric
