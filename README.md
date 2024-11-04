# npc-project
## What is the *npc-project?*
This NPC project is fairly simple code that heavily relies on the random library to function properly.

This generator will make 10 NPCs that have the following criteria:

- [Age](#Age-explained)
- [Height](#Height-explained)
- [Gender](#Gender-explained)
- [Race](#Race-explained)
- [First and Last name](#First-and-Last-name-explained)
  
## Age explained
For the code that generates the age of each NPC, I had the user input two numbers, one being the lesser number of an age range and the other being a higher number of the age range as seen below:


`age_range_L = int(input("Enter lesser number for NPC age range: "))`

`age_range_H = int(input("Enter higher number for NPC age range: "))`

Afterwards, I used the random library to pick a number between that range:

`rando_age = random.randint(age_range_L , age_range_H + 1)`

## Height explained
For the code that generates the height of each NPC, I also had the user input two numbers to get a range. 

I did this Like I did for the age above, code is essentially the same as it was.

## Gender explained
For the code that generates the gender of each NPC, I had the random library choose the value 0 (male) or 1 (female) as seen below:

`gender = random.randint(0, 1)`

This variable will play a much bigger part to deciding the first names of the NPCs later in the code.

## Race explained
For the code that generates the race of each NPC, I had the random library choose a range between 0 and 2, as seen below:

`race = random.randint(0, 2)`

0 = White, 1 = Black, and 2 = Asian

## First name and Last name explained
For the code that generates the First name of Each NPC, I made two different lists for male and female names, with each having three variations based on what race was chosen



