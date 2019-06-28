#!/anaconda3/bin/python

#Converts FASTA file information into dictionary to work with
#Key: identifier i.e. gi 41
#Value: Sequence
def make_dict(fileobj):
	seq_list = {}
	for line in fileobj:
		line = line.rstrip()
		if line[0] == '>':
			words = line.split('|')
			identifier = words[0][1:]
			number = words[4].split(' ')[0]
			name = identifier + ' ' + number
			seq_list[name] = ''
		else:
			seq_list[name] = seq_list[name] + line
	return seq_list


#Converts starting position in codon list to sequence list
def to_seq_start(codon_start, frame):
	if frame == 1:
		return codon_start*3+1
	if frame == 2:
		return codon_start*3+2
	if frame == 3:
		return codon_start*3+3

#Converts a string of continuous DNA sequence into a list of codons
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

#Returns a list of codon positions where ATG is found
def find_all_start(codon_list):
	positions = []
	#dont need to check last two codons, unless last one is full codon and stop
	for i in range(len(codon_list)-1):
		if codon_list[i] == 'ATG':
			positions.append(i)
	if (codon_list[-1] == 'TAA' or codon_list[-1] == 'TAG' or codon_list[-1] == 'TGA') and codon_list[-2] == 'ATG':
			positions.append(len(codon_list)-2)
	return positions

#Returns a list of codon positions where STOP codon is found
def find_all_stop(codon_list):
	positions = []

	for i in range(len(codon_list)):
		if codon_list[i] == 'TAA' or codon_list[i] == 'TAG' or codon_list[i] == 'TGA':
			positions.append(i)
	return positions


#ATG start
#TAA, TAG, TGA stop
#Returns all orfs for a single continuous sequence
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

#Finds the repeats with associated frequencies
#Returns Dictionary 
def find_repeat(seq_list, length):
	repeat = {}

	for title in seq_list:
		seq = seq_list[title]
		for i in range(0,len(seq)-length):
			repeat_seq = seq[i:i+length]
			if repeat_seq in repeat.keys():
				repeat[repeat_seq] += 1
			else:
				repeat[repeat_seq] = 1

	return repeat