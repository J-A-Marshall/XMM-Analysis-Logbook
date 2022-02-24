#!/usr/bin/env python
# coding: utf-8

# # Giorgio Combined Spectra

# In[3]:


from IPython.display import Image


# #### Combining the Files

# In[ ]:


epicspeccombine pha="2407_pn_source_spectrum.ds 2408_pn_source_spectrum.ds 2409_pn_source_spectrum.ds" bkg="2407_pn_bkg_spectrum.ds 2408_pn_bkg_spectrum.ds 2409_pn_bkg_spectrum.ds" rmf="2407_pn_response.rmf 2408_pn_response.rmf 2409_pn_response.rmf" arf="2407_pn_arf.arf 2408_pn_arf.arf 2409_pn_arf.arf" filepha="giorgio_pn_source_all_revs.ds" filebkg="giorgio_pn_bkg_all_revs.ds" filersp="giorgio_pn_response_all_revs.rmf"


# In[ ]:


epicspeccombine pha="2407_mos1_source_spectrum.ds 2408_mos2_source_spectrum.ds 2409_mos1_source_spectrum.ds 2407_mos2_source_spectrum.ds 2408_mos1_source_spectrum.ds 2409_mos2_source_spectrum.ds" bkg="2407_mos1_bkg_spectrum.ds 2408_mos1_bkg_spectrum.ds 2409_mos1_bkg_spectrum.ds 2407_mos2_bkg_spectrum.ds 2408_mos2_bkg_spectrum.ds 2409_mos2_bkg_spectrum.ds" rmf="2407_mos1_response.rmf 2407_mos2_response.rmf 2408_mos1_response.rmf 2408_mos2_response.rmf 2409_mos1_response.rmf 2409_mos2_response.rmf" arf="2407_mos1_arf.arf 2407_mos2_arf.arf 2408_mos1_arf.arf 2408_mos2_arf.arf 2409_mos1_arf.arf 2409_mos2_arf.arf" filepha="giorgio_mos_source_all_revs.ds" filebkg="giorgio_mos_bkg_all_revs.ds" filersp="giorgio_mos_response_all_revs.rmf"


# #### PN Spectra

# In[4]:


Image(filename="giorgio_figs/pn_eeufs.png")


# In[5]:


Image(filename="giorgio_figs/pn_ratio.png")


# #### MOS Data

# In[6]:


Image(filename="giorgio_figs/mos_eeufs.png")


# In[7]:


Image(filename="giorgio_figs/pn_ratio.png")


# ##### Simultaneous fits

# In[8]:


Image(filename="giorgio_figs/simultaneous.png")


# In[9]:


Image(filename="giorgio_figs/sim_fit_binned.png")


# 
