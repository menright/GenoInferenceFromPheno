#Madeline Enright
import sys
from collections import defaultdict
from color_map import ColorMap
from family_tree import FamilyTree



def main(args):
	color_map = ColorMap('tft_colors.txt')
	family_tree = FamilyTree('tree.txt', color_map)
	family_tree.assignGenotypes(family_tree.root)

	print family_tree.root
	print family_tree.poss_geneotypes[family_tree.root]

if __name__ == "__main__":
	main(sys.argv)
