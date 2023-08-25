x = 1
while x <= 5:
    print(x)
    x+= 1

print("finito")

# ////

word = "hooray"
guess_word = ""
number_of_guesses = 0
max_guesses = 4
out_of_guesses = False

while guess_word != word and not(out_of_guesses) :
    if number_of_guesses < max_guesses:
     guess_word = input("what is your guess: ")
     number_of_guesses += 1
    else:
       out_of_guesses = True
if out_of_guesses:
 print("you are out of guesses")
else:
  print("you win")

