
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

# function to get the complementary strand of DNA
def reverse_complement(base):
    # a dictionary to map each DNA base to its complement
    complement_dict = {'A':'T','T':'A','G':'C','C':'G'}
    return complement_dict.get(base,base)

    # reverse the sequence 
    reverse_sequence = sequence[::-1]
    
    # Iterate over each base in the reverse sequence and find its complement
    reverse_complement_sequence = ''.join(reverse_complement(base) for base in reverse_sequence)

print("79th letter of this sequence:",reverse_complement_sequence[78])

print("The 500th through the 800th letters of this sequence:",reverse_complement_sequence[499:800])



# size of the kilobase window
window_size = 1000

# nested dictionary to store the sequence counts
sequence_counts = {}

# iterate over the sequence in kilobase window
for i in range(0,len(sequence),window_size):
    start = i
    end = min(i+window_size,len(sequence))
    
    # dictionary to store to counts for this specific window
    window_counts = {'A':0,'T':0,'G':0,'C':0}
    
    # Occurence of base in this window size
    for base in sequence[start:end]:
        if base in window_counts:
            window_counts[base] += 1
        
    # store the counts for this kilobase window    
    sequence_counts[i//1000] = window_counts
    
#print nested dictionary
for kilobase, counts in sequence_counts.items():
    print(f"Kilobase {kilobase}: {counts}")
    
        
    
