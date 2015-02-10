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
theFont = "LucidaGrande"
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

def handle(lPoint, handle):
    strokeWidth(.4)
    stroke(1, 0, 0, .3)
    line(lPoint, handle)

def drawHandles(path, dm = 3, alpha = 1):
    save()

    for contour in path.contours[:]:
        lPoint = contour[0][0]
        strokeWidth(dm/5)
        for segment in contour:
            if len(segment) > 1:
                fHandle = segment[0]
                handle(lPoint, fHandle)
                
                lPoint = segment[2]
                sHandle = segment[1]
                handle(lPoint, sHandle)
                
                fill(0,.6,1, alpha)
                stroke(None)
                oval(fHandle[0]-dm/3, fHandle[1]-dm/3, dm, dm)
                oval(sHandle[0]-dm/3, sHandle[1]-dm/3, dm, dm)
            else:
                lPoint = segment[0]
            fill(1,.3,0, alpha)
            rect(lPoint[0]-dm/2, lPoint[1]-dm/2, dm, dm)
            fontSize(labelSize)
            text(str(int(lPoint[0])) + "/" + str(int(lPoint[1])), (lPoint[0] + shiftX, lPoint[1] + shiftY))
    restore()


drawHandles(path)
    
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
    
