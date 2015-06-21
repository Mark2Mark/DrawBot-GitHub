# ###################################################################
#
# Filter all installed Fonts by a certain feature
#
# --> let me know if you have ideas for improving
# --> Mark Froemberg aka DeutschMark @ GitHub <--
# --> www.markfromberg.com <--
#
# ###################################################################


# ===================================================================
#
# S E A R C H:
#
feature = "rlig"
#         ^ ^ ^ 
#         | | | 
# ===================================================================

import string
show = ''.join([ ''.join(c) for c in zip(string.uppercase, string.lowercase)])
dist = 18
x, y = 450, 10

fonts = installedFonts()

print "These fonts have got the \"%s\" feature:\n" % feature
for f in fonts:
    if feature in listOpenTypeFeatures(fontName=f):
        print f
        font(f)
        text(f + " " + show,  (10, 10))
        translate(0, dist)
        y += dist

size(x, y)
