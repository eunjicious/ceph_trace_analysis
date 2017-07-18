#! /usr/bin/env python

#
# This example creates a simple line graph. Using the data found
# in 'line.data', it makes a simple plot using all the basic features
# you'd expect to find in a zplot graph. The file is more commented
# than most you would likely create yourself.
#

from zplot import *


option=['noflush', 'flush', 'rflush']


styles = [
    ['orange',        'square',   True],
    ['lightblue',     'circle',   True],
    ['darkblue',      'triangle', True],
    ['olivedrab',     'utriangle',True],
    ['mediumpurple',  'diamond',  True],
    ['green',         'star',     True],
    ['lightsalmon',   'xline',    False],
    ['rosybrown',     'plusline', False],
    ['mistyrose',     'hline',    False],
    ['slateblue',     'vline',    False],
    ['lightcoral',    'asterisk', False],
    ['red',           'square',   False],
    ['green',         'circle',   False],
    ['brown',         'triangle', False],
    ['black',         'utriangle',False],
    ['gray',          'diamond',  False],
    ['darkcyan',      'dline1',   False],
    ['darkgoldenrod', 'dline2',   False],
]




for opt in option:
#	fname = 'fio_all_%s.resp' % opt
	fprefix = "fio_all_" + opt
	fdata = fprefix + ".resp"

	print(fdata)

	# populate zplot table from data file
	t = table(fdata)
	
	#c = postscript('flush.eps')
	ctype = 'eps'
#	c = canvas(ctype, 'flush', dimensions=[400, 300])
	c = canvas(ctype, fprefix, dimensions=[400, 300])

	# a drawable is a region of a c, and is used to convert data
	# coordinates to raw pixel coordinates on the c, based on
	# xrange and yrange.
	d = drawable(c, xrange=[-0.5,t.getmax('rownumber')+0.5], yrange=[0,800000], coord=[80,80], dimensions=[300,200])
#	d = drawable(c, xrange=[-0.5,t.getmax('rownumber')+0.5], yrange=[0,t.getmax('c0')], coord=[50,50])
	#d = drawable(c, xrange=[95,100], yrange=[0,800000], coord=[50,50])
	#d = drawable(c, xrange=[0,100], yrange=[0,100000], coord=[50,50])
	
	# create an axis for our drawable.  Specify axis labels with
	# [START,END,STEP] via xauto and yauto.
	axis(d, style='box', title=opt,
		xtitle='Percentile(th)', 
		xmanual=t.query(select='c0,rownumber'),
		xlabelrotate=90,
		xlabelanchor='r,c',
		ytitle='Response Time (s)', yauto=[0, 800000,100000])
#		ytitle='Response Time (s)', yauto=[0,t.getmax('c0'),100000])
	
	# a plotter fetches coordinates from the table, querying for the
	# specified xfield and yfield, and converting these via the drawable.
	p = plotter()
	
	# each thing we plot can be added to the legend
	L = legend()

	lg = {'c1':'async-256M', 'c2':'async-512M', 'c3':'async-1G', 'c4':'async-2G',
			'c13':'sync-256M', 'c14':'sync-512M', 'c15' : 'sync-1G', 'c16' : 'sync-2G'}

	# async 256 512 1024 2048 : c1 c2 c3 c4
	# sync 256 512 1024 2048 : c13 c14 c15 c16
	for i in range(4):
		color = styles[i][0]
		style = styles[i][1]
		fill = styles[i][2]
		ycol = "c%s" % str(i+1)

		p.line(d, t, xfield='rownumber', yfield=ycol, linecolor=color, linewidth=1)

		p.points(d, t, xfield='rownumber', yfield=ycol, 
			linewidth=0.5, style=style, linecolor=color, fill=fill, fillcolor=color,
			legend=L, legendtext=lg[ycol])

	for i in range(13,16):
		color = styles[i-8][0]
		style = styles[i-8][1]
		fill = styles[i-8][2]
		ycol = "c%s" % str(i+1)

		p.line(d, t, xfield='rownumber', yfield=ycol, linecolor=color, linewidth=1)

		p.points(d, t, xfield='rownumber', yfield=ycol, 
			linewidth=0.5, style=style, linecolor=color, fill=fill, fillcolor=color,
			legend=L, legendtext=lg[ycol])


	
	L.draw(c, coord=[d.left()+20, d.top()-10])
	
	# save to eps file
	c.render()
