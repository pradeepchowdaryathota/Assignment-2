#!/usr/bin/env python
# coding: utf-8

# In[1]:


###Q1
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


# In[2]:


###Q2
# Open the file which containing the sequence
with open(r"C:\cygwin64\home\pradeepchowdary\Informatics_573\chr1_GL383518v1_alt.fa",'r') as file:
    # Skip the first line which is header
    file.readline()
    # Read the rest of the file and replace the empty strings and newcharacters in new line
    sequence = file.read().replace('\n', '')
    
# create a dictionary for the complementary sequences
complement_dict = {"A":"T","a":"t","T":"A","t":"a","C":"G","c":"g","G":"C","g":"c"}
# reverse the sequence
reverse_sequence = sequence[::-1]

# join the complementary sequences to the reverse sequence
reverse_complement_sequence = ''.join(complement_dict.get(base,base) for base in reverse_sequence)

print("79th letter of the reverse complement sequence:", reverse_complement_sequence[78])

print("The 500th through the 800th letters of this sequence:",reverse_complement_sequence[499:800])  


# In[3]:


###Q3
with open(r"C:\cygwin64\home\pradeepchowdary\Informatics_573\chr1_GL383518v1_alt.fa",'r') as file:
    # Skip the first line which is header
    file.readline()
    # Read the rest of the file and replace the empty strings and newcharacters in new line
    sequence = file.read().replace('\n', '')

# size of the kilobase window
window_size = 1000

# nested dictionary to store the sequence counts
sequence_counts = {}

# iterate over the sequence in kilobase window
for i in range(0,len(sequence),window_size):
    start = i
    end = min(i+window_size,len(sequence))
    
    # dictionary to store to counts for this specific window
    window_counts = {'A':0,'T':0,'G':0,'C':0,'a':0,'t':0,'g':0,'c':0}
    
    # Occurence of base in this window size
    for base in sequence[start:end]:
        if base in window_counts:
            window_counts[base] += 1
        
    # store the counts for this kilobase window    
    sequence_counts[i//1000] = window_counts
    
#print nested dictionary
for kilobase, counts in sequence_counts.items():
    print(f"Kilobase {kilobase}: {counts}")


# In[4]:


##Q4(a)
# get the counts for first kilobase
first_kilobase_counts = sequence_counts[0]

# Create a list containing the number of times each nucleotide (A,C,G,T) is contained in the first 1000 base pairs.

nucleotide_counts = [
    first_kilobase_counts.get('A', 0),
    first_kilobase_counts.get('C', 0),
    first_kilobase_counts.get('G', 0),
    first_kilobase_counts.get('T', 0),
    first_kilobase_counts.get('a', 0),
    first_kilobase_counts.get('c', 0),
    first_kilobase_counts.get('g', 0),
    first_kilobase_counts.get('t', 0)
]

print("Counts of each nucleotide in the first 1000 base pairs:", nucleotide_counts)


# In[5]:


###Q4(b)

all_kilobase_counts = []

for i in range(0, len(sequence) ,1000):
    nucleotide_counts = [0,0,0,0,0,0,0,0]
    for base in sequence[i:i+1000]:
        if base == 'A' :
            nucleotide_counts[0] += 1
        elif base == 'T' :
            nucleotide_counts[1] += 1
        elif base == 'G':
            nucleotide_counts[2] += 1
        elif base == 'C':
            nucleotide_counts[3] +=1
        elif base == 'C':
            nucleotide_counts[3] +=1
        elif base == 'a':
            nucleotide_counts[4] +=1
        elif base == 'c':
            nucleotide_counts[5] +=1
        elif base == 'g':
            nucleotide_counts[6] +=1
        elif base == 't':
            nucleotide_counts[7] +=1
    all_kilobase_counts.append(nucleotide_counts)
        
print("Counts of nucleotides for each kilobase:", all_kilobase_counts)


# In[6]:


#Q4 (C)
# create an empty list for each kilobase counts
each_kilobase_counts = []

# create a loop to iterate over all sequences 
for i in range(0, len(sequence), 1000):
    kilobase = sequence[i:i+1000]
    nucleotide_counts = [kilobase.count(base) for base in 'ACGTacgt']
    
    each_kilobase_counts.append(nucleotide_counts)

print("Occurrences of each nucleotide in each kilobase:")
for i, counts in enumerate(each_kilobase_counts):
    print(f"Kilobase {i+1}: {counts}")


# In[7]:


### Q4(d)
# create an empty list to store sums of each list
sum_of_each_kilobase = []
 
# iterate over every list in the each kilobase counts
for each_list in each_kilobase_counts:
        each_list_sum = sum(each_list)
        sum_of_each_kilobase.append(each_list_sum)
    
print("Sum of each kilobase:",sum_of_each_kilobase)


# In[ ]:


### Q4(e)

# 1. Expected sum for the each list is 1000.
# 2.yes, sum of the list of every kilobase is 1000 except the last kilobase is with only the sum of 439.
# 3. The difference is because the we assigned a value of 1000 for kilobase and the in the last kilobase we only had the 439 seuences where the sequence of teh chromosome ended.so,it has different sum than expected.

