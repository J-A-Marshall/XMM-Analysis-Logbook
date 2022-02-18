#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import Image


# # **Revolution 303**

# ## PN Data

# The odf for rotation 303 was downloaded as before using the `odfid`. The same data processing techniques were copied to produce spectra for the PN and MOS cameras. The spectra for the 2 MOS cameras were merged. 

# ### Creating the Lightcurve
# 

# The lightcurve for this revolution differs from the 1st, but still has the same flaring event. It was filtered using a different method than before as using gtibuild didn't seem to work.

# In[2]:


Image(filename="303_figs/pn_lc.png")


# #### Pileup

# In[16]:


Image(filename="303_figs/pn_pileup.png")


# #### Spectrum

# In[15]:


Image(filename="303_figs/pn_laor2.png")


# ## MOS Data

# ### Lightcurves

# In[8]:


Image(filename="303_figs/mos1_lc.png")


# ##### filtering for mos2

# In[9]:


Image(filename="303_figs/mos2_lc.png")


# ### Pile up

# The same regions for the source and background regions were used from revolution 301 and the source and background spectra were extracted to produce the pileup

# In[12]:


Image(filename="303_figs/mos1_pileup.png")


# In[14]:


Image(filename="303_figs/mos2_pileup.png")


# The data for both mos cameras was merged as before.

# 
