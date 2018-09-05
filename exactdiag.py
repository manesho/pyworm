from numpy import exp, sinh, sqrt

#copy pasted from mathematica
def t3_su3(beta=1,mu3=0,J=1):
	return (2*exp(beta*mu3)*(2 + 4*exp((beta*mu3)/2) + 2*exp(beta*mu3) + 4*exp((3*beta*mu3)/2) + 2*exp(2*beta*mu3) + exp(beta*(J + mu3)) + 2*exp(beta*(3*J + mu3)) + exp(beta*(5*J + mu3)))*(sinh((beta*mu3)/2) + sinh(beta*mu3)))/(1 + 4*exp((beta*mu3)/2) + 6*exp(beta*mu3) + 8*exp((3*beta*mu3)/2) + 9*exp(2*beta*mu3) + 8*exp((5*beta*mu3)/2) + 6*exp(3*beta*mu3) + 4*exp((7*beta*mu3)/2) + exp(4*beta*mu3) + exp(beta*(J + mu3)) + 2*exp(3*beta*(J + mu3)) + 4*exp((3*beta*(2*J + mu3))/2) + exp(2*beta*(2*J + mu3)) + 2*exp((5*beta*(2*J + mu3))/2) + 2*exp(beta*(3*J + mu3)) + exp(2*beta*(4*J + mu3)) + exp(beta*(5*J + mu3)) +  2*exp(beta*(J + 2*mu3)) + exp(beta*(J + 3*mu3)) + 2*exp(beta*J + (3*beta*mu3)/2) + 2*exp(5*beta*J + (3*beta*mu3)/2) + 4*exp(3*beta*J + 2*beta*mu3) + 2*exp(5*beta*J + 2*beta*mu3) + 2*exp(beta*J + (5*beta*mu3)/2) + 4*exp(3*beta*J + (5*beta*mu3)/2) + exp(5*beta*J + 3*beta*mu3))

def t3_su3_sq(beta=1, mu3=0, J=1):
	return (8 + 18*exp((beta*mu3)/2) + 12*exp(beta*mu3) + 4*exp((3*beta*mu3)/2) + 4*exp((5*beta*mu3)/2) + 12*exp(3*beta*mu3) + 18*exp((7*beta*mu3)/2) + 8*exp(4*beta*mu3) + 2*exp(beta*(J + mu3)) + 4*exp(3*beta*(J + mu3)) +   2*exp((3*beta*(2*J + mu3))/2) + exp((5*beta*(2*J + mu3))/2) + 4*exp(beta*(3*J + mu3)) + 2*exp(beta*(5*J + mu3)) + 2*exp(beta*(J + 3*mu3)) + exp(beta*J + (3*beta*mu3)/2) + exp(5*beta*J + (3*beta*mu3)/2) +   exp(beta*J + (5*beta*mu3)/2) + 2*exp(3*beta*J + (5*beta*mu3)/2) + 2*exp(5*beta*J + 3*beta*mu3))/(2*(1 + 4*exp((beta*mu3)/2) + 6*exp(beta*mu3) + 8*exp((3*beta*mu3)/2) + 9*exp(2*beta*mu3) + 8*exp((5*beta*mu3)/2) +    6*exp(3*beta*mu3) + 4*exp((7*beta*mu3)/2) + exp(4*beta*mu3) + exp(beta*(J + mu3)) + 2*exp(3*beta*(J + mu3)) + 4*exp((3*beta*(2*J + mu3))/2) + exp(2*beta*(2*J + mu3)) + 2*exp((5*beta*(2*J + mu3))/2) + 2*exp(beta*(3*J + mu3)) +    exp(2*beta*(4*J + mu3)) + exp(beta*(5*J + mu3)) + 2*exp(beta*(J + 2*mu3)) + exp(beta*(J + 3*mu3)) + 2*exp(beta*J + (3*beta*mu3)/2) + 2*exp(5*beta*J + (3*beta*mu3)/2) + 4*exp(3*beta*J + 2*beta*mu3) +   2*exp(5*beta*J + 2*beta*mu3) + 2*exp(beta*J + (5*beta*mu3)/2) + 4*exp(3*beta*J + (5*beta*mu3)/2) + exp(5*beta*J + 3*beta*mu3)))



def t8_su3(beta=1,mu8=0,J=1):
		return (
					(sqrt(3)*(-1 + exp(1/2*sqrt(3)*beta*mu8))*(1 + exp(1/2*sqrt(3)*beta*mu8))*
				    	(4 + exp(1/2*sqrt(3)*beta*mu8)*(6 + 4*exp(1/2*sqrt(3)*beta*mu8) + 
    				 	 exp(J*beta)*(1 + exp(2*J*beta))**2)))
				/
					(4 + 2*exp(beta*(J + sqrt(3)*mu8))*(2 + exp(1/2*sqrt(3)*beta*mu8)) +
						exp(1/2*sqrt(3)*beta*mu8)*(12 + 4*exp(3/2*sqrt(3)*beta*mu8) + 
  						2*exp(J*beta)*(1 + exp(2*J*beta))**2 + 2*exp(sqrt(3)*beta*mu8)*
						(6 + 2*exp(3*J*beta) + exp(5*J*beta)) + exp(1/2*sqrt(3)*beta*mu8)*
						(15 + 8*exp(3*J*beta) + exp(4*J*beta) + 4*exp(5*J*beta) + exp(8*J*beta))
						)) 
				)
