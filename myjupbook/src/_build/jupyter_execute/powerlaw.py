#!/usr/bin/env python
# coding: utf-8

# # **Plotting a Broken Powerlaw Emissivity Profile** 

# In[1]:


import numpy as np 
import matplotlib.pyplot as plt
from IPython.display import Image


# In[2]:


plt.rc('font', family='serif')
plt.rc('xtick', labelsize='x-small')
plt.rc('ytick', labelsize='x-small')


# Using the equations from: https://heasarc.gsfc.nasa.gov/xanadu/xspec/manual/node141.html

# In[3]:


def broken_powerlaw(k,x,q1,q2,r_br):
    returnArray=[]
    for i in x:
        if i<= r_br:
            returnArray.append(k * i**(-q1))
        if i >= r_br:
            returnArray.append(k* (r_br**(q2-q1)) * i**(-q2))            
    return returnArray


# In[4]:


r_out = 400 # Outer accretion edge 
k = 1 # Normalisation Constant
q1 = 6 # Inner emissivity index
q2 = 3 # Outer emissivity index
r_br = 6 # Break radii 

x = np.linspace(1,r_out,r_out+1)
y_dat = broken_powerlaw(k,x,q1,q2,r_br)


# In[5]:


# Log - log plot
fig, ax = plt.subplots()
ax.plot(x,y_dat,linewidth='1.5',color='k')
ax.set_yscale('log')
ax.set_xscale('log')
ax.grid(True,which='both',axis='both',ls='--')
ax.set_xlabel("Disk radius $(r_g)$")
ax.set_ylabel(r"$\epsilon$ (arbitrary units)")
plt.title("Emissivity profile of MCG-6-30-15")
plt.savefig('emissivity_curve_log.png', dpi = 300)
plt.show()

# log-linear plot
fig, ax = plt.subplots()
ax.plot(x,y_dat,linewidth='1.5',color='k')
ax.set_yscale('log')
ax.grid(True,which='both',axis='both',ls='--')
ax.set_xlabel("Disk radius $(r_g)$")
ax.set_ylabel(r"$\epsilon$ (arbitrary units)")
plt.title("Emissivity profile of MCG-6-30-15")
plt.savefig('emissivity_curve_linear.png', dpi = 300)
plt.show()


# In[6]:


Image('emissivity_curve_linear.png')


# In[7]:


Image('emissivity_curve_log.png')


# ## Plotting emissivity profile for varying break radii

# In[8]:


# A list of break radii to plot
r_set=[2,4,6,8,10,12]
y_dat_list=[]
for i in r_set:
    y_dat = broken_powerlaw(k,x,q1,q2,i) 
    plt.plot(x,y_dat,label='$r_b$ = {:}'.format(i),ls='--')
plt.plot(x,y_dat[0:],label='$r_b$ = {:}'.format(i),ls='-',color='k')
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel("Disk radius $(r_g)$")
plt.ylabel(r"$\epsilon$ (arbitrary units)")
plt.grid(True,which='both',ls='--')
plt.title(r"Emissivity profile at varying $r_{br}$")
plt.savefig('emissivity_curve_varied_log.png', dpi = 300)
plt.show()    

Image('emissivity_curve_varied_log.png')


# In[9]:


for i in r_set:
    y_dat = broken_powerlaw(k,x,q1,q2,i) 
    plt.plot(x,y_dat,label='$r_b$ = {:}'.format(i),ls='--')
plt.plot(x,y_dat[0:],label='$r_b$ = {:}'.format(i),ls='-',color='k')
plt.legend()
plt.yscale('log')
plt.xlabel("Disk radius $(r_g)$")
plt.ylabel(r"$\epsilon$ (arbitrary units)")
plt.grid(True,which='both',ls='--')
plt.title(r"Emissivity profile at varying $r_{br}$")
plt.savefig('emissivity_curve_varied_linear.png', dpi = 300)
plt.show()    

Image('emissivity_curve_varied_linear.png')
    


# ## Plotting emissivity profile for varying inner index

# In[20]:


# A list of q1 to plot
q_set=[3,3.5,4,4.5,5,5.5,6]
y_dat_list=[]
for i in q_set:
    y_dat = broken_powerlaw(k,x,i,q2,r_br) 
    plt.plot(x,y_dat,label='q1 = {:.1f}'.format(i),ls='--')
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel("Disk radius $(r_g)$")
plt.ylabel(r"$\epsilon$ (arbitrary units)")
plt.grid(True,which='both',ls='--')
plt.title(r"Emissivity profile at varying inner index")
plt.savefig('emissivity_curve_index_log.png', dpi = 300)
plt.show()    

Image('emissivity_curve_index_log.png')


# In[ ]:




