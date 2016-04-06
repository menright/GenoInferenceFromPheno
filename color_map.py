import sys
from collections import defaultdict
from genotype import Genotype

class ColorMap:
	def __init__(self, filename):
		self.color_map = self.construct_color_map(filename)
		self.allele_genotype  = self.list_genotypes_for_allele(filename)
	# maps color phenotypes to a list of genotypes
	def construct_color_map(self, filename):
		file = open(filename, 'r')
		genes_dict = defaultdict(list)
		line = file.readline().strip()
		while(line != [''] and line != ''):
			gene = Genotype(line)
			genes_dict[gene.phenotype].append(gene)
			line = file.readline()
		return genes_dict

	def list_genotypes_for_allele(self, filename):
		file = open(filename, 'r')
		genes_set = defaultdict(set)
		line = file.readline().strip()
		while(line != [''] and line != ''):
			genes = line.strip().split('\t')
			pheno = genes.pop(0)
			for gene in genes:
				letter = gene[0]
				key = (pheno, letter.lower())
				genes_set[key].add(gene)
			line = file.readline()
		return genes_set

	def __str__(self):
		print "Genotype representation: "
		for phen in self.color_map:
			print "Phenotype: " + str(phen)
			for list in self.color_map[phen]:
				print " [" + str(list) + "]"