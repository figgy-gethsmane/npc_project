import random
import time

# allows user to input a range of height and age using 4 different input statements
age_range_L = int(input("Enter lesser number for NPC age range: "))
age_range_H = int(input("Enter higher number for NPC age range: "))
height_range_L = float(input("Enter lesser height(in feet) for NPC height range: "))
height_range_H = float(input("Enter higher height(in feet) for NPC height range: "))

npc_generated = 0

# Using the npc_generated variable, I can loop all the code 10 times, with each time adding a value of one to the variable
while npc_generated < 10:
    npc_generated += 1
    rando_age = random.randint(age_range_L , age_range_H + 1)

    rando_height = random.uniform(height_range_L , height_range_H)

    race = random.randint(0, 2)

    gender = random.randint(0, 1)
    
    # This major part of my code decides the name of the NPC, race and gender, all building off one another.
    # For gender I decided to make 0 = male and 1 = female and for race 0 = white, 1 = black and 2 = asian
    # Based on whatever integer the random library chooses, it will choose one name out of one of the three different variations of name_list_M, according to each race
    # Or one name out of one of the three different variations of name_list_F, also according to each of the races.
    if gender == 0:
        gender = "Male"
        if race == 0:
            race = "White"
            name_list_M = [ "Noah" , "Liam ", "Jacob", "Mason", "William", "Ethan", "Michael", "Alexander", "Jayden" ,
                        "Daniel", "Elijah", "Aiden", "James", "Benjamin", "Matthew", "Jackson", "Logan", "David", "Anthony", "Joseph", "Joshua", 
                        "Andrew", "Lucas", "Gabriel", "Samuel", "Christopher", "John", "Dylan", "Isaac", "Ryan"
                        ]
        elif race == 1:
            race = "Black"
            name_list_M = ["Deion", "Deiondre", "Dele", "Denzel", "Dewayne", "Dikembe", "Duante", "Jamar", "Jevonte", 
                        "Elijah", "Isaiah", "Booker", "Caleb", "Jabari", "Ahmod", "Amare", "Asaad", "Autry", "Calvin", "Hakeem",
                        "Michael", "Aaron", "Aiyden", "Amir", "Cory", "Dajon", "Ekon", "Ericson", "Grady", "Jeremiah", "LeBron"
                        ]
        else:
            race = "Asian"
            name_list_M = ["Jin", "Chang", "Dae", "Aiguo", "Aki", "Carlos", "Chan", "Ming", "Cho", "Dewei", "Fai", "Feng", "Gary", 
                        "Guozhi", "Hai", "Haider", "Han", "Harold", "Hiromi", "Ichiro", "Isamu", "Jackie"
                        ]
        rando_name_M = random.choice(name_list_M)
        uniname = rando_name_M


    if gender == 1:
        gender = "Female"
        if race == 0:
            race = "White"
            name_list_F = ["Jennifer", "Jessica", "Ashley", "Sarah", "Amanda", "Emily", "Elizabeth", "Stephanie", "Nicole", "Michelle", "Samantha", 
                            "Kimberly", "Amy", "Heather", "Rachel", "Rebecca", "Lauren", "Angel", "Megan", "Hannah", "Christina", "Lisa", "Amber", "Mary", 
                            "Brittany", "Emma", "Laura", "Danielle", "Madison"
                            ]
        elif race == 1:
                race = "Black"
                name_list_F = ["Jasmine", "Zuri", "Aaliyah", "Nevaeh", "Abeba", "Ada", "Adamma", "Aiysha", "Alexis", "Amara", "Asha", "Ayana", "Chloé", "Destiny",
                            "Halle", "Jordan", "Laila", "Makayla", "Malaika", "Taylor", "Tiana", "Valeria"
                            ]
        else: 
            race = "Asian"
            name_list_F = ["Daiyu", "Emi", "Aika", "Akira", "Hana", "Mai", "Mira", "Ngaio", "Adeline", "Amida", "Amy", "Bo", "Cheng", "Chika", 
                        "Chivy", "Dara", "Lanfen", "Nguyen"
                        ]
        rando_name_F = random.choice(name_list_F)
        uniname = rando_name_F
    
    # This list and the random command after decide the last names of all 10 NPCS
    last_name_list = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
                        "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
                        "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green", "Adams","Nelson", "Baker", "Hall", "Rivera", 
                        "Campbell", "Mitchell", "Carter", "Roberts", "Gomez"
                        ]
    rando_last_name = random.choice(last_name_list)

    # Prints all NPC information out in a readable manner, f command allows me to insert what one of my variables equals to inside a string
    # \n puts string a new line and ":.2f" limits a floats decimal values to just 2 values
    print(f"\nNPC {npc_generated}"
           "\nFull name:", uniname, rando_last_name,
           "\nRace:", race,
           "\nGender:", gender,
           "\nAge:", rando_age,
           f"\nHeight: {rando_height:.2f} ft"
           )
    time.sleep(3)
