#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install d3blocks


# In[2]:


import pandas as pd
import numpy as np
from d3blocks import D3Blocks

# Load the datasets
data = pd.read_csv('/Users/pranav/Desktop/Python/D3 Blocks/Sample_data_moving_bubbles.csv')


# In[3]:


data


# In[4]:


# Load d3blocks
d3 = D3Blocks()


# Generate moving bubbles visualization
d3.movingbubbles(
    data, 
    speed={"slow": 1000, "medium": 200, "fast": 10}, 
    filepath='movingbubbles.html')


# In[5]:


import pandas as pd

# Sample DataFrame creation
# Assuming df has columns: 'datetime', 'sample_id', 'state'
# Here's a quick example structure (you would replace this with your actual DataFrame)
data = {
    'datetime': pd.date_range("2023-04-14 00:00", periods=24, freq='H').repeat(50),
    'sample_id': list(range(50)) * 24,
    'state': np.random.choice(['Cardio', 'Strength', 'Swim', 'Class', 'Sauna', 'Functional'], size=1200)
}
df = pd.DataFrame(data)


# Implementing the closing time rule: gym is closed from 9 PM to 6 AM
df['hour'] = df['datetime'].dt.hour
df.loc[(df['hour'] >= 21) | (df['hour'] < 6), 'state'] = 'Out of the Gym'

# Remove the temporary 'hour' column
df.drop('hour', axis=1, inplace=True)


# Display the head of the DataFrame to verify changes
print(df.head())


# In[6]:


# Load d3blocks
d3 = D3Blocks()


# Generate moving bubbles visualization
d3.movingbubbles(
    df, 
    speed={"slow": 1000, "medium": 200, "fast": 10}, 
    filepath='movingbubbles.html')


# In[ ]:




