#!/anaconda3/bin/python

#This program finds the longest sequence in a given FASTA format file 
#command line arg - file name 

from fasta_functions import make_dict
import sys

def main():
	if len(sys.argv) < 2:
		sys.stderr.write('Please enter a FASTA file name')
		return 1

	if len(sys.argv) > 2:
		sys.stderr.write('Too many arguments entered')
		return 2

	try:
		f = open(str(sys.argv[1]))
		seq = make_dict(f)
		f.close()
	except IOError as e:
		errno, strerror = e.args
		print("I/O error({0}): {1}".format(errno,strerror))
	except ValueError:
		print("No valid integer in line.")
	except:
		print("Unexpected error:", sys.exc_info()[0])
		raise

	
	f = open('max_length_seq.txt','w')
	sorted_rec = {}
	for name in seq:
		sorted_rec[len(seq[name])] = name
	for i in sorted(sorted_rec):
		if len(sorted_rec[i]) == 4:
			sorted_rec[i] += '  '
		if len(sorted_rec[i]) == 5:
			sorted_rec[i] += ' '
		f.write("Name of Sequence: %s  Length of Sequence: %d \n"
			% (sorted_rec[i], i))
	f.write('Total Number of Sequences: %s \n' % (str(len(seq.keys()))))
	f.close()
	return 0

if __name__ == "__main__":
	main()


