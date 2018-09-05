from math import sqrt

def generate_decayrules(mu3=0,mu8=0):
	return general_decayrules(mu3,mu8)
		
#		mu0rules = {	"FWD":{"eq":{"=":0.5,"x":0,"b":0},
#										   	  "2f":{"=":0,"x":0,"b":0},
#											  "3f":{"=":0,"x":0,"b":0}
#											  },
#								   "BWD":{"eq":{"=":0.5,"x":0,"b":0},
#										   	  "2f":{"=":0,"x":0,"b":0},
#											  "3f":{"=":0,"x":0,"b":0}
#											  }
#					}
#
		#rules = { wtype:mu0rules for wtype in ["u>d","d>u", "u>s","s>u","d>s","s>d"] }

#		if mu3>=0 and mu3<=4:
#			return generate_decayrules_mu3lt4(mu3)
#		elif mu3>4 and mu3<=8:
#			return generate_decayrules_mu3lt8(mu3)
#		else:
#			print("invalid mu3 -> i set it to 0")
#			return generate_decayrules_mu3lt4(0)


def generate_2f_transitio_nrules(mu3=0,mu8=0):
#		mu0rules = {"FWD":{"=":1, "x":0},
#					"BWD":{"=":1, "x":0}}
#		rules = { wtype:mu0rules for wtype in ["u>d","d>u", "u>s","s>u","d>s","s>d"] }
	return generate_general2ftransitionrules(mu3,mu8)
#		if mu3>=0 and mu3<=4:
#			return generate_2f_transition_rules_mu3lt4(mu3)
#		elif mu3>4 and mu3 <=8:
#			return generate_2f_transition_rules_mu3lt8(mu3)
#		else:
#			print("invalid mu3 -> i set it to 0")
#			return generate_decayrules_mu3lt4(0)



def general_decayrules(mu3,mu8):
		u2dfwd = {	"eq":{"=":0.5 if mu3>0 else max((4+mu3)/8,0),
						  "x":0,
						  "b":max(mu3/4,0.)},
					"2f":{"=":0., 
						  "x":0.5 if mu3>4 else max(mu3/8., 0.),
						  "b":max(-1+mu3/4.,0.)	},
					"3f":{"=":0., 
						  "x":0., 
						  "b":max(mu3/4.,0.)	}
				  }
		d2ufwd = {	"eq":{"=":0.5 if mu3>0 else max((4-mu3)/8, 0.),
						  "x":0, 	
						  "b":max(-mu3/4.,0.)		},
					"2f":{"=":0, 	
						  "x":0.5 if mu3< -4. else max(-mu3/8., 0),
						  "b":max(-1-mu3/4,0.)		},
					"3f":{"=":0., 
						  "x":0., 
						  "b":max(-mu3/4.,0.)	}
				  }
		d2sfwd = {	"eq":{"=":0.5 if mu8*sqrt(3) > mu3 else max((8-mu3+sqrt(3)*mu8)/16.,0.),
						  "x":0,
						  "b":max((-mu3+sqrt(3)*mu8)/8.,0.)		},
					"2f":{"=":0,
						  "x":0.5 if mu8*sqrt(3)>8+mu3 else max((sqrt(3)*mu8-mu3)/16,0.),
						  "b":max((-8-mu3+sqrt(3)*mu8)/8.,0.)		},
					"3f":{"=":0, 		 
						  "x":0, 
						  "b":max((-mu3+sqrt(3)*mu8)/8.,0.)	}
				  }
		s2dfwd = {	"eq":{"=":0.5 if -mu8*sqrt(3) > -mu3 else max((8+mu3-sqrt(3)*mu8)/16.,0.),
						  "x":0,
						  "b":max((mu3-sqrt(3)*mu8)/8.,0.)		},
					"2f":{"=":0,
						  "x":0.5 if mu8*sqrt(3) +8<mu3 else max((-sqrt(3)*mu8+mu3)/16,0.),
						  "b":max((-8+mu3-sqrt(3)*mu8)/8.,0.)		},
					"3f":{"=":0, 		 
						  "x":0, 
						  "b":max((mu3-sqrt(3)*mu8)/8.,0.)	}
				  }

		u2sfwd = {	"eq":{"=":0.5 if mu8*sqrt(3) > -mu3 else max((8+mu3+sqrt(3)*mu8)/16.,0.),
						  "x":0,
						  "b":max((mu3+sqrt(3)*mu8)/8.,0.)		},
					"2f":{"=":0,
						  "x":0.5 if mu8*sqrt(3)>8-mu3 else max((sqrt(3)*mu8+mu3)/16,0.),
						  "b":max((-8+mu3+sqrt(3)*mu8)/8.,0.)		},
					"3f":{"=":0, 		 
						  "x":0, 
						  "b":max((mu3+sqrt(3)*mu8)/8.,0.)	}
				  }

		s2ufwd = {	"eq":{"=":0.5 if -mu8*sqrt(3) > mu3 else max((8-mu3-sqrt(3)*mu8)/16.,0.),
						  "x":0,
						  "b":max((-mu3-sqrt(3)*mu8)/8.,0.)		},
					"2f":{"=":0,
						  "x":0.5 if mu8*sqrt(3) +8<-mu3 else max((-sqrt(3)*mu8-mu3)/16,0.),
						  "b":max((-8-mu3-sqrt(3)*mu8)/8.,0.)		},
					"3f":{"=":0, 		 
						  "x":0, 
						  "b":max((-mu3-sqrt(3)*mu8)/8.,0.)	}
				  }



		rules = {"u>d":{"FWD":u2dfwd, "BWD":d2ufwd},
				 "d>u":{"FWD":d2ufwd, "BWD":u2dfwd},
				 "d>s":{"FWD":d2sfwd, "BWD":s2dfwd},
				 "s>d":{"FWD":s2dfwd, "BWD":d2sfwd},
				 "u>s":{"FWD":u2sfwd, "BWD":s2ufwd},
				 "s>u":{"FWD":s2ufwd, "BWD":u2sfwd}
				 }
		return rules



def generate_decayrules_mu3lt4(mu3):
		u2dfwd = {	"eq":{"=":0.5, 		 "x":0, 		"b":mu3/4	},
					"2f":{"=":0, 		 "x":mu3/8, 	"b":0		},
					"3f":{"=":0, 		 "x":0, 		"b":mu3/4	}
				  }
		d2ufwd = {	"eq":{"=":(4-mu3)/8, "x":0, 		"b":0		},
					"2f":{"=":0, 		 "x":0,			"b":0		},
					"3f":{"=":0, 		 "x":0, 		"b":0	}
				  }
		d2sfwd = {	"eq":{"=":(8-mu3)/16,"x":0, 		"b":0		},
					"2f":{"=":0, 		 "x":0,			"b":0		},
					"3f":{"=":0, 		 "x":0, 		"b":0	}
				  }
		s2dfwd = {	"eq":{"=":0.5, 		 "x":0, 		"b":mu3/8	},
					"2f":{"=":0, 		 "x":mu3/16, 	"b":0		},
					"3f":{"=":0, 		 "x":0, 		"b":mu3/8	}
				  }
		u2sfwd = s2dfwd;
		s2ufwd = d2sfwd;

		rules = {"u>d":{"FWD":u2dfwd, "BWD":d2ufwd},
				 "d>u":{"FWD":d2ufwd, "BWD":u2dfwd},
				 "d>s":{"FWD":d2sfwd, "BWD":s2dfwd},
				 "s>d":{"FWD":s2dfwd, "BWD":d2sfwd},
				 "u>s":{"FWD":u2sfwd, "BWD":s2ufwd},
				 "s>u":{"FWD":s2ufwd, "BWD":u2sfwd}
				 }
		return rules

def generate_decayrules_mu3lt8(mu3):
		u2dfwd = {	"eq":{"=":0.5, 		 "x":0, 		"b":mu3/4		},
					"2f":{"=":0, 		 "x":0.5, 		"b":(mu3-4)/4	},
					"3f":{"=":0, 		 "x":0, 		"b":mu3/4		}	
				  }
		d2ufwd = {	"eq":{"=":0,		 "x":0, 		"b":0			},
					"2f":{"=":0, 		 "x":0,			"b":0			},
					"3f":{"=":0, 		 "x":0, 		"b":0			}
				  }
		d2sfwd = {	"eq":{"=":(8-mu3)/16,"x":0, 		"b":0		},
					"2f":{"=":0, 		 "x":0,			"b":0		},
					"3f":{"=":0, 		 "x":0, 		"b":0	}
				  }
		s2dfwd = {	"eq":{"=":0.5, 		 "x":0, 		"b":mu3/8	},
					"2f":{"=":0, 		 "x":mu3/16, 	"b":0		},
					"3f":{"=":0, 		 "x":0, 		"b":mu3/8	}
				  }
		u2sfwd = s2dfwd;
		s2ufwd = d2sfwd;

		rules = {"u>d":{"FWD":u2dfwd, "BWD":d2ufwd},
				 "d>u":{"FWD":d2ufwd, "BWD":u2dfwd},
				 "d>s":{"FWD":d2sfwd, "BWD":s2dfwd},
				 "s>d":{"FWD":s2dfwd, "BWD":d2sfwd},
				 "u>s":{"FWD":u2sfwd, "BWD":s2ufwd},
				 "s>u":{"FWD":s2ufwd, "BWD":u2sfwd}
				 }
		return rules


def generate_2f_transition_rules_mu3lt4(mu3):
		u2dfwd = {"=":1, "x":0}
		d2ufwd = {"=":1-mu3/4, "x":mu3/4}
		u2sfwd = {"=":1, "x":0}
		s2ufwd = {"=":1-mu3/8, "x":mu3/8}
		d2sfwd = s2ufwd
		s2dfwd = u2sfwd
		rules = {"u>d":{"FWD":u2dfwd, "BWD":d2ufwd},
				 "d>u":{"FWD":d2ufwd, "BWD":u2dfwd},
				 "d>s":{"FWD":d2sfwd, "BWD":s2dfwd},
				 "s>d":{"FWD":s2dfwd, "BWD":d2sfwd},
				 "u>s":{"FWD":u2sfwd, "BWD":s2ufwd},
				 "s>u":{"FWD":s2ufwd, "BWD":u2sfwd}
				 }
		return rules

def generate_2f_transition_rules_mu3lt8(mu3):
		u2dfwd = {"=":1, "x":0}
		d2ufwd = {"=":0, "x":1}
		u2sfwd = {"=":1, "x":0}
		s2ufwd = {"=":1-mu3/8, "x":mu3/8}
		d2sfwd = s2ufwd
		s2dfwd = u2sfwd
	
		rules = {"u>d":{"FWD":u2dfwd, "BWD":d2ufwd},
				 "d>u":{"FWD":d2ufwd, "BWD":u2dfwd},
				 "d>s":{"FWD":d2sfwd, "BWD":s2dfwd},
				 "s>d":{"FWD":s2dfwd, "BWD":d2sfwd},
				 "u>s":{"FWD":u2sfwd, "BWD":s2ufwd},
				 "s>u":{"FWD":s2ufwd, "BWD":u2sfwd}
				 }
		return rules
			
						
						
											
						
def generate_general2ftransitionrules(mu3,mu8):
		d2ufwd = {"=":min(1., max(0., 1-mu3/4.)), "x":1-min(1., max(0., 1-mu3/4.))}
		u2dfwd = {"=":min(1., max(0., 1+mu3/4.)), "x":1-min(1., max(0., 1+mu3/4.))}
		d2sfwd = {"=":min(1., max(0., 1./8.  * (8-mu3+sqrt(3)*mu8))),
				  "x":1-min(1., max(0., 1./8.* (8-mu3+sqrt(3)*mu8)))  }
		u2sfwd = {"=":min(1., max(0., 1./8.  * (8+mu3+sqrt(3)*mu8))),
				  "x":1-min(1., max(0., 1./8.* (8+mu3+sqrt(3)*mu8)))  }
		s2dfwd = {"=":min(1., max(0., 1./8.  * (8+mu3-sqrt(3)*mu8))),
				  "x":1-min(1., max(0., 1./8.* (8+mu3-sqrt(3)*mu8)))  }
		s2ufwd = {"=":min(1., max(0., 1./8.  * (8-mu3-sqrt(3)*mu8))),
				  "x":1-min(1., max(0., 1./8.* (8-mu3-sqrt(3)*mu8)))  }
		rules = {"u>d":{"FWD":u2dfwd, "BWD":d2ufwd},
				 "d>u":{"FWD":d2ufwd, "BWD":u2dfwd},
				 "d>s":{"FWD":d2sfwd, "BWD":s2dfwd},
				 "s>d":{"FWD":s2dfwd, "BWD":d2sfwd},
				 "u>s":{"FWD":u2sfwd, "BWD":s2ufwd},
				 "s>u":{"FWD":s2ufwd, "BWD":u2sfwd}
				 }
		return rules
		
