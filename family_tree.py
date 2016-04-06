#Madeline Enright
import sys
from collections import defaultdict
from dog import Dog
from genotype import Genotype
from color_map import ColorMap

class FamilyTree:
	def __init__(self, filename, color_map):
		self.file = open(filename, 'r')
		self.root = self.constructTree()
		self.poss_genes = {}
		self.poss_geneotypes = {}
		self.color_map = color_map.color_map
		self.allele_genotype = color_map.allele_genotype

	#This function constructs a tree from filename
	def constructTree(self):
		#Read next item from file. If theere are no more items or next
		#item is marker, then return
		line = self.file.readline().split(',')
		if line == [''] or line == ["-1\n"] or line==["-1"]:
			return

		#Else create node with this item and recur for children
		name = line[0].strip()
		color = line[1].strip()

		node = Dog(name, color);
		node.dam = self.constructTree()
		node.sire = self.constructTree()
		return node

	#postorder traversal to assign genotypes
	def assignGenotypes(self, node):
		if node:
			self.assignGenotypes(node.dam)
			self.assignGenotypes(node.sire)
			self.visit(node)
			return node

	def visit(self, node):
		genes_list = self.get_genotypes_for_phenotype(node.color)
		if(node.dam) and (node.sire):
			combos = self.combine_parent_alleles(node.sire, node.dam)
			valid_combos = self.remove_invalid_combos_for_phenotype(combos, node)
			full_genos = self.create_full_genotypes(valid_combos, node)
			self.poss_geneotypes[node] = (full_genos)
			genotypes = []
			for line in full_genos:
				genotypes.append(Genotype(line))
			self.poss_genes[node] = genotypes

		else:
			self.poss_genes[node] = genes_list
			self.poss_geneotypes[node] = (genes_list)

	def combine_parent_alleles(self, sire, dam):
		offspring_alleles = defaultdict(set)
		for gene in self.poss_genes[sire]:
			for allele in gene.allele_map:
				unique_genes = set()
				for dam_gene in self.poss_genes[dam]:

					combos = [dam_gene.allele_map[allele][0], gene.allele_map[allele][0]]
					combos.sort()
					string = combos[0]+combos[1]
					unique_genes.add(string)

					combos = [dam_gene.allele_map[allele][0], gene.allele_map[allele][1]]
					combos.sort()
					string = combos[0]+combos[1]
					unique_genes.add(string)

					combos = [dam_gene.allele_map[allele][1], gene.allele_map[allele][0]]
					combos.sort()
					string = combos[0]+combos[1]
					unique_genes.add(string)

					combos = [dam_gene.allele_map[allele][1], gene.allele_map[allele][1]]
					combos.sort()
					string = combos[0]+combos[1]
					unique_genes.add(string)
				for combo in unique_genes:
					offspring_alleles[allele].add(combo)
		return offspring_alleles

	def remove_invalid_combos_for_phenotype(self, combos, node):
		valid_alleles = defaultdict(list)
		for allele in combos:
			valid = combos[allele].intersection(self.allele_genotype[(node.color, allele)])
			valid_alleles[allele] = valid
		return valid_alleles

	def create_full_genotypes(self, combos, node):
		valid_genotypes = []
		for a in combos["a"]:
			for b in combos["b"]:
				for s in combos["s"]:
					color_exp = str(node.color) + "\t" + a + "\t" + b + "\t" + s
					valid_genotypes.append(color_exp)
		return valid_genotypes

	def get_genotypes_for_phenotype(self, color):
		return self.color_map[color]

	def get_phenotypes_for_genotype(self, geno):
		for key, value in self.color_map:
			if geno in value:
				print "Phenotype is " + key