import sys
from collections import defaultdict

#contains a mapping of possible alleles with letter signifiers:
# ie A: [At,At] [A,At]. phenotype: white&tan
# B: [bb] [Bb]
#special case Cch
class Genotype:
	def __init__(self, line):
		self.allele_map = defaultdict(list)
		#split genes
		genes = line.strip().split('\t')
		#display type
		self.phenotype = genes[0]
		genes.pop(0)
		self.genotype = ""

		for allele in genes:
			self.genotype += allele
			#identify each allele
			current_letter = allele[0].lower()
			current_string=""
			for letter in allele:
				#skip if we are at the beginning
				#CCh ChCh  CC dd Dd  AAt     A  A
				if current_string != "":
					if(current_letter.upper() == letter or current_letter.lower() == letter):
						#end the current string and add to dict
						self.allele_map[current_letter].append(current_string)
						#reset the current string
						current_string = ""
				#start parsing new allele
				current_string += letter
				#add the parsed allele to the map for that letter signifier
			self.allele_map[current_letter].append(current_string)

	def __str__(self):
		print "Genotype: " + str(self.genotype) + " ["+str(self.phenotype) + "]" + " map: " + str(self.allele_map)

	def __repr__(self):
		return "Genotype: " + str(self.genotype) + " ["+str(self.phenotype) + "]" + " map: " + str(self.allele_map)