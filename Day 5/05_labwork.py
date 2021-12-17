#
word = input("input reverse word\n")
for char in range(len(word) -1, -1, -1):
    print(word[char], end="")
    print("\n")
