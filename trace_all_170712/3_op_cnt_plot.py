#! /usr/bin/python2.7

from zplot import *
import sys


if len(sys.argv) < 3:
	print("Usage: ./.py all_op_cnt swift")
	exit(0)

prefix=sys.argv[1]
t = table(prefix + '.data')
ctype = 'eps'
#ctype = 'pdf'

bench=sys.argv[2]

### ymax 
ymax=0
#col = ['B', 'S', 'L', 'E','SBGL', 'SBFL']
col = [bench]
for c in col:
    ymax = ymax if t.getmax(c) < ymax else t.getmax(c)

ymax = ymax + ymax * 0.1
print(ymax)

#### ymax round 
round_ymax = 0 
round_scale = 10 if ymax < 100 else 100 

while round_ymax < ymax:
    round_ymax += round_scale

print(round_ymax)
ymax=round_ymax


outprefix = bench + "/" + bench + "_op_cnt"
c = canvas(ctype, outprefix, dimensions=['6in', '4in'])
#c = canvas(ctype, prefix, dimensions=['6in', '4in'])
#c = canvas(ctype, prefix, dimensions=['3.5in', '2.95in'])
d = drawable(c, yrange=[-1.5, t.getmax('rownumber')+1.5], xrange=[0,ymax],
	coord=[100,40]
	)
#yrange=[0, t.getmax('time')*1.2])

axis(d, style='box', ymanual=t.query(select='func, rownumber'),
		xtitle='count(#)',
		#xlabelrotate=90, xlabelanchor='r,c',
		title=bench, 
		#ytitle='func',
		xauto=[0, ymax, ymax/5]
#		yauto=[0, 100, 10]

	)
p = plotter()
L = legend()


barargs = {'drawable':d, 'table':t, 'xfield':bench,
	    'yfield':'rownumber', 'fill':True, 'barwidth':0.8,
#	    'labelfield':'swift',	
	    'fillsize': 0.5, 'fillstyle':'solid', 'fillcolor':'black'}

p.horizontalbars(**barargs)

c.render()

#####
from subprocess import call
call(["open", outprefix + ".eps"])

#
#
#
#options = [('ORG', 'lightsalmon', 0.5), ('TCR', 'darkblue', 0.5)]
##c = postscript('fig1.eps'i
#ctype = 'eps' 
##if len(sys.argv) < 2 else sys.argv[1]
##c = canvas(ctype, 'fig1', dimensions=['3.5in', '2.95in'])
#
#c = canvas(ctype, 'fig2_exec_time', dimensions=[240,220])
##c = canvas(ctype, 'fig1-pattern', dimensions=['3.5in', '2in'])
#d = drawable(c, xrange=[-0.5, t.getmax('rownumber')+2.5], yrange=[0,30000], dimensions=[160,120], coord=[60,70])
#
##axis(d, xtitle='Cache size', ytitle='exec_time', yauto=[0,200,100])
#axis(d, style='box', 
##       xtitle='Cache size', 
#        xlabelrotate=90,
#        xlabelanchor='r,c',
#        xmanual=[['DELETE', 1],['PERSIST', 4], ['TRUNCATE', 7], ['WAL', 10]], ytitle='Execution Time(s)', yauto=[0,30000,10000])
##axis(d, xtitle='Cache size', xmanual=t.query(select='opt,rownumber'), ytitle='exec_time', yauto=[0,200,100])
#
#p = plotter()
#L = legend()
#
#offset = 0 
#
#for opt, fcolor, fsize, in options:
##       st = table(table=t, where='buff="bsize"')
#        w = 'opt="%s"' % opt 
##       print(w)
#        st = table(table=t, where=w)
##       st = table(table=t, where='buff="256M"')
#        barargs = {'drawable':d, 'table':st, 'xfield':'rowline', 
#                        'yfield':'exec_time', 'fill':True, 'barwidth':0.8, 
#                        'fillsize':fsize, 'fillstyle':'solid', 'fillcolor':fcolor,
#                        'legend':L, 'legendtext':opt}
#
##       barargs = {'drawable':d, 'table':st, 'xfield':'rownumber', 
#        p.verticalbars(**barargs)
#        offset += st.getmax('rownumber')
#
#L.draw(c, coord=[d.left()+20, 
##:      labelfontsize=7,
#        d.top()-20], skipnext=3, skipspace=40)
#
#
#c.render()
#
