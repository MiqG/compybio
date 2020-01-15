# load libraries
library(deSolve)

# define variables
  #time intervals
t_intv = seq(0,100, by= 0.1)
  # initial state
init_state = c(metA = 100, metB= 0, metC= 0, metD= 0, metE= 0, metF= 0, metG= 0)
  # parameters (rates)
rates = c(r1 = 0.15, r2 = 0.2, r3 = 0.8, r4 = 0.2, r5 = 0.4, r6 = 0.1, r7 = 0.01, r8 = 0.05)

  # stoichiometric matrix


# ode function
ode_system <- function(t,state,parameters){
  with(as.list(c(state,parameters)), {
   dA = (-1)*((-1)*r1*metA + (-1)*r2*metA^(1)) + (-1)*r3*metA
   dB = r1*metA -r4*metB -r5*metB
   dC = r2*metA -r6*metC
   dD = r3*metA -r7*metD -r8*metG
   dE = r4*metB
   dF = r5*metB + r6*metC + r7*metD + r8*metG
   dG = r8*metD
   list(c(dA,dB,dC,dD,dE,dF,dG))
  })
}

out = ode(y = init_state, times = t_intv, func = ode_system, parms = rates)

plot(out)
