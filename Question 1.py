#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Open the file which containing the sequence
with open(r"C:\cygwin64\home\pradeepchowdary\Informatics_573\chr1_GL383518v1_alt.fa",'r') as file:
    # Skip the first line which is header
    file.readline()
    # Read the rest of the file and replace the empty strings and newcharacters in new line
    sequence = file.read().replace('\n', '')

# Print the 10th letter of the sequence
print("10th letter of the sequence:", sequence[9])

# Print the 758th letter of the sequence
print("758th letter of the sequence:", sequence[757])


# In[ ]:




