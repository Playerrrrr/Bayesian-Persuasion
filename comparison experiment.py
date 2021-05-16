#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 15 10:46:44 2021

@author: lijiahao
"""

#!/usr/bin/env python
# coding: utf-8

# In[34]:


from scipy.optimize import minimize
import numpy as np
import pandas as pd


# In[35]:


# First we define the utility of the player in the stage game


# In[36]:


ug0 = 1
ug1 = 2
ub0 = -1
ub1 = -2


# In[37]:


# Then we set the probability of states
# The variables with short names are for the first stage while variables with logn names are for the second stage


# In[38]:
a_list=np.linspace(0,1,51)
b_list=np.linspace(0,1,51)
c_list=[0,1]

list_a = []
list_b = []
list_c = []
list_v_com = []
list_v_noncom = []
list_1p0_com = []
list_1p0_noncom = []

for a in a_list:
    for b in b_list:
        for c in c_list:
            pg = b
            pb = 1-b
            
            g00pg = a
            g00pb = 1-a
            g10pg = a
            g10pb = 1-a
            b00pg = a
            b00pb = 1-a
            b10pg = a
            b10pb = 1-a
            
            g01pg = 1-a
            g01pb = a
            g11pg = 1-a
            g11pb = a
            b01pg = 1-a
            b01pb = a
            b11pg = 1-a
            b11pb = a
            
            
            # In[39]:
            
            
            # We need to solve the information design problem in the second stage after all possible histories
            
            
            # In[40]:
            
            
            # Here is the information design problem after history g00
            
            
            # In[41]:
            
            
            # We will need to determine g00pg0 g00pg1 g00pb0 and g00pb1
            # We denote them as x[0], x[1], x[2] and x[3] respectively
            
            
            # In[42]:
            
            
            fun = lambda x : - x[0] - x[2]
            cons = ({'type': 'eq', 'fun': lambda x: x[0] + x[1] - g00pg},
                    {'type': 'eq', 'fun': lambda x: x[2] + x[3] - g00pb},
                    {'type': 'ineq', 'fun': lambda x: x[0] * ug0 + x[2] * ub0 - x[0] * ug1 - x[2] * ub1},
                    {'type': 'ineq', 'fun': lambda x: x[1] * ug1 + x[3] * ub1 - x[1] * ug0 - x[3] * ub0},
                    {'type': 'ineq', 'fun': lambda x: x[0]},
                    {'type': 'ineq', 'fun': lambda x: x[1]},
                    {'type': 'ineq', 'fun': lambda x: x[2]},
                    {'type': 'ineq', 'fun': lambda x: x[3]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[0]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[1]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[2]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[3]}
                   )
            x0 = np.array((c,c,c,c))
            g00res = minimize(fun, x0, method='SLSQP', constraints=cons)
            
            ug00 = g00res.x[0] * ug0 + g00res.x[1] * ug1 + g00res.x[2] * ub0 + g00res.x[3] * ub1
            vg00 = g00res.fun
            
            #print("With g00pg0 =",g00res.x[0])
            #print("With g00pg1 =",g00res.x[1])
            #print("With g00pb0 =",g00res.x[2])
            #print("With g00pb1 =",g00res.x[3])
            #print("The expected utility of the player after g00 is", ug00)
            
            
            # In[43]:
            
            
            # Here is the information design problem after history g10
            # We will need to determine g10pg0 g10pg1 g10pb0 and g10pb1
            # We denote them as x[0], x[1], x[2] and x[3] respectively
            
            
            # In[44]:
            
            
            fun = lambda x : - x[0] - x[2]
            cons = ({'type': 'eq', 'fun': lambda x: x[0] + x[1] - g10pg},
                    {'type': 'eq', 'fun': lambda x: x[2] + x[3] - g10pb},
                    {'type': 'ineq', 'fun': lambda x: x[0] * ug0 + x[2] * ub0 - x[0] * ug1 - x[2] * ub1},
                    {'type': 'ineq', 'fun': lambda x: x[1] * ug1 + x[3] * ub1 - x[1] * ug0 - x[3] * ub0},
                    {'type': 'ineq', 'fun': lambda x: x[0]},
                    {'type': 'ineq', 'fun': lambda x: x[1]},
                    {'type': 'ineq', 'fun': lambda x: x[2]},
                    {'type': 'ineq', 'fun': lambda x: x[3]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[0]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[1]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[2]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[3]}
                   )
            x0 = np.array((c,c,c,c))
            g10res = minimize(fun, x0, method='SLSQP', constraints=cons)
            
            ug10 = g10res.x[0] * ug0 + g10res.x[1] * ug1 + g10res.x[2] * ub0 + g10res.x[3] * ub1
            vg10 = g10res.fun
            
            #print("With g10pg0 =",g10res.x[0])
            #print("With g10pg1 =",g10res.x[1])
            #print("With g10pb0 =",g10res.x[2])
            #print("With g10pb1 =",g10res.x[3])
            #print("The expected utility of the player after g10 is", ug10)
            
            
            # In[45]:
            
            
            fun = lambda x : - x[0] - x[2]
            cons = ({'type': 'eq', 'fun': lambda x: x[0] + x[1] - b00pg},
                    {'type': 'eq', 'fun': lambda x: x[2] + x[3] - b00pb},
                    {'type': 'ineq', 'fun': lambda x: x[0] * ug0 + x[2] * ub0 - x[0] * ug1 - x[2] * ub1},
                    {'type': 'ineq', 'fun': lambda x: x[1] * ug1 + x[3] * ub1 - x[1] * ug0 - x[3] * ub0},
                    {'type': 'ineq', 'fun': lambda x: x[0]},
                    {'type': 'ineq', 'fun': lambda x: x[1]},
                    {'type': 'ineq', 'fun': lambda x: x[2]},
                    {'type': 'ineq', 'fun': lambda x: x[3]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[0]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[1]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[2]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[3]}
                   )
            x0 = np.array((c,c,c,c))
            b00res = minimize(fun, x0, method='SLSQP', constraints=cons)
            
            ub00 = b00res.x[0] * ug0 + b00res.x[1] * ug1 + b00res.x[2] * ub0 + b00res.x[3] * ub1
            vb00 = b00res.fun
            
            #print("With b00pg0 =",b00res.x[0])
            #print("With b00pg1 =",b00res.x[1])
            #print("With b00pb0 =",b00res.x[2])
            #print("With b00pb1 =",b00res.x[3])
            #print("The expected utility of the player after b00 is", ub00)
            
            
            # In[46]:
            
            
            fun = lambda x : - x[0] - x[2]
            cons = ({'type': 'eq', 'fun': lambda x: x[0] + x[1] - b10pg},
                    {'type': 'eq', 'fun': lambda x: x[2] + x[3] - b10pb},
                    {'type': 'ineq', 'fun': lambda x: x[0] * ug0 + x[2] * ub0 - x[0] * ug1 - x[2] * ub1},
                    {'type': 'ineq', 'fun': lambda x: x[1] * ug1 + x[3] * ub1 - x[1] * ug0 - x[3] * ub0},
                    {'type': 'ineq', 'fun': lambda x: x[0]},
                    {'type': 'ineq', 'fun': lambda x: x[1]},
                    {'type': 'ineq', 'fun': lambda x: x[2]},
                    {'type': 'ineq', 'fun': lambda x: x[3]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[0]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[1]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[2]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[3]}
                   )
            x0 = np.array((c,c,c,c))
            b10res = minimize(fun, x0, method='SLSQP', constraints=cons)
            
            ub10 = b10res.x[0] * ug0 + b10res.x[1] * ug1 + b10res.x[2] * ub0 + b10res.x[3] * ub1
            vb10 = b10res.fun
            
            #print("With b10pg0 =",b10res.x[0])
            #print("With b10pg1 =",b10res.x[1])
            #print("With b10pb0 =",b10res.x[2])
            #print("With b10pb1 =",b10res.x[3])
            #print("The expected utility of the player after b10 is", ub10)
            
            
            # In[47]:
            
            
            fun = lambda x : - x[0] - x[2]
            cons = ({'type': 'eq', 'fun': lambda x: x[0] + x[1] - g01pg},
                    {'type': 'eq', 'fun': lambda x: x[2] + x[3] - g01pb},
                    {'type': 'ineq', 'fun': lambda x: x[0] * ug0 + x[2] * ub0 - x[0] * ug1 - x[2] * ub1},
                    {'type': 'ineq', 'fun': lambda x: x[1] * ug1 + x[3] * ub1 - x[1] * ug0 - x[3] * ub0},
                    {'type': 'ineq', 'fun': lambda x: x[0]},
                    {'type': 'ineq', 'fun': lambda x: x[1]},
                    {'type': 'ineq', 'fun': lambda x: x[2]},
                    {'type': 'ineq', 'fun': lambda x: x[3]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[0]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[1]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[2]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[3]}
                   )
            x0 = np.array((c,c,c,c))
            g01res = minimize(fun, x0, method='SLSQP', constraints=cons)
            
            ug01 = g01res.x[0] * ug0 + g01res.x[1] * ug1 + g01res.x[2] * ub0 + g01res.x[3] * ub1
            vg01 = g01res.fun
            
            #print("With g01pg0 =",g01res.x[0])
            #print("With g01pg1 =",g01res.x[1])
            #print("With g01pb0 =",g01res.x[2])
            #print("With g01pb1 =",g01res.x[3])
            #print("The expected utility of the player after g01 is", ug01)
            
            
            # In[48]:
            
            
            fun = lambda x : - x[0] - x[2]
            cons = ({'type': 'eq', 'fun': lambda x: x[0] + x[1] - g11pg},
                    {'type': 'eq', 'fun': lambda x: x[2] + x[3] - g11pb},
                    {'type': 'ineq', 'fun': lambda x: x[0] * ug0 + x[2] * ub0 - x[0] * ug1 - x[2] * ub1},
                    {'type': 'ineq', 'fun': lambda x: x[1] * ug1 + x[3] * ub1 - x[1] * ug0 - x[3] * ub0},
                    {'type': 'ineq', 'fun': lambda x: x[0]},
                    {'type': 'ineq', 'fun': lambda x: x[1]},
                    {'type': 'ineq', 'fun': lambda x: x[2]},
                    {'type': 'ineq', 'fun': lambda x: x[3]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[0]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[1]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[2]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[3]}
                   )
            x0 = np.array((c,c,c,c))
            g11res = minimize(fun, x0, method='SLSQP', constraints=cons)
            
            ug11 = g11res.x[0] * ug0 + g11res.x[1] * ug1 + g11res.x[2] * ub0 + g11res.x[3] * ub1
            vg11 = g11res.fun
            
            #print("With g11pg0 =",g11res.x[0])
            #print("With g11pg1 =",g11res.x[1])
            #print("With g11pb0 =",g11res.x[2])
            #print("With g11pb1 =",g11res.x[3])
            #print("The expected utility of the player after g11 is", ug11)
            
            
            # In[49]:
            
            
            fun = lambda x : - x[0] - x[2]
            cons = ({'type': 'eq', 'fun': lambda x: x[0] + x[1] - b01pg},
                    {'type': 'eq', 'fun': lambda x: x[2] + x[3] - b01pb},
                    {'type': 'ineq', 'fun': lambda x: x[0] * ug0 + x[2] * ub0 - x[0] * ug1 - x[2] * ub1},
                    {'type': 'ineq', 'fun': lambda x: x[1] * ug1 + x[3] * ub1 - x[1] * ug0 - x[3] * ub0},
                    {'type': 'ineq', 'fun': lambda x: x[0]},
                    {'type': 'ineq', 'fun': lambda x: x[1]},
                    {'type': 'ineq', 'fun': lambda x: x[2]},
                    {'type': 'ineq', 'fun': lambda x: x[3]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[0]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[1]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[2]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[3]}
                   )
            x0 = np.array((c,c,c,c))
            b01res = minimize(fun, x0, method='SLSQP', constraints=cons)
            
            ub01 = b01res.x[0] * ug0 + b01res.x[1] * ug1 + b01res.x[2] * ub0 + b01res.x[3] * ub1
            vb01 = b01res.fun
            
            #print("With b01pg0 =",b01res.x[0])
            #print("With b01pg1 =",b01res.x[1])
            #print("With b01pb0 =",b01res.x[2])
            #print("With b01pb1 =",b01res.x[3])
            #print("The expected utility of the player after b01 is", ub01)
            
            
            # In[50]:
            
            
            fun = lambda x : - x[0] - x[2]
            cons = ({'type': 'eq', 'fun': lambda x: x[0] + x[1] - b11pg},
                    {'type': 'eq', 'fun': lambda x: x[2] + x[3] - b11pb},
                    {'type': 'ineq', 'fun': lambda x: x[0] * ug0 + x[2] * ub0 - x[0] * ug1 - x[2] * ub1},
                    {'type': 'ineq', 'fun': lambda x: x[1] * ug1 + x[3] * ub1 - x[1] * ug0 - x[3] * ub0},
                    {'type': 'ineq', 'fun': lambda x: x[0]},
                    {'type': 'ineq', 'fun': lambda x: x[1]},
                    {'type': 'ineq', 'fun': lambda x: x[2]},
                    {'type': 'ineq', 'fun': lambda x: x[3]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[0]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[1]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[2]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[3]}
                   )
            x0 = np.array((c,c,c,c))
            b11res = minimize(fun, x0, method='SLSQP', constraints=cons)
            
            ub11 = b11res.x[0] * ug0 + b11res.x[1] * ug1 + b11res.x[2] * ub0 + b11res.x[3] * ub1
            vb11 = b11res.fun
            
            #print("With b11pg0 =",b11res.x[0])
            #print("With b11pg1 =",b11res.x[1])
            #print("With b11pb0 =",b11res.x[2])
            #print("With b11pb1 =",b11res.x[3])
            #print("The expected utility of the player after b11 is", ub11)
            
            
            # In[51]:
            
            
            # The above utility after some history can be added to the first stage payoff directly to solve the information design in the first stage
            
            
            # In[52]:
            
            
            fun = lambda x : - x[0] - x[2]
            cons = ({'type': 'eq', 'fun': lambda x: x[0] + x[1] - pg},
                    {'type': 'eq', 'fun': lambda x: x[2] + x[3] - pb},
                    {'type': 'ineq', 'fun': lambda x: x[0] * (ug0 + ug00) + x[2] * (ub0 + ub00) - x[0] * (ug1 + ug01) - x[2] * (ub1 + ub01)},
                    {'type': 'ineq', 'fun': lambda x: x[1] * (ug1 + ug11) + x[3] * (ub1 + ub11) - x[1] * (ug0 + ug10) - x[3] * (ub0 + ub10)},
                    {'type': 'ineq', 'fun': lambda x: x[0]},
                    {'type': 'ineq', 'fun': lambda x: x[1]},
                    {'type': 'ineq', 'fun': lambda x: x[2]},
                    {'type': 'ineq', 'fun': lambda x: x[3]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[0]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[1]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[2]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[3]}
                   )
            x0 = np.array((c,c,c,c))
            res = minimize(fun, x0, method='SLSQP', constraints=cons)
            #print("The maximum utility of the information designer in the first stage is",res.fun)
            #print("With pg0 =",res.x[0])
            #print("With pg1 =",res.x[1])
            #print("With pb0 =",res.x[2])
            #print("With pb1 =",res.x[3])
            pg0 = res.x[0]
            pg1 = res.x[1]
            pb0 = res.x[2]
            pb1 = res.x[3]
            
            
            # In[53]:
            
            
            #print("The utility of the information designer is", res.fun + pg0 *  vg00 + pb0 *  vb00 + pg1 * vg11 + pb1 * vb11)
            
            
            # In[54]:
            
            
            res.x[0] + res.x[2]
            
            
            # In[55]:
            
            
            # We record two things: the utility of the information designer and the probability assigned to action 0 in the first stage
            
            
            # In[56]:
            
            
            v_noncommitment = res.fun + pg0 *  vg00 + pb0 *  vb00 + pg1 * vg11 + pb1 * vb11
            p0_stage1_noncommitment = res.x[0] + res.x[2]
            
            
            # In[57]:
            
            
            # Then we compute this problem in the commitment case
            
            
            # In[58]:
            
            
            # We will need to determine 36 variables
            # pg0 pg1 pb0 pb1: x[0] x[1] x[2] x[3]
            
            # g00pg0 g00pg1 g00pb0 g00pb1 x[4] x[5] x[6] x[7]
            # g01pg0 g01pg1 g01pb0 g01pb1 x[8] x[9] x[10] x[11]
            # g10pg0 g10pg1 g10pb0 g10pb1 x[12] x[13] x[14] x[15]
            # g11pg0 g11pg1 g11pb0 g11pb1 x[16] x[17] x[18] x[19]
            
            # b00pg0 b00pg1 b00pb0 b00pb1 x[20] x[21] x[22] x[23]
            # b01pg0 b01pg1 b01pb0 b01pb1 x[24] x[25] x[26] x[27]
            # b10pg0 b10pg1 b10pb0 b10pb1 x[28] x[29] x[30] x[31]
            # b11pg0 b11pg1 b11pb0 b11pb1 x[32] x[33] x[34] x[35]
            
            
            # In[59]:
            
            
            fun = lambda x : -(x[0]*(1+x[4]+x[6])+x[1]*(x[16]+x[18])+x[2]*(1+x[20]+x[22])+x[3]*(x[32]+x[34]))
            cons = ({'type': 'eq', 'fun': lambda x: x[0] + x[1] - pg},
                    {'type': 'eq', 'fun': lambda x: x[2] + x[3] - pb},
                    {'type': 'eq', 'fun': lambda x: x[4] + x[5] - g00pg},
                    {'type': 'eq', 'fun': lambda x: x[6] + x[7] - g00pb},
                    {'type': 'eq', 'fun': lambda x: x[8] + x[9] - g01pg},
                    {'type': 'eq', 'fun': lambda x: x[10] + x[11] - g01pb},
                    {'type': 'eq', 'fun': lambda x: x[12] + x[13] - g10pg},
                    {'type': 'eq', 'fun': lambda x: x[14] + x[15] - g10pb},
                    {'type': 'eq', 'fun': lambda x: x[16] + x[17] - g11pg},
                    {'type': 'eq', 'fun': lambda x: x[18] + x[19] - g11pb},
                    {'type': 'eq', 'fun': lambda x: x[20] + x[21] - b00pg},
                    {'type': 'eq', 'fun': lambda x: x[22] + x[23] - b00pb},
                    {'type': 'eq', 'fun': lambda x: x[24] + x[25] - b01pg},
                    {'type': 'eq', 'fun': lambda x: x[26] + x[27] - b01pb},
                    {'type': 'eq', 'fun': lambda x: x[28] + x[29] - b10pg},
                    {'type': 'eq', 'fun': lambda x: x[30] + x[31] - b10pb},
                    {'type': 'eq', 'fun': lambda x: x[32] + x[33] - b11pg},
                    {'type': 'eq', 'fun': lambda x: x[34] + x[35] - b11pb},
                    {'type': 'ineq', 'fun': lambda x: x[4] * ug0 + x[6] * ub0 - x[4] * ug1 - x[6] * ub1},
                    {'type': 'ineq', 'fun': lambda x: x[5] * ug1 + x[7] * ub1 - x[5] * ug0 - x[7] * ub0},
                    {'type': 'ineq', 'fun': lambda x: x[8] * ug0 + x[10] * ub0 - x[8] * ug1 - x[10] * ub1},
                    {'type': 'ineq', 'fun': lambda x: x[9] * ug1 + x[11] * ub1 - x[9] * ug0 - x[11] * ub0},
                    {'type': 'ineq', 'fun': lambda x: x[12] * ug0 + x[14] * ub0 - x[12] * ug1 - x[14] * ub1},
                    {'type': 'ineq', 'fun': lambda x: x[13] * ug1 + x[15] * ub1 - x[13] * ug0 - x[15] * ub0},
                    {'type': 'ineq', 'fun': lambda x: x[16] * ug0 + x[18] * ub0 - x[16] * ug1 - x[18] * ub1},
                    {'type': 'ineq', 'fun': lambda x: x[17] * ug1 + x[19] * ub1 - x[17] * ug0 - x[19] * ub0},
                    {'type': 'ineq', 'fun': lambda x: x[20] * ug0 + x[22] * ub0 - x[20] * ug1 - x[22] * ub1},
                    {'type': 'ineq', 'fun': lambda x: x[21] * ug1 + x[23] * ub1 - x[21] * ug0 - x[23] * ub0},
                    {'type': 'ineq', 'fun': lambda x: x[24] * ug0 + x[26] * ub0 - x[24] * ug1 - x[26] * ub1},
                    {'type': 'ineq', 'fun': lambda x: x[25] * ug1 + x[27] * ub1 - x[25] * ug0 - x[27] * ub0},
                    {'type': 'ineq', 'fun': lambda x: x[28] * ug0 + x[30] * ub0 - x[28] * ug1 - x[30] * ub1},
                    {'type': 'ineq', 'fun': lambda x: x[29] * ug1 + x[31] * ub1 - x[29] * ug0 - x[31] * ub0},
                    {'type': 'ineq', 'fun': lambda x: x[32] * ug0 + x[34] * ub0 - x[32] * ug1 - x[34] * ub1},
                    {'type': 'ineq', 'fun': lambda x: x[33] * ug1 + x[35] * ub1 - x[33] * ug0 - x[35] * ub0},
                    {'type': 'ineq', 'fun': lambda x: x[0] * (ug0+x[4]*ug0+x[5]*ug1+x[6]*ub0+x[7]*ub1) 
                     + x[2] * (ub0+x[20]*ug0+x[21]*ug1+x[22]*ub0+x[23]*ub1) 
                     - x[0] * (ug1+x[8]*ug0+x[9]*ug1+x[10]*ub0+x[11]*ub1) 
                     - x[2] * (ub1+x[24]*ug0+x[25]*ug1+x[26]*ub0+x[27]*ub1)},
                    {'type': 'ineq', 'fun': lambda x: x[1] * (ug1+x[16]*ug0+x[17]*ug1+x[18]*ub0+x[19]*ub1) 
                     + x[3] * (ub1+x[32]*ug0+x[33]*ug1+x[34]*ub0+x[35]*ub1) 
                     - x[1] * (ug0+x[12]*ug0+x[13]*ug1+x[14]*ub0+x[15]*ub1) 
                     - x[3] * (ub0+x[28]*ug0+x[29]*ug1+x[30]*ub0+x[31]*ub1)},
                    {'type': 'ineq', 'fun': lambda x: x[0]},
                    {'type': 'ineq', 'fun': lambda x: x[1]},
                    {'type': 'ineq', 'fun': lambda x: x[2]},
                    {'type': 'ineq', 'fun': lambda x: x[3]},
                    {'type': 'ineq', 'fun': lambda x: x[4]},
                    {'type': 'ineq', 'fun': lambda x: x[5]},
                    {'type': 'ineq', 'fun': lambda x: x[6]},
                    {'type': 'ineq', 'fun': lambda x: x[7]},
                    {'type': 'ineq', 'fun': lambda x: x[8]},
                    {'type': 'ineq', 'fun': lambda x: x[9]},
                    {'type': 'ineq', 'fun': lambda x: x[10]},
                    {'type': 'ineq', 'fun': lambda x: x[11]},
                    {'type': 'ineq', 'fun': lambda x: x[12]},
                    {'type': 'ineq', 'fun': lambda x: x[13]},
                    {'type': 'ineq', 'fun': lambda x: x[14]},
                    {'type': 'ineq', 'fun': lambda x: x[15]},
                    {'type': 'ineq', 'fun': lambda x: x[16]},
                    {'type': 'ineq', 'fun': lambda x: x[17]},
                    {'type': 'ineq', 'fun': lambda x: x[18]},
                    {'type': 'ineq', 'fun': lambda x: x[19]},
                    {'type': 'ineq', 'fun': lambda x: x[20]},
                    {'type': 'ineq', 'fun': lambda x: x[21]},
                    {'type': 'ineq', 'fun': lambda x: x[22]},
                    {'type': 'ineq', 'fun': lambda x: x[23]},
                    {'type': 'ineq', 'fun': lambda x: x[24]},
                    {'type': 'ineq', 'fun': lambda x: x[25]},
                    {'type': 'ineq', 'fun': lambda x: x[26]},
                    {'type': 'ineq', 'fun': lambda x: x[27]},
                    {'type': 'ineq', 'fun': lambda x: x[28]},
                    {'type': 'ineq', 'fun': lambda x: x[29]},
                    {'type': 'ineq', 'fun': lambda x: x[30]},
                    {'type': 'ineq', 'fun': lambda x: x[31]},
                    {'type': 'ineq', 'fun': lambda x: x[32]},
                    {'type': 'ineq', 'fun': lambda x: x[33]},
                    {'type': 'ineq', 'fun': lambda x: x[34]},
                    {'type': 'ineq', 'fun': lambda x: x[35]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[0]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[1]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[2]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[3]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[4]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[5]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[6]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[7]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[8]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[9]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[10]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[11]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[12]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[13]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[14]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[15]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[16]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[17]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[18]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[19]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[20]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[21]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[22]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[23]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[24]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[25]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[26]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[27]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[28]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[29]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[30]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[31]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[32]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[33]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[34]},
                    {'type': 'ineq', 'fun': lambda x: 1 - x[35]},
                   )
            x0 = np.array((c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c))
            res = minimize(fun, x0, method='SLSQP', constraints=cons)
            
            #print("The utility of the information designer is", res.fun)
            
            
            # In[60]:
            
            
            v_commitment = res.fun
            p0_stage1_commitment = res.x[0] + res.x[2]
            
            
            # In[61]:
            
            
            v_commitment
            
            
            # In[72]:
            
        
            
            list_a.append(a)
            list_b.append(b)
            list_c.append(c)
            list_v_com.append(-v_commitment)
            list_v_noncom.append(-v_noncommitment)
            list_1p0_com .append(p0_stage1_commitment)
            list_1p0_noncom.append(p0_stage1_noncommitment)
            
        # In[73]:
        


table = {'a':list_a,
         'b':list_b,
         'c':list_c,
         'utility of commitment':list_v_com,
         'commitment p0 in stage 1':list_1p0_com,
         'utility of noncommitment':list_v_noncom,
         'noncommitment p0 in stage 1':list_1p0_noncom}

df = pd.DataFrame(table)

formater="{0:.02f}".format
# 或者
#format = lambda x:'%.2f' % x
x = df.applymap(formater)

        
        

