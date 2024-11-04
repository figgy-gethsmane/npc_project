# npc-project
## What is the *npc-project?*
This NPC project is fairly simple code that heavily relies on the random library to function properly.

This generator will make 10 NPCs that have the following criteria:

- [Age](#Age-explained)
- Height
- Gender
- Race
- First and Last name
  
## Age explained
For the code that generates the age of each NPC, I had the user input two two numbers, one being the lesser number of an age range and the other being a higher number of the age range as seen below:


`age_range_L = int(input("Enter lesser number for NPC age range: "))`

`age_range_H = int(input("Enter higher number for NPC age range: "))`

Afterwards, I used the rnaodm library to pick a number between that range:

`rando_age = random.randint(age_range_L , age_range_H + 1)`



