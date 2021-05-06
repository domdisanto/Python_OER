# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 08:01:14 2021
Most recently updated: 4.21.2021 
@author: Dominic DiSanto
"""

'''
# Using generic "units" for each medication (less realistic but significantly less cumbersome to data sim)
'''

# Modules

import pandas as pd 
import numpy as np 
import random, string 
import datetime

np.random.seed(8114)


# Creating three ADS machines and their assignment to different "wings"

machines = {
    1:['ED'],
    2:['Surgery', 'Neurology'],
    3:['Dermatology', 'Oncology']
    }

pd.DataFrame(data = [[1, 'Emergency Department'],
                     [2, 'Surgery'],
                     [2, 'Neurology'],
                     [3, 'Dermatology'],
                     [3, 'Oncology']
                     ], columns=['Machine ID', 'Department/Location']).to_csv("Machines.csv", index=False)


meds = pd.read_excel('Sample_Med_Names.xlsx').iloc[:, 0:10].sort_values('Med_Name')

meds[['Med_Name', 'Note', 'EmergencyStatus']].to_csv("MEDICATIONS.csv", index=False)


init_units = {'SpecialHigh':np.random.choice(range(30, 45)),
              'Common':30,
              'Moderate':20,
              'Rare':10,
              'SpecialLow':np.random.choice(range(30, 45)) # also setting high, even though rarely dispensed
              }


stockout_range = {'SpecialLow':range(2, 8),
                  'Rare':range(10, 30),
                  'Moderate':range(25, 50),
                  'Common':range(65, 105),
                  'SpecialHigh':range(150, 200)
                  }


def ID(): return(''.join(random.choices(string.ascii_uppercase + string.digits, k=12)))
ID()



# Machine 1 - Emergency Department 
    # ibuprofen will be rarely given out 
    # furosemide will be rarely given out BUT is emergency status 
    # Metoprolol will stock our  frequently 
    # ibuprofen will be rarely given
    # pravastatin 10 mg TAB will not have been dispensed at all 
    # furosemide will be rare BUT emergency status so can't replace 
    
    
## Starting Inventory 
meds_ED = meds.loc[meds['ED_Rarity']!='None',
                   ['Med_Name', 'ED_Rarity', 'EmergencyStatus']]


meds_ED['Init'] = meds_ED['ED_Rarity'].apply(lambda rarity: init_units.get(rarity))


## Setting unique meds as outlined above
meds_ED.loc[meds_ED['Med_Name'].isin(['ibuprofen 200mg TAB',
                                  'ibuprofen 400mg TAB',
                                  'furosemide 40mg TAB',
                                  ]), 'ED_Rarity'] = 'SpecialLow'

meds_ED.loc[meds_ED['Med_Name'].isin(['metoprolol succinate ER 25mg TAB',
                                  'metoprolol tartrate 25mg TAB',
                                  ]), 'ED_Rarity'] = 'SpecialHigh'



ED_meds_df = pd.DataFrame(data=None, columns=['TransactionID', 'Machine', 'Day',
                                         'Medication', 'Type', 'AmtRemaining'])

for med in meds_ED.loc[meds_ED['ED_Rarity']!='', 'Med_Name']:
    rarity = meds_ED.loc[meds_ED['Med_Name']==med, 'ED_Rarity'].item()    
    ED_meds_df .loc[ED_meds_df .shape[0], :] = [ID(), 1, 'day', med, 'Withdrawal', init_units[rarity]-1]    
    stockouts = 0
    limit = np.random.choice(stockout_range[rarity])    
    while stockouts<=limit:
        if ED_meds_df .loc[ED_meds_df .shape[0]-1, 'AmtRemaining']>0:
            ED_meds_df .loc[ED_meds_df .shape[0], :] = [ID(), 1, 'day', med, 'Withdrawal', 
                                            max(0, ED_meds_df .loc[ED_meds_df .shape[0]-1, 'AmtRemaining']-np.random.choice([1, 2, 3]))]
        else:
            ED_meds_df .loc[ED_meds_df .shape[0], :] = [ID(), 1, 'day', med, 'Refill', init_units[rarity]]
            stockouts += 1

ED_meds_df .loc[ED_meds_df .shape[0], :] = [ID(), 1, 'day', 'pravastatin 10mg TAB','Withdrawal', 14]
            

# Checking frequency of stock-outs
pd.crosstab(ED_meds_df ['Medication'], ED_meds_df ['Type']).sort_values('Refill')

transact_tot = ED_meds_df ['Medication'].value_counts().reset_index() 
transact_tot.columns = ['Medication', 'StockOutFreq'] 


m1_df_freq = ED_meds_df .merge(transact_tot, on='Medication')
m1_df_freq['TransactNo'] = m1_df_freq.groupby('Medication').cumcount()+1
m1_df_freq['DayNum'] = round(365*m1_df_freq['TransactNo'] / m1_df_freq['StockOutFreq'])

for i in range(m1_df_freq.shape[0]):
    m1_df_freq.loc[i, 'Day'] = (datetime.date(2020, 1, 1) + datetime.timedelta(m1_df_freq.loc[i, 'DayNum'])).strftime('%Y-%m-%d')

em_dept_meds = m1_df_freq.drop(['StockOutFreq', 'TransactNo', 'DayNum'], axis=1)

em_dept_meds.to_csv('EmergencyDepartmentTransactions.csv')

####################################################################################



# Machine 2 (Surgery, Neurology)
    # acetaZOLAMIDE 125mg TAB
    # acetaZOLAMIDE 250mg TAB
    # EPINEPHrine 0.3mg/0.3mL 0.3mL PE
    # enoxaparin 60mg/0.6mL 0.6mL SYRINGE
    # enoxaparin 80mg/0.8mL 0.8mL SYRINGE


meds_2 = meds.loc[(meds['Neurology_Rarity']!='None') | (meds['GenSurgery_Rarity']!='None'),
                   ['Med_Name', 'Neurology_Rarity', 'GenSurgery_Rarity', 'EmergencyStatus']]


meds_2 ['Init'] = meds_2['Neurology_Rarity'].apply(lambda rarity: init_units.get(rarity)) + meds_2['GenSurgery_Rarity'].apply(lambda rarity: init_units.get(rarity))
                  


## Setting unique meds as outlined above
meds_2.loc[meds_2['Med_Name'].isin(['DAPTomycin PFI 50mg/1mL 10mL INJ', # emergency status=Yes
                                     'enoxaparin 120mg/0.8mL 0.8mL SYRINGE'
                                  ]), 'ED_Rarity'] = 'SpecialLow'
    # Only setting one non-emergent meds as specialty low (with its lower dosages set as specialhigh so an easy replacement), 
    # Letting the randomization run, see if there are valid  meds to replace and leave this somewhat open ended to 
    # justify inventory changes to be made 

meds_2.loc[meds_2['Med_Name'].isin(['acetaZOLAMIDE 125mg TAB',
                                     'acetaZOLAMIDE 250mg TAB',
                                     'EPINEPHrine 0.3mg/0.3mL 0.3mL PEN',
                                     'enoxaparin 60mg/0.6mL 0.6mL SYRINGE',
                                     'enoxaparin 80mg/0.8mL 0.8mL SYRINGE'
                                     ]), 'ED_Rarity'] = 'SpecialHigh'



mach2_meds_df = pd.DataFrame(data=None, columns=['TransactionID', 'Machine', 'Day',
                                         'Medication', 'Type', 'AmtRemaining'])


for med in meds_2.loc[(meds_2['Neurology_Rarity']!='') | (meds_2['GenSurgery_Rarity']!=''), 'Med_Name']:
    rarity = np.where(meds_2.loc[meds_2['Med_Name']==med, 'GenSurgery_Rarity'].item()!='None', # arbitrarily prioritizing gen surgery over neuro
                      meds_2.loc[meds_2['Med_Name']==med, 'GenSurgery_Rarity'].item(),
                      meds_2.loc[meds_2['Med_Name']==med, 'Neurology_Rarity'].item()).item()
    meds_2.loc[meds_2['Med_Name']==med, 'ED_Rarity'].item()    
    mach2_meds_df .loc[mach2_meds_df .shape[0], :] = [ID(), 1, 'day', med, 'Withdrawal', init_units[rarity]-1]    
    stockouts = 0
    limit = np.random.choice(stockout_range[rarity])    
    while stockouts<=limit:
        if mach2_meds_df .loc[mach2_meds_df .shape[0]-1, 'AmtRemaining']>0:
            mach2_meds_df .loc[mach2_meds_df .shape[0], :] = [ID(), 1, 'day', med, 'Withdrawal', 
                                            max(0, mach2_meds_df .loc[mach2_meds_df .shape[0]-1, 'AmtRemaining']-np.random.choice([1, 2, 3]))]
        else:
            mach2_meds_df.loc[mach2_meds_df.shape[0], :] = [ID(), 1, 'day', med, 'Refill', init_units[rarity]]
            stockouts += 1


# Checking frequency of stock-outs
pd.crosstab(mach2_meds_df['Medication'], mach2_meds_df['Type']).sort_values('Refill')

transact_tot = mach2_meds_df['Medication'].value_counts().reset_index() 
transact_tot.columns = ['Medication', 'StockOutFreq'] 


m2_df_freq = mach2_meds_df.merge(transact_tot, on='Medication')
m2_df_freq['TransactNo'] = m2_df_freq.groupby('Medication').cumcount()+1
m2_df_freq['DayNum'] = round(365*m2_df_freq['TransactNo'] / m2_df_freq['StockOutFreq'])

for i in range(m2_df_freq.shape[0]):
    m2_df_freq.loc[i, 'Day'] = (datetime.date(2020, 1, 1) + datetime.timedelta(m2_df_freq.loc[i, 'DayNum'])).strftime('%Y-%m-%d')

neuro_surg_meds = m2_df_freq.drop(['StockOutFreq', 'TransactNo', 'DayNum'], axis=1) 

neuro_surg_meds.to_csv('Neuro_Surgery_Transactions.csv', index=False)


# Machine 3 (Oncology, Dermatology)
    # levothyroxine 100mcg TAB -- only one specialty high med, and the only specialty low will be an emergent 
    # furosemide 40mg TAB -- our dermatological emergency status med (used for edemas)

meds_3 = meds.loc[(meds['Oncology_Rarity']!='None') | (meds['Dermatology_Rarity']!='None'),
                   ['Med_Name', 'Oncology_Rarity', 'Dermatology_Rarity', 'EmergencyStatus']]


meds_3['Init'] = meds_3['Dermatology_Rarity'].apply(lambda rarity: init_units.get(rarity)) + meds_3['Oncology_Rarity'].apply(lambda rarity: init_units.get(rarity))


## Setting unique meds as outlined above
meds_3.loc[meds_3['Med_Name'] == 'levothyroxine 100mcg TAB', 'ED_Rarity'] = 'SpecialHigh'

meds_3.loc[meds_3['Med_Name'] == 'furosemide 40mg TAB' , 'ED_Rarity'] = 'SpecialLow'



mach3_meds_df = pd.DataFrame(data=None, columns=['TransactionID', 'Machine', 'Day',
                                         'Medication', 'Type', 'AmtRemaining'])

for med in meds_3.loc[meds_3['ED_Rarity']!='', 'Med_Name']:
    rarity = np.where(meds_3.loc[meds_3['Med_Name']==med, 'Oncology_Rarity'].item()!='None', # arbitrarily prioritizing gen surgery over neuro
                      meds_3.loc[meds_3['Med_Name']==med, 'Oncology_Rarity'].item(),
                      meds_3.loc[meds_3['Med_Name']==med, 'Dermatology_Rarity'].item()).item()
    mach3_meds_df.loc[mach3_meds_df.shape[0], :] = [ID(), 1, 'day', med, 'Withdrawal', init_units[rarity]-1]    
    stockouts = 0
    limit = np.random.choice(stockout_range[rarity])    
    while stockouts<=limit:
        if mach3_meds_df.loc[mach3_meds_df.shape[0]-1, 'AmtRemaining']>0:
            mach3_meds_df.loc[mach3_meds_df.shape[0], :] = [ID(), 1, 'day', med, 'Withdrawal', 
                                            max(0, mach3_meds_df.loc[mach3_meds_df.shape[0]-1, 'AmtRemaining']-np.random.choice([1, 2, 3]))]
        else:
            mach3_meds_df.loc[mach3_meds_df.shape[0], :] = [ID(), 1, 'day', med, 'Refill', init_units[rarity]]
            stockouts += 1


# Checking frequency of stock-outs
pd.crosstab(mach3_meds_df['Medication'], mach2_meds_df['Type']).sort_values('Refill')

transact_tot = mach3_meds_df['Medication'].value_counts().reset_index() 
transact_tot.columns = ['Medication', 'StockOutFreq'] 


m3_df_freq = mach3_meds_df.merge(transact_tot, on='Medication')
m3_df_freq['TransactNo'] = m3_df_freq.groupby('Medication').cumcount()+1
m3_df_freq['DayNum'] = round(365*m3_df_freq['TransactNo'] / m3_df_freq['StockOutFreq'])

for i in range(m3_df_freq.shape[0]):
    m3_df_freq.loc[i, 'Day'] = (datetime.date(2020, 1, 1) + datetime.timedelta(m3_df_freq.loc[i, 'DayNum'])).strftime('%Y-%m-%d')

derm_onc_meds = m3_df_freq.drop(['StockOutFreq', 'TransactNo', 'DayNum'], axis=1) 

derm_onc_meds .to_csv('Onc_Derm_Transactions.csv', index=False)


####################################################################################
'''  
# Misc temporal trends I was considering 

## Weekly Trend 

### ONDANsetron ODT 4mg TAB 
### More heavily used Mon-Wed (more commonly when surgeries may be held so post-op care can take palce during the week, when services are more heavily staffed)
### Aenesthesia for nausea post-surg 


## Annual Trend(s)

### ED 
#### DOPamine in D5W 800mcg/1mL 250mL INJ
#### Injection common with shock/trauma 
#### More common during summer (more trauma admissions)

### Dermatology
#### hydrocortisone 1% 1app CREAM )(specifically the cream, not the tabs)
#### Specifically in dermatology clinics, sunburns/post-summer skin treatment
#### More common in July/August 
'''