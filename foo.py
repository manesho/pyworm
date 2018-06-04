import numpy as np
class Site(object):
	def __init__(self,coord=(0,0), initialspin="u",neighbours=[(0,0),(0,0),(0,0),(0,0)],
						isfundamental=0, tmax=1 ):
			self.eventlist = np.array([(0,initialspin,initialspin,"bd",coord),
							   			(tmax,initialspin,initialspin,"bd",coord)],
									dtype = [('time', 'i8'), 
											 ('spinfwd', 'U1'),
											 ('spinbwd','U1'),
											 ('kind', 'U2'),
											 ('transitionnb', '(2,)i4')])

				
