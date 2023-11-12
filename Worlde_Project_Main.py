# Creating list of characters from solution
solution = "angle"
solution_list = []
for i in solution:
  solution_list.append(i)

# Logic to ensure that the selected choice is only 5 letters
choice_one = (input("Wordle selection: "))
while int(len(choice_one)) != 5:
  choice_one = (input("[Only 5 letters long pls] Wordle selection: "))

# Creating list of characters from choice
choice_list = []
for i in choice_one:
  choice_list.append(i)

def matcher_func(char_list, sol_list):
  c_list = char_list
  s_list = sol_list
  for char in range(len(c_list)):
    if c_list[char] == s_list[char]:
      del c_list[char]
      del s_list[char]
      print(f"Position {char + 1}: One of the characters is in the right position: {c_list[char]}")
    elif c_list[char] in s_list:
      print(f"Position {char + 1}: One of the characters is in position {c_list[char]}")
    else:
      print(f"Position {char + 1}: No character match")


matcher_func(choice_list, solution_list)
