unique_permutations = set()
def permutations_make(word, cur_word=""):
    global permutations
    if word == "":
        return unique_permutations.add(cur_word)
    for i in range(len(word)):
        permutations_make(word[:i] + word[i+1:], cur_word + word[i])

my_word = "aeofloe"
permutations_make(my_word)
sorted_permutations = sorted(list(unique_permutations))
my_word_index = sorted_permutations.index(my_word)
print(sorted_permutations[my_word_index + 1])    