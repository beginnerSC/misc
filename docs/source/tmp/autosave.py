#!/usr/bin/env python
# coding: utf-8

# # Autosave
# 
# * Below is how subprocess can call an alias, code from [here](https://stackoverflow.com/questions/12060863/python-subprocess-call-a-bash-alias). 
# * In terminal, turn this into a python script, say ```autosave.ipynb``
#     ```
#     jupyter nbconvert --to script autosave.ipynb
#     ```
# * Also in terminal ```python autosave.py```
# * This can be used with the schedule library
# 

# In[ ]:


import schedule 
import datetime, time, subprocess

def autosave():
    subprocess.call(['/bin/bash', '-i', '-c', 'cnp'])
    print('Pushed', datetime.datetime.now())

if __name__ == '__main__':
    schedule.every(5).minutes.do(autosave)
    while True:
        schedule.run_pending() 
        time.sleep(1) 

