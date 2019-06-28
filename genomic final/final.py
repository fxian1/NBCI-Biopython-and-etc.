#!/anaconda3/bin/python

dna_data = {}

f = open("../dna2.fasta")

for line in f:
	line = line.rstrip()
	if line[0] == '>':
		words = line.split('|')
		identifier = words[0][1:]
		number = words[4].split(' ')[0]
		name = identifier + ' ' + number
		dna_data[name] = ''
	else:
		dna_data[name] = dna_data[name] + line

f.close()

"""
f = open("output.txt", 'w')

for name in dna_data:
	f.write(name)
	f.write('\n')
	f.write(dna_data[name])
	f.write(' ' + str(len(dna_data[name])))
	f.write('\n')

f.close()

print(len(dna_data.keys()))

sorted_rec = {}

for name in dna_data:
	sorted_rec[len(dna_data[name])] = name


for i in sorted(sorted_rec):
	print(sorted_rec[i] + ', ' + str(i))
"""
####
#Part 3

def to_seq_start(codon_start, frame):
	if frame == 1:
		return codon_start*3+1
	if frame == 2:
		return codon_start*3+2
	if frame == 3:
		return codon_start*3+3

def convert_to_list(sequence):
	codon_list = []
	c=0
	for i in range(int(len(sequence)/3)):
		codon_list.append(sequence[c:c+3])
		c = c+3
	leftover = sequence[c:]
	if len(leftover) != 0:
		codon_list.append(leftover)
	return codon_list

def find_all_start(codon_list):
	positions = []
	#dont need to check last two codons, unless last one is full codon and stop
	for i in range(len(codon_list)-1):
		if codon_list[i] == 'ATG':
			positions.append(i)
	if (codon_list[-1] == 'TAA' or codon_list[-1] == 'TAG' or codon_list[-1] == 'TGA') and codon_list[-2] == 'ATG':
			positions.append(len(codon_list)-2)
	return positions

def find_all_stop(codon_list):
	positions = []

	for i in range(len(codon_list)):
		if codon_list[i] == 'TAA' or codon_list[i] == 'TAG' or codon_list[i] == 'TGA':
			positions.append(i)
	return positions


#ATG start
#TAA, TAG, TGA stop
#returns all orfs for a single continuous sequence
def find_ORFs(sequence, frame, title): 
	ORFs = {} #key: orf, value: starting position

	if frame == 1:
		pass
	if frame == 2:
		sequence = sequence[1:]
	if frame == 3:
		sequence = sequence[2:]

	if sequence.find('ATG') != -1:
		codon_list = convert_to_list(sequence)
		start_list = find_all_start(codon_list)
		end_list = find_all_stop(codon_list)
		if len(end_list) == 0:
			return None
		for start in start_list:
			end_pos=0
			while(end_pos < len(end_list) and len(end_list) != 1):
				if end_list[end_pos] > start:
					break
				else:
					end_pos += 1

			if end_pos == len(end_list):
				end_pos -= 1
			if end_list[end_pos] < start:
				break
			else:
				orf_list = codon_list[start:end_list[end_pos]+1]
				orf = ''.join(orf_list)
				ORFs[orf] = 'Starts at position ' + str(to_seq_start(start,frame)) + ' in ' + title
		return ORFs
	
	else:
		return None

"""
orf1 = find_ORFs(dna_data['gi 16'], 1)

for key in orf1:
	print(key + ', ' + str(orf1[key]) + '\n')

orf_sort = {}
for key in orf1:
	orf_sort[len(key)] = key + ' ' + str(orf1[key])

for key in sorted(orf_sort):
	print(orf_sort[key] + ', ' + str(key) + '\n')

"""

#Longest ORF for all records
large_orf = {}

#for title in dna_data:
for i in range(1,4):
	orf = find_ORFs(dna_data['gi 16'],i,'gi 16')
	if orf is not None:
		large_orf.update(orf)


orf_sort = {}
for key in large_orf:
	orf_sort[len(key)] = key + ' ' + str(large_orf[key])

for key in sorted(orf_sort):
	print(orf_sort[key] + ', ' + str(key) + '\n')


#Part 4

def find_repeat(seq_list, length):
	repeat = {}

	for title in seq_list:
		seq = seq_list[title]
		print(title)
		for i in range(0,len(seq)-length):
			repeat_seq = seq[i:i+length]
			print(repeat_seq)
			if repeat_seq in repeat.keys():
				repeat[repeat_seq] += 1
			else:
				repeat[repeat_seq] = 1

	return repeat


all_repeats = find_repeat(dna_data, 12)
sorted_repeats = {}

for repeat in all_repeats:
	sorted_repeats[all_repeats[repeat]] = repeat

for freq in sorted(sorted_repeats):
	print(sorted_repeats[freq] + ', ' + str(freq))






