#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install pymysql


# In[4]:


pip install cx_Oracle


# In[5]:


pip install tabulate


# In[6]:


pip install pyodbc


# In[8]:


import csv
import pandas as pd
import mysql.connector
con = mysql.connector.connect(host='academicmysql.mysql.database.azure.com',
                              database='axk7120',
                              user='axk7120',
                              password='Akhila@1996')

cur = con.cursor()
cur.execute("select database()")  #provides database name
value = cur.fetchone()  #retrieves next tuple
print("connected",value)

def  InsertIntoTable(location, name_table):
    new_file = pd.read_csv(location,delimiter = ',')  #reads the csv file
    new_file.head() #Retrieves n no of rows
    print(new_file)
    new_file = new_file.where((pd.notnull(new_file)), None)
    for i,row in new_file.iterrows():
        s_qu_y = name_table  #Insert query statement
        print(row)
        cur.execute(s_qu_y ,tuple(row)) 
        
        us_state = "INSERT INTO STATE VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        InsertIntoTable('US_state.csv' , us_state) 
        
        
        
    new_file = new_file.where((pd.notnull(new_file)), None)
    for i,row in new_file.iterrows():
        s_qu_y = name_table  #Insert query statement
        print(row)
        cur.execute(s_qu_y ,tuple(row)) 
        
        us_county = "INSERT INTO COUNTY VALUES(%s,%s,%s,%s,%s)"
        InsertIntoTable('Us_County.csv' , us_county) 
            
            
            
            
    new_file = new_file.where((pd.notnull(new_file)), None)
    for i,row in new_file.iterrows():
        s_qu_y = name_table  #Insert query statement
        print(row)
        cur.execute(s_qu_y ,tuple(row)) 
        
        us_c_c = "INSERT INTO CONFIRMED_CASES VALUES(%s,%s,%s,%s)"
        InsertIntoTable('Us_confirmed_cases.csv' , us_c_c)
            
            
    new_file = new_file.where((pd.notnull(new_file)), None)
    for i,row in new_file.iterrows():
        s_qu_y = name_table  #Insert query statement
        print(row)
        cur.execute(s_qu_y ,tuple(row)) 
        
        us_deaths = "INSERT INTO DEATHS VALUES(%s,%s,%s,%s)"
        InsertIntoTable('Us_deaths.csv' , us_deaths)
        
        
    new_file = new_file.where((pd.notnull(new_file)), None)
    for i,row in new_file.iterrows():
        s_qu_y = name_table  #Insert query statement
        print(row)
        cur.execute(s_qu_y ,tuple(row)) 
        
        us_vacc = "INSERT INTO VACCINATIONS VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        InsertIntoTable('Us_Vaccinations.csv' , us_vacc)
            
        #print("record inserted")
        
        
        
        
    cur.close()  
    con.commit()
    con.close    



# In[ ]:





# In[ ]:





# In[ ]:




