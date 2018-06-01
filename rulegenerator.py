def generate_decayrules(mu3=0,mu8=0):
		mu0rules = {	"FWD":{"eq":{"=":0.5,"x":0,"b":0},
										   	  "2f":{"=":0,"x":0,"b":0},
											  "3f":{"=":0,"x":0,"b":0}
											  },
								   "BWD":{"eq":{"=":0.5,"x":0,"b":0},
										   	  "2f":{"=":0,"x":0,"b":0},
											  "3f":{"=":0,"x":0,"b":0}
											  }
					}

		rules = { wtype:mu0rules for wtype in ["u>d","d>u", "u>s","s>u","d>s","s>d"] }
		return rules

def generate_2f_transitio_nrules(mu3=0,mu8=0):
		mu0rules = {"FWD":{"=":1, "x":0},
					"BWD":{"=":1, "x":0}}
		rules = { wtype:mu0rules for wtype in ["u>d","d>u", "u>s","s>u","d>s","s>d"] }
		return rules

