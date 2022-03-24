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

# In[3]:


Image(filename="303_figs/pn_lc.png")


# #### Corrected Lightcurve

# In[2]:


Image(filename="303_figs/pn_corrected_lc.png")


# #### Pileup

# Following https://heasarc.gsfc.nasa.gov/docs/xmm/abc/node8.html#SECTION00880000000000000000

# Extracting source and background regions and spectra

# In[ ]:


evselect table=pn_clean.fits energycolumn=PI withfilteredset=yes filteredset=pn_source_region.fits keepfilteroutput=yes filtertype=expression expression='((FLAG==0) && (PATTERN <= 4) && ((X,Y) IN circle(26273,27909,641.7))' withspectrumset=yes spectrumset=pn_source_spectrum.fits spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=20479


# In[ ]:


evselect table=pn_clean.fits energycolumn=PI withfilteredset=yes filteredset=pn_bkg_region.fits keepfilteroutput=yes filtertype=expression expression='((FLAG==0) && (PATTERN <= 4) && ((X,Y) IN circle(29257,25919,1124)' withspectrumset=yes spectrumset=pn_bkg_spectrum.fits spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=20479


# In[ ]:


epatplot set=pn_source_region.fits plotfile=pn_pileup.ps useplotfile=yes withbackgroundset=yes backgroundset=pn_bkg_region.fits


# In[3]:


Image(filename="303_figs/pn_pileup.png")


# #### Spectrum

# In[3]:


Image(filename="303_figs/pn_laor2.png")


# ## MOS Data

# ### Lightcurves

# In[8]:


Image(filename="303_figs/mos1_lc.png")


# In[4]:


Image(filename="303_figs/mos1_corrected_lc.png")


# ##### Mos2

# In[9]:


Image(filename="303_figs/mos2_lc.png")


# In[5]:


Image(filename="303_figs/mos2_corrected_lc.png")


# ### Pile up

# The same regions for the source and background regions were used from revolution 301 and the source and background spectra were extracted to produce the pileup

# In[12]:


Image(filename="303_figs/mos1_pileup.png")


# In[14]:


Image(filename="303_figs/mos2_pileup.png")


# The data for both mos cameras was merged as before.

# 
