import numpy as np
class Site(object):
	def __init__(self,coord=(0,0), initialspin="u",neighbours=[(0,0),(0,0),(0,0),(0,0)],
						isfundamental=0, tmax=1 ):
			
		self.isfundamental = isfundamental
		self.neighbours = neighbours
		self.eventlist = np.array([(0,initialspin,initialspin,"bd",coord),
							   			(tmax,initialspin,initialspin,"bd",coord)],
									dtype = [('time', 'i8'), 
											 ('spinfwd', 'U1'),
											 ('spinbwd','U1'),
											 ('kind', 'U2'),
											 ('transitionnb', '(2,)i4')])

		def find_event_at(self, time):
			for event in self.eventlist:
					if event['time'] == time:
						return event
			#if there is none: error
			print("no event at time ", time)
			return None
		
		def find_spin_at(self,time):
			for event in self.eventlist:
					if event['time'] == time:
						print("ther is an event at ", time)
						return None
					if event['time'] > time:
						return event.spins["BWD"]
			print("looped trhough the lattice never reached time ", time)
			return None
		
		def find_event_in_dir(self,time, direction):
			# go to the first event after time
			i=0
			while self.eventlist[i]['time'] < time:
				i=i+1

			if self.eventlist[i]['time'] == time:
				if direction == "FWD":
					return self.eventlist[i+1]
				else:
					return self.eventlist[i-1]
			else:
				if direction == "FWD":
					return self.eventlist[i]
				else:
					return self.eventlist[i-1]

			

		def add_event_at(self, time, spins, transitionto, kind):
			# go to the first event after time
			i=0
			while self.eventlist[i]['time'] < time:	
				i=i+1
			# check wether ther is already one there:	
			if self.eventlist[i]['time'] == time:
					print("there is already an event at t=", time)
					return 
			else:
					self.eventlist.insert(i, 
									Event(time=time, spins=spins, transitionto=transitionto, kind=kind))

		def delete_event_at(self, time):
			i=0
			while self.eventlist[i]['time'] != time:
					i=i+1
			if self.eventlist[i]['time'] == time:
					self.eventlist.pop(i)
			else:
					print("no event found at t", time)
			


