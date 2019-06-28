#!/anaconda3/bin/python

from fasta_functions import *
import sys

def main():
	filename = input('Please Enter FASTA file name: ')
	frame = input('Please Enter 1, 2, 3 for frame, or 4 for all frames: ')

	try:
		frame = int(frame)
	except TypeError:
		sys.stderr.write('Invalid frame entered')
		frame = 1

	if not isinstance(filename, str):
		sys.stderr.write('Invalid Filename entered')
		return 1
	if frame > 4:
		sys.stderr.write('Invalid frame entered')
		return 2

	try:
		f = open(filename)
		seq_list = make_dict(f)
		f.close()
	except IOError as e:
		errno, strerror = e.args
		print("I/O error({0}): {1}".format(errno,strerror))
	except ValueError:
		print("No valid integer in line.")
	except:
		print("Unexpected error:", sys.exc_info()[0])
		raise

	file_orf = {}
	if frame == 4:
		for seq in seq_list:
			for i in range(1,4):
				orf = find_ORFs(seq_list[seq],i,seq)
				if orf is not None:
					file_orf.update(orf)
	else:
		for seq in seq_list:
			orf = find_ORFs(seq_list[seq],frame,seq)
			if orf is not None:
				file_orf.update(orf)

	f = open('max_orf.txt','w')
	orf_sort = {}
	for orf in file_orf:
		orf_sort[len(orf)] = orf + ' ' + str(file_orf[orf])
	orf_sorted = sorted(orf_sort)
	f.write("Longest ORF Sequence: %s \nLength: %d \n"
		% (orf_sort[orf_sorted[-1]], orf_sorted[-1]))
	f.close()
	return 0

if __name__ == "__main__":
	main()

