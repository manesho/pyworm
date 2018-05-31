from numpy import random as rnd
from collections import namedtuple

#defining the data structure
Event = namedtuple('Event', 'time, spins, transitionto, kind')

class Site(object):
		def __init__(self,coord=(0,0), initialspin=0,neighbours=[(0,0),(0,0),(0,0),(0,0)],
						isfundamental=0, tmax=1 ):
			self.eventlist=[Event(time=0, 
						   spins={"BWD":initialspin, "FWD":initialspin},
						   transitionto=None,
						   kind = "boundary") ,
				   		Event( time= tmax, 
						   spins={"BWD":initialspin, "FWD":initialspin},
						   transitionto=None,
						   kind = "boundary")]
			self.isfundamental = isfundamental
			self.neighbours =  neighbours

		def find_event_at(self, time):
			for event in self.eventlist:
					if event.time == time:
						return event
			#if there is none: error
			print("no event at time ", time)
			return None
		
		def find_spin_at(self,time):
			for event in self.eventlist:
					if event.time == time:
						print("ther is an event at ", time)
						return None
					if event.time > time:
						return event.spins["BWD"]
			print("looped trhough the lattice never reached time ", time)
			return None
		
		def find_event_in_dir(self,time, direction):
			# go to the first event after time
			i=0
			while self.eventlist[i].time < time:
				i=i+1

			if self.eventlist[i].time == time:
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
			while self.eventlist[i].time < time:	
				i=i+1
			# check wether ther is already one there:	
			if self.eventlist[i].time == time:
					print("there is already an event at t=", time)
					return 
			else:
					self.eventlist.insert(i, 
									Event(time=time, spins=spins, transitionto=transitionto, kind=kind))

		def delete_event_at(self, time):
			i=0
			while self.eventlist[i].time != time:
					i=i+1
			if self.eventlist[i].time == time:
					self.eventlist.pop(i)
			else:
					print("no event found at t", time)
			

class Lattice(object):
	def __init__(self, beta=1,s1=2, s2=2, ics=[1,1]):
			self.s1 =s1
			self.s2 =s2
			self.nsites = s1*s2
			self.beta = beta
			#work with integer time:
			self.tmax = 10000000000
			self.sites= {(x1,x2):Site(coord =(x1,x2),
									initialspin = ics[self.isfund(x1,x2)],
									neighbours =self.nblist(x1,x2),
									isfundamental= self.isfund(x1,x2),
									tmax= self.tmax,
									)
							for x1 in range(0,self.s1) for x2 in range(0, self.s2)}
	
	def nblist(self,x1,x2):
			return [((x1+1)%self.s1, x2),((x1-1)%self.s1, x2),(x1,(x2+1)%self.s2),(x1,(x2-1)%self.s2)]
	
	def isfund(self,x1,x2):
				if x1%2==x2%2:
						return 1
				else:
						return 0
	def t3squared(self):
			t3 =0.
			t3local =0.12
			for coord, site in self.sites.items():
					#u or ubar
					if site.eventlist[0].spins["FWD"] == 0:
							if site.isfundamental == 1:
								t3local = 0.5
							else:
								t3local = -0.5
					else: #d or dbar
							if site.isfundamental == 1:
								t3local = -0.5
							else:
								t3local = 0.5
					t3 = t3+ t3local
			return t3*t3


class Worm(object):
		def __init__(self, lattice):
				self.lattice = lattice
				
				self.headx = (0,0)
				self.tailx = self.headx
				self.headt = int(round(rnd.uniform()*lattice.tmax))
				self.tailt = self.headt
				if rnd.uniform()>0.5:
					self.direction ="FWD"
					self.reversedirection = "BWD"
				else:
					self.direction ="BWD"
					self.reversedirection = "BWD"

				self.closed =False

				#add an event for the tail:
				prevspin = self.lattice.sites[self.tailx].find_spin_at(self.tailt)
				tailspins = {"FWD":prevspin, "BWD":prevspin}
				tailspins[self.direction] = self.newspin( prevspin)
				self.lattice.sites[self.tailx].add_event_at(self.tailt, tailspins, None, "tail")
		def decayconst(self,spin1,spin2):
				if spin1==spin2:
						return 0.5
				else:
						return 0

		def newspin(self,oldspin):
			if oldspin == 0:
				return 1
			else:
				return 0
 		
		def sampledectime(self,decconsts, dt):
			if sum(decconsts)!=0:
				#t as it should be:
				tfloat = rnd.exponential(1/sum(decconsts)) 
				ts = int(round((tfloat / self.lattice.beta) * self.lattice.tmax))
			else:
				ts = dt
			return ts

		def choose_decnb(self, decconsts):
			cumprob =0
			rnum =rnd.uniform()
			for i in range(4):
				cumprob = cumprob + decconsts[i]/sum(decconsts)		
				if cumprob >= rnum:
					return i

		def flip_dir(self):
				if self.direction == "FWD":
					self.direction ="BWD"
					self.reversedirection = "BWD"
				else:
					self.direction ="FWD"
					self.reversedirection = "FWD"
	

		def step(self):
			
			#first find the closest events in the direction on the current and the neighbour sites:
			nbs = self.lattice.sites[self.headx].neighbours;
			nbnextevents = [self.lattice.sites[nb].find_event_in_dir(self.headt, self.direction) for nb in nbs]
			csnextevent = self.lattice.sites[self.headx].find_event_in_dir(self.headt,self.direction)
			
			dtnbs = [abs(ev.time - self.headt) for ev in nbnextevents ]
			dtc = abs(csnextevent.time - self.headt)
			dt = min(min(dtnbs), dtc)
			
			# identify the spins:
			if self.direction == "FWD":
				spinc = csnextevent.spins["BWD"]
				spinnbs = [ev.spins["BWD"] for ev in nbnextevents ]
			else:
				spinc = csnextevent.spins["FWD"]
				spinnbs = [ev.spins["FWD"] for ev in nbnextevents ]

			# identify the decayconstants
			decconsts = [self.decayconst(spinc, s2) for s2 in spinnbs]
			t = self.sampledectime(decconsts, dt)
			# if the time is smaller than dr -> jump
			if t < dt:
				#print("decay")
				if self.direction == "FWD":
					t2jump = self.headt + t
				else:
					t2jump = self.headt -t
				
				#choose a decayneighbour:
				nbindex = self.choose_decnb(decconsts)
				decaynbcoord = nbs[nbindex]
				# add an event on the current site:
				newspins = {"FWD":self.newspin(spinc), "BWD":self.newspin(spinc)}
				newspins[self.direction] = spinc
				self.lattice.sites[self.headx].add_event_at(t2jump,newspins,decaynbcoord,"transition")
				# add an event on the neighbour site
				newspins = {"FWD":self.newspin(spinnbs[nbindex]), "BWD":self.newspin(spinnbs[nbindex])}
				newspins[self.direction] = spinnbs[nbindex]
				self.lattice.sites[decaynbcoord].add_event_at(t2jump,newspins,self.headx,"transition")
				# move the worm head:
				self.headt = t2jump
				self.headx = decaynbcoord
				self.flip_dir()
				return 0
			
			#if the next event is on the current site
			if dtc == dt:
				#print("process event")
				nextevtime = self.headt+dt if self.direction=="FWD" else self.headt-dt
				evccoord = self.headx
				eventtoprocess = self.lattice.sites[evccoord].find_event_at(nextevtime)
				if eventtoprocess.kind == "boundary":
						#print("bdry")
						newspin = self.newspin(spinc)
						eventtoprocess.spins["FWD"]=newspin
						eventtoprocess.spins["BWD"]=newspin
						#update the other boundary as well:
						otherboundarytime = 0 if nextevtime == self.lattice.tmax else self.lattice.tmax
						otherboundaryevent = self.lattice.sites[evccoord].find_event_at(otherboundarytime)
						self.headt = otherboundarytime
						otherboundaryevent.spins["FWD"]=newspin
						otherboundaryevent.spins["BWD"]=newspin
						return 0
				if eventtoprocess.kind == "transition":
						#print("trns")
						self.headt = nextevtime
						self.headx = eventtoprocess.transitionto
						self.flip_dir()
						#delete the event
						self.lattice.sites[self.headx].delete_event_at(nextevtime)
						self.lattice.sites[evccoord].delete_event_at(nextevtime)
						return 0
				if eventtoprocess.kind == "tail":
						#print("tail")
						self.lattice.sites[self.headx].delete_event_at(nextevtime)
						self.closed = True
						return 1
			
			# if not: move the head
			#print("justmove")
			self.headt = self.headt+dt if self.direction=="FWD" else self.headt-dt
			return 0

		def run(self):
			while self.closed == False:
				self.step()

def launch_simulation(beta =1 , termsteps=1000, wormruns = 10000):
		lattice = Lattice(beta=beta, s1 =2,s2=2, ics=[0,0])
		t3sq = int(0)
		for i in range(termsteps):
			w = Worm(lattice)
			w.run()
		for i in range(wormruns):
			w=Worm(lattice)
			w.run()
			t3sq = t3sq + int(lattice.t3squared())

		return t3sq/wormruns
