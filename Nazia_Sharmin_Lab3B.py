 #Course: Data Structure , Author:Nazia Sharmin, assignment:Lab3B,instructor:Professor-Diego Aguirre,
# T.A.:Anindita Nath, date of last modification:None
from AVLTree import Node, AVLTree
from RedBlackTree import RBTNode, RedBlackTree
from collections import defaultdict

anagram_count = 0

def create_avl_tree(file):
    words_in_my_tree = AVLTree()
    for line in file:
        word = line.strip("\n")
        words_in_my_tree.insert(Node(word))
    file.close()
    return words_in_my_tree

def create_rbt_tree(word_file):
    words_in_my_tree = RedBlackTree()
    for line in word_file:
        word = line.strip("\n")
        words_in_my_tree.insert(word)
    word_file.close()
    return words_in_my_tree

def find_largest_anagram():
    with open("pain.txt", "r") as mytxt:
        for line in mytxt:
            newline = line.rstrip("\n").split("\t")
        anagrams_list = [line]
        anagrams_map = defaultdict(list)
        for ana in anagrams_list:
            anagrams_map[''.join(sorted(ana))].append(ana)
            max_key = max(anagrams_map, key= lambda x: len(set(anagrams_map[x])))
    return max_key, anagrams_map

def print_anagrams(word, treeType, prefix=""):
    global anagram_count
    if len(word) <=1:
        str = prefix + word
        if treeType.search(str):
            anagram_count += 1
            print(prefix+word)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]
            after = word[i + 1:]

            if cur not in before:
                print_anagrams(before + after, treeType, prefix + cur)

def search_word(word, tree):
    if tree.search(word):
        print("Found! Word is available in the tree.")
    else:
        print("Not Found! Word is not available in the tree.")

def user_menu_selection():
    print("1. AVL")
    print("2. Red Black")
    user_choice = input("What type of tree would you like to use (1 or 2)?")
    word = input("What word would you like to search in the tree?")
    return user_choice, word

def main():
	word_file = open("pain.txt", "r")
	user_choice, word = user_menu_selection()
	
	if user_choice == "1":
		word_list_avl = create_avl_tree(word_file)
		search_word(word, word_list_avl)
		anagram = input("\nWhich word do you want to permutate?")
		print_anagrams(anagram, word_list_avl)
	
	else:
		word_list_rbt = create_rbt_tree(word_file)
		search_word(word, word_list_rbt)
		anagram = input("Which word do you want to permutate?")
		print_anagrams(anagram, word_list_rbt)
	
	print("Number of permutations in word file: ", anagram_count)
	max_key, anagrams_map = find_largest_anagram()
	print("\nGreatest number of anagrams found for the word:", anagrams_map[max_key])

main()