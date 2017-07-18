#! /usr/bin/python2.7

from zplot import *


def get_ymax(coll_list, t):
	ymax=0

	for c in coll_list:
		ymax = ymax if t.getmax(c) < ymax else t.getmax(c)

	ymax = ymax + ymax * 0.1 

	round_ymax = 0 
	round_scale = 10 if ymax < 100 else 100 

	while round_ymax < ymax:
		round_ymax += round_scale
	
	print(round_ymax)

	return round_ymax


def plot_graph(prefix, coll):
	
	t = table(prefix + '.data')
	c = canvas('eps', prefix + "-" + coll, dimensions=['3.8in', '3in'])
	
	coll_list = [coll]
	ymax = get_ymax(coll_list, t)
	d = drawable(c, xrange=[0, t.getmax('rownumber')+2], yrange=[0, ymax])
	#d = drawable(c, xrange=[0, t.getmax('rownumber')+2], yrange=[0, t.getmax(coll)])
	
	p = plotter()
	
	L = legend()
	
	options = [('filestore', 'red'), ('bluestore', 'blue')]
	
	cond = 'store="%s"' % "filestore"
	axis(d, style='box', ytitle=coll, xmanual=t.query(select='wor, line', where=cond),
		yauto=[0,ymax,ymax/10], title=prefix
	)
	for store, color in options:
	
		cond = 'store="%s"' % store
	
		subt = table(table=t, where=cond)
	
		barargs = {'drawable':d, 'table':subt,
					'xfield' : 'line', 'yfield' : coll,
					'labelfield' : coll,
					'fill':True, 'barwidth': 0.8,
					'fillsize' : 0.5, 'fillcolor': color, 
					'legend' : L, 'legendtext' : store
				}
	
		p.verticalbars(**barargs)
	
	#			'fill':True, 'barwidth':0.8, 
	#			'fillsize' : 1, 'fillstyle':'hline','fillcolor':'red',
	#			'legend' : L, 'legendtext':"tmp"
	#			}
	#
	L.draw(c, coord = [d.right()-60, d.top()-5], skipnext=2, skipspace=40)
	c.render()
	
	
	### 
	from subprocess import call
	call(["open", prefix + "-" + coll + ".eps"])

###########
if __name__ == "__main__":
	workloads=["fio_write_1m", "fio_write_4k", "fio_read_1m", "fio_read_4k"]
	workloads=["rados-read", "rados-write"]
	for w in workloads:
		print w
		plot_graph(w, 'iops')
#		plot_graph(w, 'bw')
#		plot_graph(w, 'runt')






