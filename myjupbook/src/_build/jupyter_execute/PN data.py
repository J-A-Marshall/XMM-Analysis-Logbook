#!/usr/bin/env python
# coding: utf-8

# # **Initial Analysis of the PN Data**

# - - - -

# ### Table of Contents
# 
# * [1. Initialisation](#initialisation)
#     * [1.1 HEASOFT](#HEASOFT)
#     * [1.2 SAS](#sas)
# * [2. Importing the ODF](#ODF)
#     * [2.1 Python Script](#section_2_1)
#     * [2.2 Defining the path directions](#section_2_2)
# * [3. Creating Image](#image)
# * [4. Filtering the Data](#filter)   
#     * [4.1 Lightcurve](#lightcurve)
# * [5. Source Detection](#source)   
# * [6. Checking for Pileup](#pileup)
# * [7. Preparing the Spectrum](#specprepare)
# * [8. XSPEC](#xspec)
#     * [8.1 Fitting a Model](#model)
#     * [8.2 Creating the Unfolded Spectrum](#unfolded)
# * [9. Background Lightcurve](#bck_light)

# - - - -

# ### 1. Initialisation<a class="anchor" id="initialisation"></a>
# 
# #### 1.1 HEASOFT <a class="anchor" id="HEASOFT"></a>
# To install and initialise HEASOFT, the following was entered into the `.bashrc` file:

# In[ ]:


source scl_source enable devtoolset-7
export HEADAS=/usr/local/heasoft-6.28/x86_64-pc-linux-gnu-libc2.17
alias heainit=". $HEADAS/headas-init.sh"


# This can then be initialised using the alias `heainit` whenever a new session is created

# #### 1.2 SAS<a class="anchor" id="sas"></a>
# To install and initialise SAS, the following was entered into the `.bashrc` file:

# In[ ]:


export SAS_DIR=/usr/local/xmm_sas/xmmsas_20210317_1624
alias sasinit=". $SAS_DIR/sas-setup.sh"
export SAS_CCFPATH=/usr/local/XMM/ccf/
export SAS_CCF=/data/cluster4/jamie_and_jeton/xmm_obs/ccf.cif


# This can then be initialised using the alias `sasinit` whenever a new session is created

# ### 2 Importing the ODF<a class="anchor" id="ODF"></a>
# Initially the ODF was imported into the working directory in the shared file using startsas. Following section **Executing Startsas** at https://www.cosmos.esa.int/web/xmm-newton/sas-thread-startup-in-python
# To do this, a python script was made which uses and *odfid* to import the ODF into a selected destination.

# #### 2.1 Python Script <a class="anchor" id="section_2_1"></a>

# In[ ]:


import os
from pysas.wrapper import Wrapper as w
work_dir = '/data/cluster4/jamie_and_jeton/work_dir/0301_0029740101_data'
inargs = [f'odfid=0029740101',f'workdir={work_dir}']
w('startsas', inargs).run()


# **<span style="color:red">
# For analysis of different ODFs, a different odfid and destination path will need to be defined before startsas is ran otherwise this will overwrite data!</span>**

# #### 2.2 Defining the path directions <a class="anchor" id="section_2_2"></a>

# In[ ]:


export SAS_CCF='/data/cluster4/jamie_and_jeton/work_dir/'


# In[ ]:


odfingest


# In[ ]:


export SAS_ODF='/data/cluster4/jamie_and_jeton/work_dir/0301_0029740101_data/0301_0029740101_SCX00000SUM.SAS'


# ### 3. Creating Image<a class="anchor" id="image"></a>

# To get a sense of what the data we are using looks like and comes from, an image of the source is made. 1st epproc is ran.

# In[ ]:


epproc


# Imaging events file renamed to `EPIC.fits`

# In[ ]:


evselect table=EPIC.fits withimageset=yes imageset=image.fits xcolumn=X ycolumn=Y imagebinning=imageSize ximagesize=600 yimagesize=600


# In[ ]:


ds9 image.fits &


# ![MCG-6-30-15_SOURCE_IMAGE](C:\Users\jamie\OneDrive\Documents\University\Year_4\Research_Project\Jupyter Notebooks\Figures\MCG-6-30-15_SOURCE_IMAGE.png)

# The scale was set to **log** and the colour to **heat**.

# ### 4 Filtering the Data <a class="anchor" id="Filter"></a>
# #### 4.1 Standard filters<a class="anchor" id="std filt"></a>

# In[ ]:


evselect table=EPIC.fits withfilteredset=yes expression='(PATTERN <= 4)&&(PI in [200:15000])' filteredset=EPIC_filtered.fits filtertype=expression keepfilteroutput=yes updateexposure=yes filterexposure=yes


# #### 4.2 Light curve<a class="anchor" id="lightcurve"></a>

# Plotting a lightcurve using the filtered data:

# In[ ]:


evselect table=EPIC_filtered.fits withrateset=yes rateset=lightcurve_filtered.fits maketimecolumn=yes timecolumn=TIME timebinsize=100 makeratecolumn=yes 


# In[ ]:


dsplot table=lightcurve_filtered.fits x=TIME y=RATE   


# ![MCG-6-30-15_filtered_light_curve.png](attachment:MCG-6-30-15_filtered_light_curve.png)

# There is a clear cutoff of data at the right side of the graph indicating that there was a flaring event that was filtered out. For brevity, a lightcurve using the unfiltered data will be created.

# In[ ]:


evselect table=EPIC.fits withrateset=yes rateset=lightcurve_un-filtered.fits maketimecolumn=yes timecolumn=TIME timebinsize=100 makeratecolumn=yes


# In[ ]:


dsplot table=lightcurve_un-filtered.fits.fits x=TIME y=RATE   


# ![MCG-6-30-15_un-filtered_light_curve.png](attachment:MCG-6-30-15_un-filtered_light_curve.png)

# There is clearly a strong flaring event that should be removed. The standard filtering also removed various other counts from the un-filtered data that can be seen by comparing the two graphs. It is clear that the filtered data set should be used from here on.

# #### 4.3 Deep Minimum Lightcurve <a class="anchor" id="source"></a>
# To see how the data varies when the object is in a state of low flux, the data is restricted so that only counts taken between 1.13008x10$^{8}$ and 1.13015x10$^{8}$ are used.

# In[ ]:


evselect table=EPIC_filtered.fits withfilteredset=yes filteredset=deepmin.fits filtertype=expression expression='(TIME < 1.13015e8)&&(TIME > 1.13008e8)' keepfilteroutput=yes updateexposure=yes


# In[ ]:


evselect table=deepmin.fits withrateset=yes rateset=deepmin_lightcurve.fits maketimecolumn=yes timecolumn=TIME timebinsize=100 makeratecolumn=yes


# In[ ]:


dsplot table=deepmin_lightcurve.fits x=TIME y=RATE


# ![MCG-6-30-15_deepmin_light_curve.png](attachment:MCG-6-30-15_deepmin_light_curve.png)

# ### 5. Source Detection <a class="anchor" id="source"></a>

# The image of the source was viewed again to determine where the source and background regions are. To do this it was viewed with ds9 and circles under the region tab were added to the image and altered in size until they matched these regions. The properties such as position and radius of these circles were set to physical units and recorded.

# ![MCG-6-30-15_image_with_regions.png](attachment:MCG-6-30-15_image_with_regions.png)

# ![Background%20circle.png](attachment:Background%20circle.png)![Source%20circle.png](attachment:Source%20circle.png)

# The spectrum of the source and background regions was then determined using `spectrumset`

# In[ ]:


evselect table=EPIC_filt_time.fits withspectrumset=yes spectrumset=PNsource_spec.fits energycolumn=PI spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=20479 expression='(FLAG==0) && (PATTERN<=4) && ((X,Y) IN circle(26229.662,27962.992,565.3))'


# In[ ]:


evselect table=EPIC_filt_time.fits withspectrumset=yes spectrumset=PNbackg_spec.fits energycolumn=PI spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=20479 expression='(FLAG==0) && (PATTERN<=4) && ((X,Y) IN circle(29365.842,25855.344,712.9))'


# In[ ]:


backscale spectrumset=PNbackg_spec.fits badpixlocation=EPIC_filt_time.fits


# ### 6. Checking for Pileup<a class="anchor" id="pileup"></a>

# In[ ]:


epatplot set=EPIC_filtered.fits plotfile=EPIC_epat.ps useplotfile=yes withbackgroundset=yes backgroundset=bkg_filtered.fits


# The output of this is plotted with `gv`. There is an error raised stating<span style="color:red">Warning: Missing charsets in String to FontSet conversion</span>
# This can be solved by issuing the command `export LC_CTYPE=C`. This is not a permanent solution as it resets so there may be something missing in solva.

# In[ ]:


gv EPIC_epat.ps


# ![MCG-6-30-15_Pileup.png](attachment:MCG-6-30-15_Pileup.png)

# ### 7. Preparing the Spectrum <a class="anchor" id="specprepare"></a>
# The calibration files, arf and rmf were created and grouped together to make using xspec easier

# In[ ]:


rmfgen spectrumset=PNsource_spec.fits rmfset=PN.rmf


# In[ ]:


arfgen spectrumset=PNsource_spec.fits arfset=PN.arf withrmfset=yes rmfset=PN.rmf badpixlocation=EPIC_filt_time.fits detmaptype=psf


# In[ ]:


specgroup spectrumset=PNsource_spec.fits mincounts=25 oversample=3 rmfset=PN.rmf arfset=PN.arf backgndset=PNbackg_spec.fits groupedset=PN_spectrum_grp.fits


# ### 8. XSPEC <a class="anchor" id="xspec"></a>

# In[ ]:


xspec


# In[ ]:


XSPEC12> data PN_spectrum.fits


# This .fits file contains the arf,rmf,source & background files for convenience 

# In[ ]:


XSPEC12> cpd /xs


# In[ ]:


XSPEC12> setplot energy


# The effective area of the telescope is zero below ~0.2keV and above 10keV, so this energy range will be ignored

# In[ ]:


XSPEC12> ignore 0.0-0.2 , 10.0-**


# ![MCG-60-30-15_RAW_DATA.png](attachment:MCG-60-30-15_RAW_DATA.png)

# This is the filtered data from MCG-60-30-15. There seems to be a break in the data at around 2.2keV which is due to the gold coating on the mirrors creating an absorption edge. The arf and rmf should take this into account when fitting models to this data, however, the data below this will be ignored as it is not important to what we want to observe.

# In[ ]:


XSPEC12> ignore 0.0-2.5


# In[ ]:


XSPEC12> plot ldata


# ![MCG-60-30-15_Restricted_data.png](attachment:MCG-60-30-15_Restricted_data.png)

# This presents a much clearer view of the data and a slight hump at ~6keV can be seen. A simple power law model can now be fitted to the data to try and extract some information about the small hump.

# #### Fitting a model <a class="anchor" id="model"></a>

# In[ ]:


XSPEC12> model powerlaw


# In[ ]:


1:powerlaw:PhoIndex>-3


# In[ ]:


2:powerlaw:norm>1


# In[ ]:


XSPEC12> fit


# In[ ]:


XSPEC12>plot ldata delchi


# ![MCG-60-30-15_q=3_Powerlaw.png](attachment:MCG-60-30-15_q=3_Powerlaw.png)

# Here the iron emission line at 6.4keV can clearly be seen and is very strongly broadened to energies around ~5keV.

# #### Creating the Unfolded Spectrum<a class="anchor" id="unfolded"></a>

# Instructions given for how to produce a figure of the iron line:
# 
# "To make a plot of the line flux you can create an "unfolded spectrum" see XSPEC plot ufs (or eeufs). You can either 1) ignore some energy range such as 3-8 keV, fit continuum, then notice 3-8 keV again for plotting purposes, or 2) fit a powerlaw plus Laor model (for now) and once you have a good fit set the Laor normalisation to zero for plotting purposes. That should give you a nice iron line plot to work with!"

# In[ ]:


XSPEC12> data PN_spectrum_grp.fits 


# In[ ]:


XSPEC12> setplot energy


# In[ ]:


XSPEC12> cpd /xs


# In[ ]:


XSPEC12> ignore 0.0-2.5 , 3.0-8.0 , 10.0-**


# In[ ]:


XSPEC12> plot ldata


# ![MCG-6-30-15_iron-line-removed.png](attachment:MCG-6-30-15_iron-line-removed.png)

# In[ ]:


XSPEC12> model powerlaw


# In[ ]:


1:powerlaw:PhoIndex>-3


# In[ ]:


2:powerlaw:norm>1


# In[ ]:


XSPEC12> fit


# In[ ]:


XSPEC12> notice 3.0-8.0


# In[ ]:


XSPEC12> plot ldata delchi


# ![MCG-6-30-15_fitted_model_iron_removed.png](attachment:MCG-6-30-15_fitted_model_iron_removed.png)

# In[ ]:


XSPEC12> plot eeufs


# ![MCG-6-30-15_unfolded_spec_v1.png](attachment:MCG-6-30-15_unfolded_spec_v1.png)

# The iron line can clearly be seen, however removing the continuum fit and rescaling the y axis needs to be done
# 

# In[ ]:


XSPEC12> iplot


# In[ ]:


PLT> Rescale Y 0.014 0.025


# In[ ]:


PLT> Hardcopy /PS


# ![MCG-6-30-15_unfolded_spec_v2.png](attachment:MCG-6-30-15_unfolded_spec_v2.png)

# In[ ]:


PLT>


# In[ ]:


XSPEC12>


# # 9. Background lightcurve <a class="anchor" id="bck_light"></a>

# A lightcurve is made to determine the prescence of any flaring events. A background region needs to be selected and a lightcurve plotted

# The image file was brought up with ds9 and a background region selected

# ![background%20circle%20lightcurve.png](attachment:background%20circle%20lightcurve.png)

# ![background%20circle%20detail.png](attachment:background%20circle%20detail.png)
# 

# In[ ]:


evselect table=EPIC_filt_time.fits withspectrumset=yes spectrumset=background_spectrum.fits energycolumn=PI spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=20479 expression='(FLAG==0) && (PATTERN<=4) && ((X,Y) IN circle(28681.84,26026.204,1542.3115))'


# In[ ]:


dsplot table=background_spectrum.fits


# ![background%20graph.png](attachment:background%20graph.png)

# The background area was selected from the EPIC.fits file

# In[2]:


evselect table=EPIC.fits withfilteredset=yes expression='((X,Y) IN circle(28681.84,26026.204,1542.3115))' filteredset=background_spec.fits filtertype=expression keepfilteroutput=yes


# The lightcurve of the backgroud area was created and plotted

# In[ ]:


evselect table=background_spec.fits withrateset=yes rateset=background_lightcurve.fits maketimecolumn=yes timecolumn=TIME timebinsize=100 makeratecolumn=yes


# In[ ]:


dsplot table=background_lightcurve.fits x=TIME y=RATE &


# ![background%20lightcurve.png](attachment:background%20lightcurve.png)
