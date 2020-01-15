#!/usr/bin/env python3

"""
**USAGE:**

        make_ode_function_R.py [coefficients_matrix] [rates_vector] [ode_function.R]
        
    INPUT: [coefficients_matrix] [rates_vector]
    OUTPUT: [ode_function_R_file]

Requirements: 
    - *coefficients_matrix*: tab format. First row contains a column called 'var_name' with the variable names, followed by the names of the reactions.
    
    - *rates_vector*: tab format. Two columns: 'r_name' and 'r_val'.
    
    - Dimensions of *coefficients_matrix* and *rates_vector* should allow matrix multiplication without considering the 'var_name' column in the coefficients_matrix.

"""
#### PARSING ARGUMENTS ####

# load libraries
import pandas as pd
import numpy as np
import sys
args = sys.argv

# parse arguments
    # coefficients
coefs = pd.read_csv(args[1],header=0,sep='\t')
    # out R script
ode_function_file = args[2]

#### SCRIPT ####

def make_ode_term_str(coefficient_value,coefficient_variable_name,rate_name):
    ode_term = '('+str(np.sign(coefficient_value))+')*('+rate_name+')*'+coefficient_variable_name+'^('+str(abs(coefficient_value))+')'
    return ode_term

# store rates names
rate_names = coefs.columns[1:]

# lists to store variables
ode_system = []
ode_system_derivatives = []

# generate written equations
for row in range(0,coefs.shape[0]):

    # store variable's coefficients
    var_coefs = coefs.drop('var_name',axis=1).loc[row,:]
    # store variable's name
    var_name = coefs.loc[row,'var_name']
    # list to store each equation formatted row
    ode_list = []

    for coef,rate_name in zip(var_coefs,rate_names):

        if coef < 0:
            # compute term
            ode_term = make_ode_term_str(coef,var_name,rate_name) 
            # save ode_term
            ode_list.append(ode_term)

        if coef == 0: continue

        if coef > 0:
        # store variables with negative coefficients of the same reaction

            # start list   
            tmp_terms = []
            # variable coefficient
            tmp_coefs = coefs.loc[coefs[rate_name] < 0,rate_name]
            # variable name
            tmp_names = coefs.loc[coefs[rate_name] < 0,'var_name']   

            for tmp_c,tmp_n in zip(tmp_coefs,tmp_names):
                ode_term = make_ode_term_str(tmp_c,tmp_n,rate_name)
                tmp_terms.append(ode_term)

            # change signs    
            tmp_terms = '(-1)*('+' + '.join(tmp_terms)+')'       

            # save ode_term
            ode_list.append(tmp_terms)

    # join if there is more than one term
    if len(ode_list) > 1: ode_list = [' + '.join(ode_list)]

    # add left equation side
    ode_list = 'd' + var_name + ' = ' + ode_list[0]  

    # store
    ode_system.append(ode_list)
    ode_system_derivatives.append('d' + var_name)

# make start and end of the function
start_line = 'ode_system <- function(t,state,parameters){with(as.list(c(state,parameters)),{'
end_line = 'list(c('+','.join(ode_system_derivatives)+')) })}'

# write lines
with open(ode_function_file,'w') as ode_file: ode_file.writelines(start_line+'\n'+'\n'.join(ode_system)+'\n'+end_line)