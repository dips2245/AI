import nltk
from nltk.tree import Tree

sentence = "The dog is playing on the couch."
parse_tree_string = "(S (NP (Det The) (N dog)) (VP (V is) (VP (V playing) (PP (P on) (NP (Det the) (N couch))))))"
parse_tree = Tree.fromstring(parse_tree_string)
parse_tree.pretty_print()