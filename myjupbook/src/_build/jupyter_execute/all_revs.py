#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import Image


# # Combining Giorgio and Fabian Data
# 

# ## Plotting the MOS data sets

# The combined revolutions for the MOS cameras from the Fabian and Giorgio data was plotted to see how close the data was and whether combining the data would be possible.

# In[3]:


Image(filename="all_revs_figs/mos_data_both_epochs.png")


# The MOS data seems to have very good agreement between the two epochs. A way to statistically show this would be good - have not achieved this yet.

# ## Merging the MOS data

# As the data matched very well, all the MOS data for each revolution from both epochs was merged together.

# In[ ]:


epicspeccombine pha="301_mos1_source_spectrum.ds 301_mos2_source_spectrum.ds 302_mos1_source_spectrum.ds 302_mos2_source_spectrum.ds 303_mos1_source_spectrum.ds 303_mos2_source_spectrum.ds 2407_mos1_source_spectrum.ds 2408_mos2_source_spectrum.ds 2409_mos1_source_spectrum.ds 2407_mos2_source_spectrum.ds 2408_mos1_source_spectrum.ds 2409_mos2_source_spectrum.ds" bkg="301_mos1_bkg_spectrum.ds 301_mos2_bkg_spectrum.ds 302_mos1_bkg_spectrum.ds 302_mos2_bkg_spectrum.ds 303_mos1_bkg_spectrum.ds 303_mos2_bkg_spectrum.ds 2407_mos1_bkg_spectrum.ds 2408_mos1_bkg_spectrum.ds 2409_mos1_bkg_spectrum.ds 2407_mos2_bkg_spectrum.ds 2408_mos2_bkg_spectrum.ds 2409_mos2_bkg_spectrum.ds" rmf="301_mos1_response.rmf 301_mos2_response.rmf 302_mos1_response.rmf 302_mos2_response.rmf 303_mos1_response.rmf 303_mos2_response.rmf 2407_mos1_response.rmf 2407_mos2_response.rmf 2408_mos1_response.rmf 2408_mos2_response.rmf 2409_mos1_response.rmf 2409_mos2_response.rmf" arf="301_mos1_arf.arf 301_mos2_arf.arf 302_mos1_arf.arf 302_mos2_arf.arf 303_mos1_arf.arf 303_mos2_arf.arf 2407_mos1_arf.arf 2407_mos2_arf.arf 2408_mos1_arf.arf 2408_mos2_arf.arf 2409_mos1_arf.arf 2409_mos2_arf.arf" filepha="mos_source_fab_and_giorg.ds" filebkg="mos_bkg_fab_and_giorg.ds" filersp="mos_response_fab_and_giorg.rmf"


# Plotting with the `relxill` model:

# In[2]:


Image(filename="all_revs_figs/mos_relxill.png")


# In[5]:


Image(filename="all_revs_figs/mos_relxill_formatted.png")


# ## Merging the PN data

# Looking at the PN data showed similar results to the MOS camera with agreement between the 2 epochs. Again, some way of statistically determining this is needed as it seems like the agreement is not as good as it was for the MOS data from eyeballing it.

# In[8]:


Image(filename="all_revs_figs/pn_both_epochs.png")


# Merging the pn data from all 6 revolutions:

# In[ ]:


epicspeccombine pha="301_pn_source_spectrum.ds 302_pn_source_spectrum.ds 303_pn_source_spectrum.ds 2407_pn_source_spectrum.ds 2408_pn_source_spectrum.ds 2409_pn_source_spectrum.ds" bkg="301_pn_bkg_spectrum.ds 302_pn_bkg_spectrum.ds 303_pn_bkg_spectrum.ds 2407_pn_bkg_spectrum.ds 2408_pn_bkg_spectrum.ds 2409_pn_bkg_spectrum.ds" rmf="301_pn_response.rmf 302_pn_response.rmf 303_pn_response.rmf 2407_pn_response.rmf 2408_pn_response.rmf 2409_pn_response.rmf" arf="301_pn_arf.arf 302_pn_arf.arf 303_pn_arf.arf 2407_pn_arf.arf 2408_pn_arf.arf 2409_pn_arf.arf" filepha="pn_source_fab_and_giorg.ds" filebkg="pn_bkg_fab_and_giorg.ds" filersp="pn_response_fab_and_giorg.rmf"


# Fitting the data with the relxill model:

# In[9]:


Image(filename="all_revs_figs/pn_relxill.png")


# In[10]:


Image(filename="all_revs_figs/pn_relxill_formatted.png")


# ## Merging the MOS and PN data together

# Merging the MOS and PN data together respectively yields good results, if the data allows, merging of the PN data with the MOS data may be possible to increase the signal to noise even more. Intially plotting the data together looks promising:

# In[11]:


Image(filename="all_revs_figs/mos_and_pn_both_epochs.png")


# Attempting to merge the files using `eppicspeccombine` fails mdue to a <span style="color:red">"Different PI channel interval"</span>. The command is included here in case it can be used later as it was rather tedious to write out:

# In[ ]:


epicspeccombine pha="301_mos1_source_spectrum.ds 301_mos2_source_spectrum.ds 302_mos1_source_spectrum.ds 302_mos2_source_spectrum.ds 303_mos1_source_spectrum.ds 303_mos2_source_spectrum.ds 2407_mos1_source_spectrum.ds 2408_mos2_source_spectrum.ds 2409_mos1_source_spectrum.ds 2407_mos2_source_spectrum.ds 2408_mos1_source_spectrum.ds 2409_mos2_source_spectrum.ds 301_pn_source_spectrum.ds 302_pn_source_spectrum.ds 303_pn_source_spectrum.ds 2407_pn_source_spectrum.ds 2408_pn_source_spectrum.ds 2409_pn_source_spectrum.ds" bkg="301_mos1_bkg_spectrum.ds 301_mos2_bkg_spectrum.ds 302_mos1_bkg_spectrum.ds 302_mos2_bkg_spectrum.ds 303_mos1_bkg_spectrum.ds 303_mos2_bkg_spectrum.ds 2407_mos1_bkg_spectrum.ds 2408_mos1_bkg_spectrum.ds 2409_mos1_bkg_spectrum.ds 2407_mos2_bkg_spectrum.ds 2408_mos2_bkg_spectrum.ds 2409_mos2_bkg_spectrum.ds 301_pn_bkg_spectrum.ds 302_pn_bkg_spectrum.ds 303_pn_bkg_spectrum.ds 2407_pn_bkg_spectrum.ds 2408_pn_bkg_spectrum.ds 2409_pn_bkg_spectrum.ds" rmf="301_mos1_response.rmf 301_mos2_response.rmf 302_mos1_response.rmf 302_mos2_response.rmf 303_mos1_response.rmf 303_mos2_response.rmf 2407_mos1_response.rmf 2407_mos2_response.rmf 2408_mos1_response.rmf 2408_mos2_response.rmf 2409_mos1_response.rmf 2409_mos2_response.rmf 301_pn_response.rmf 302_pn_response.rmf 303_pn_response.rmf 2407_pn_response.rmf 2408_pn_response.rmf 2409_pn_response.rmf" arf="301_mos1_arf.arf 301_mos2_arf.arf 302_mos1_arf.arf 302_mos2_arf.arf 303_mos1_arf.arf 303_mos2_arf.arf 2407_mos1_arf.arf 2407_mos2_arf.arf 2408_mos1_arf.arf 2408_mos2_arf.arf 2409_mos1_arf.arf 2409_mos2_arf.arf 301_pn_arf.arf 302_pn_arf.arf 303_pn_arf.arf 2407_pn_arf.arf 2408_pn_arf.arf 2409_pn_arf.arf" filepha="mos_and_pn_source_fab_and_giorg.ds" filebkg="mos_and_pn_bkg_fab_and_giorg.ds" filersp="mos_and_pn_response_fab_and_giorg.rmf"


# 
