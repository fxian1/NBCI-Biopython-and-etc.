#!/anaconda3/bin/python

from fasta_functions import *
import sys

def main():
	if len(sys.argv) == 1:
		sys.stderr.write('Missing filename and repeat length')
		return 1
	if len(sys.argv) == 2:
		sys.stderr.write('Missing repeat length')
		return 2

	if len(sys.argv) > 3:
		sys.stderr.write('Too many arguments entered')
		return 3

	if isinstance(sys.argv[2], int):
		sys.stderr.write('repeat length must be an integer')
		return 4
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

	repeats = find_repeat(seq, int(sys.argv[2]))

	f = open('max_repeat.txt','w')
	sorted_repeats = {}
	for repeat in repeats:
		sorted_repeats[repeats[repeat]] = repeat
	for i in sorted(sorted_repeats):
		f.write("Repeat Sequence: %s  Frequency: %d \n"
			% (sorted_repeats[i], i))
	f.close()
	return 0

if __name__ == "__main__":
	main()

