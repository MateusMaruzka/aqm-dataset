#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 17:14:08 2023

@author: mateus
"""

import pandas as pd

# Step 1: Load the first dataset
df1 = pd.read_csv('e1_df.csv')  # Replace 'path/to/dataset1.csv' with the actual file path of your first dataset

# Step 2: Load the second dataset
df2 = pd.read_csv('e2_df.csv')  # Replace 'path/to/dataset2.csv' with the actual file path of your second dataset

df3 = pd.read_csv('e2sp_df.csv')  # Replace 'path/to/dataset2.csv' with the actual file path of your second dataset


# Step 3: Join the datasets side by side
joined_df = pd.concat([df1, df2, df3], axis=1)

joined_df.to_csv('all_tago_df.csv', index=True)  # Replace 'path/to/save/modified_df.csv' with the actual file path where you want to save the DataFrame

# Step 4: Output the joined DataFrame
print(joined_df)