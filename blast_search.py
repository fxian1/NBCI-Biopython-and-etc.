#!/anaconda3/bin/python

import Bio
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

fasta_string = open("myseq.fa").read()

result_handle = NCBIWWW.qblast("blastn","nt",fasta_string)

blast_record = NCBIXML.read(result_handle)

print(len(blast_record.alignments))

e_val = 0.01

for alignment in blast_record.alignments:
	for hsp in alignment.hsps:
		if hsp.expect < e_val:
			print('Alignment')
			print('seq:', alignment.title)
			print('len:', alignment.length)
			print('e value:', hsp.expect)
			print(hsp.query)
			print(hsp.match)
			print(hsp.sbjct)