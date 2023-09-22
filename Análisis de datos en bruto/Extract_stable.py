#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pickle
import os
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm as tqdm

general_directory=os.getcwd()+'/Data/'

# In[3]:


def save_dataP(name,dictionary,location=general_directory):

    with open(location+'Saves/'+ name+'.pkl', 'wb') as tf:
        pickle.dump(dictionary,tf)
    


# In[4]:


def census(day,cen):
    with open(general_directory+'Days/'+day) as file:
        orow='0'
        for line in file:
            if line!='zones time_end time_start time_start zones\n':
                row=line.replace("'",'').replace("  ",' ').replace('\n','').split(sep=' ')
                if row[0]!=orow[0]:
                    cen[row[0]]=cen.get(row[0],{'home':[],'work':[]})
                    cen[row[0]]['home']=cen[row[0]].get('home')+[row[3]]
                    cen[row[0]]['work']=cen[row[0]].get('work')+[row[4]]
                    orow=row
       
    


# In[8]:


def stable(censdic):
    estable={}
    for ID in censdic.keys():
        stable_place=0
        gp=[]
        for place in ['home','work']:
            for i in set(censdic[ID][place]):            
                p=censdic[ID][place].count(i)/N
                if 0.5<=p:
                    stable_place+=1
                    gp.append(i)         
        if stable_place==2:
            estable[int(ID)]=estable.get(int(ID),{'home':[],'work':[]})
            estable[int(ID)]['home']=estable[int(ID)].get('home',gp[0])+[gp[0]]
            estable[int(ID)]['work']=estable[int(ID)].get('work',gp[1])+[gp[1]]
    save_dataP('Estables',estable)
    print('Detectados '+ str(len(estable)) +' IDs con comportamiento estable')


# In[6]:


def main():
    get_days()
    if N==0: print('No data yet')
    else:
        print('Days in data: '+str(N))
        cen={}
        print('Starting census')
        list(map(census,tqdm(days,desc='Census'),[cen for i in days]))
        #print([str(list(cen.keys())[i])+':'+str(cen[list(cen.keys())[i]]) for i in range(5)])
        print('Defining stables')
        stable(cen)
        print('Census done')


# In[ ]:


if __name__=="__main__":
    
    main()


# with open(general_directory+'Saves/Estables.pkl','r+b') as pk:
#         estables=pickle.load(pk)
# estables
