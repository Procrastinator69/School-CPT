#     ﻿# The script of the game goes in this file.
#
# # Declare characters used by this game. The color argument colorizes the
# # name of the character.
#
# define e = Character("Eileen")
#
#
# # The game starts here.
#
# label start:
#
#     # Show a background. This uses a placeholder by default, but you can
#     # add a file (named either "bg room.png" or "bg room.jpg") to the
#     # images directory to show it.
#
#     scene bg room
#
#     # This shows a character sprite. A placeholder is used, but you can
#     # replace it by adding a file named "eileen happy.png" to the images
#     # directory.
#
#     show eileen happy
#
#     # These display lines of dialogue.
#
#     e "You've created a new Ren'Py game."
#
#     e "Once you add a story, pictures, and music, you can release it to the world!"
#
#     # This ends the game.
#
#     return

# define j = Character("Jim", color="#0000ff") # nickname Jim as J; put colour = *insert html colour code*
#
# label start:    # by default, renpy jumps to start
#     # scene       # completely replaces everything you see
#     # or use # show        # creates new layer and puts it on top (must use transparent picture)
#     scene lelouch   # put file name to put the picture in
#     pause         # makes sure that the picture doesn't end immediately after loading
#     show beater # use with dissolve to fade in or out     # show puts image on top
#     pause
#     scene disappointed # with fade # add with fade to cause the image to fade in or out
#     "Hello test 1" # use to make the program say this, not anyone in particular
#     j "Hello my name is Jim"
#     pause
#     $ y = renpy.input("Please enter a name")    # if the user wants to choose their own name
#     if y == "":
#         "Please enter a name."
#     y "Hi my name is [y]"   # square brackets to put name
#     menu:       # use to create options
#         "buy the apple":    # choice 1
#             $ choice1 = "1"
#             "you selected option 1"
#             jump option1
#         "Steal the apple":  # choice 2
#             $ choice1 = "2"
#             "you selected option 2"
#             jump option2
#
#     # use renpy.randomchoice() for random
# label option1:
#     "You just selected option1."
#     jump after_choices         # use to jump after the choices to avoid bugs
# label option2:
#     "You just selected option2."
#     jump after_choices
# label after_choices:
#     if choice1 == "1":
#         "you are a good person"
#     if choice1 == "2":
#         "you are a bloody thief mate"
#     $ strength = 0
#     menu:
#         "go to the gym":
#             $ strength += 1
#         "stay at home":
#             "you are lazy"
#     "day 2"
#     menu:
#         "go to the gym":
#             $ strength += 1
#         "stay at home":
#             "you are lazy"
#
#     if strength == 1:
#         "not too shabby, but you've got a long way to go."
#     if strength > 1:
#         "you are ripped"
#
# return

# example 2:
# $ narrator("Which direction would you like to go?", interact=False)
# $ result = renpy.display_menu([ ("East", "east"), ("West", "west") ])

# Name: Astin Wong
# Last Modified: November 9, 2020
# Description: Make a visual novel game, where the player is presented with choices.

# creating nicknames to refer to

define j = Character("Joe")
define J = Character("Jean")
define B = Character("Bobby")
define N = Character("Narrator")
define S = Character("Supervision Teacher")
define T= Character("Teacher")
define jeanFriend = Character("Jessica")

init python:
    healthBar = 100

label start:

    while healthBar == 100:
        $ load = 5

        while load >= 0:

            "loading in [load] seconds."

            $ load -= 1

        "Success!"

        j "Hello traveler"
        $ n = renpy.input("What is your name? ")
        while n=="":
            "What is your name?"
            $ n = renpy.input("What is your name? ")
        while n == "Joe":
            "Please pick a different name. "
            $ n = renpy.input("What is your name? ")
        while n == "Bobby":
            "Please pick a different name. "
            $ n = renpy.input("What is your name? ")
        while n == "Narrator":
            "Please pick a different name. "
            $ n = renpy.input("What is your name? ")
        while n == "[T]":
            "Please pick a different name. "
            $ n = renpy.input("What is your name? ")

        scene beater at topleft with fade
        pause

        j "Hello [n], my name is Joe, and I will be teaching you the basics of this game."
        j "This is a game of survival."
        j "Every choice you make can affect the lifespan of your character. "
        j "The goal of this game is to survive a day at school without getting covid-19. "
        j "Oh my, look at the time. Ah sorry, I must be heading off now. You best hurry as well. "
        show bg_1012 at truecenter with dissolve
        pause

        j "In order to play this game, you will have to make decisions which can change your character’s life, quite literally. "
        j "Just click on the text box to go to the next line of text. "
        j "To pick choices, click one of the options in the boxes. "
        j "The words in the parenthesis are the thoughts of the character. "
        j "Do your best, for your sake and mine. "


        scene bg_029 with vpunch
        pause
        show basketball
        pause

        "Beep Beep! "
        "You arise, deafened from the racket of the alarm clock. "
        "After getting up, you quickly get dressed and prepare for another rough school day. "

        # use global to globalize function
        # def

        scene beater at left
        pause

        "As you step outside, you are greeted by the chilly autumn breeze. "
        "You quickly double back and don your jacket before beginning your morning walk to school."


        show lmao mr joaquim at right
        pause

        "After arriving at school, a wave of sleepiness overwhelms you. "
        "You try to shake it off like nothing, but you keep feeling more and more exhausted. "
        "You’re beginning to regret staying up to play games last night, and begin to have thoughts about skipping class. "
        "Suddenly, you receive a message from your friend Bobby, who wants you to skip class with him. "
        "With a dilemma on your hands, what will you pick? "
        menu:   # use to create options
            "skip class":
                jump skipMorningClass

            "go to class":
                jump morningClass


        label skipMorningClass:
            menu:
                "meet with Bobby":
                    "covid time"
                    jump covidTime

                "go to roof":
                    "You head to the roof and look around outside. "
                    "You begin to feel bored. "
                    menu:
                        "Go back to class ":
                            T "Where tf were you maggot? "
                            jump morningClass
                        "Go to sleep ":
                            "You drown into a deep slumber, and are awakened by the sound of the lunch bell chiming. "
                            "You rub the sleep out of your eyes, and start heading to lunch. "
                            jump bellRing


        label morningClass:
            "You go to class, and start to feel tired."
            "You try to fight it several times, but fatigue gets the better of you."
            "You decide to take a nap."
            $ randomChoice1 = renpy.random.randint(1,2)
            if randomChoice1 == 1:
                "The teacher catches you slacking, and doesn't hesitate to send you to detention. "
                jump detention1
            elif randomChoice1 == 2:
                "Yawning, you rub your eyes to freshen up."
                jump sleep1

        label detention1:

            "You are quite surprised, as you spot your best friend Bobby in the detention room and sit at the seat closest to him. "
            "You are quite concerned about getting in trouble once more, as you are already in detention and don't want to risk talking to Bobby. "
            "Out of nowhere, another wave of exhaustion hits you."
            "You feel the urge to take yet another nap."

            menu:
                "Start talking to your friend Bobby.":
                    "After you tell him a joke, he starts laughing too much."
                    "This leads to a cough."
                    "Which then leads to a sneeze in your face. "
                    jump covidTime

                "Act out of character and actually study for once":
                    "Since you are already in trouble, you decide to study instead of talking to Bobby."
                    "After a few excruciating hours, the bell finally chimes for lunch time."
                    jump bellRing

                "You find yourself drifting back to sleep once again.":
                    "You wake up with a throbbing head, as a loud noise makes you flinch."
                    "You see the supervision teacher with a furious look on his face, paired with a metre stick in each hand. "
                    S "ARE YOU STILL GOING TO SLEEP MR [n] ? "
                    S "OR DO I NEED TO WAKE YOU UP AGAIN ? "

                    menu:
                        "Yes I will sleep again. ":
                            S "If a death wish is your desire, I shall grant it to you. "
                            "He slaps you several with the pair of rulers in his hands. "
                            S "I'll be keeping an eye on you. (slaps ruler on desk) "
                            S "I better not see you slacking again. "
                            "Suddenly, the teacher sneezes in your face "
                            "ACHOOOO!"
                            "You begin to have some trouble breathing. "
                            "After a few minutes, your forehead feels like it's blazing, and you begin to sneeze constantly. "
                            jump covidTime
                        "No sir, there won't be a next time. ":
                            S "I'll be keeping an eye on you. "
                            S "I better not see you slacking again. "
                            "Suddenly, the teacher sneezes in your face "
                            "ACHOOOO! "
                            "You begin to have some trouble breathing. "
                            "After a few minutes, your forehead feels like it's blazing, and you begin to sneeze constantly. "
                            jump covidTime

        label sleep1:
            $ randomChoice2 = renpy.random.randint(1,2)
            if randomChoice2 == 1:
                "As luck would have it, it was a study period."
                "You didn't miss anything important at all."
                "You glance at the ancient analog clock on the wall right as the bell rings to signal for lunch time. "
            if randomChoice2 == 2:
                "As you groggily wake up, you rub your eyes in disbelief. "
                "Everyone has already left and you have been left behind in the classroom. "
                "You spot writing on the whiteboard, and it says 'UNIT test tomorrow! Make sure to review the important material today!' "
                n "(Oh boy, I shouldn't have went to sleep during class.) "
                "You have nobody to ask for the day's material, as your only and also best friend Bobby skipped the entire class. "
                n "(I'll worry later)"
                n "(Let's just go for lunch in the meantime.) "

        label bellRing:
            scene bg_5161 with vpunch
            "You are heading to lunch when you see the popular kid named Jean that is always surrounded by others. She catches you staring, and smiles at you. "
            "Suddenly, you see your best friend gesturing at you to eat lunch with him in the corner of your eye. "
            "However, you haven’t forgotten about the covid-19 epidemic that is going around and you also want to eat alone to lower the risk of contracting the virus."

            menu:
                "Make a move towards Jean ":
                    jump popularKid
                "Eat with your best friend #brosforlife #premarital handholding is a sin ":
                    jump bestBros
                "Eat alone to avoid covid. I don't need friends to pass the time. ":
                    jump lonerTime


        label popularKid:
            scene
            "You spot Jean talking with her best friend Jessica and you approach her nervously. "
            "You approach Jean nervously. "

            menu:
                "Do you muster up all your courage and ask her to bave lunch together? ":
                    $ randomChoice3 = renpy.random.randint(1,2)
                    if randomChoice3 == 1:
                        n "Jean, d-do you want to have lunch with me? "
                        J "M-M-Me?? "
                        n "Yeah, would that be ok by you? "
                        jeanFriend "Yes of course, Jean would be happy to. "
                        J "Who died and made you boss, Jessica?"
                        J "Who said I wanted to have lunch with him anyways? "
                        n "Wow, thanks a lot. "
                        n "I can leave if you want. "
                        J "Sorry, I didn't mean it that way. "
                        J "I'd be happy to have lunch with you if that's ok with you. "
                        n "Shall we go to the cafeteria then? "
                        J "But of course, [n]. "
                        jump lunchPopularKid


                    if randomChoice 3 == 2:
                        n "Hi Jean, do you want to have lunch together? "
                        "or so you try to say. "
                        n "In reality, your voice cracked while trying to talk. "
                        J "(visible confusion is eteched on her face) "
                        "Awkward silence follows and you make your runaway quickly. "
                        n "(Why did I voice crack? Damn it!) "
                        menu:
                            "Do you want to eat lunch with your best friend instead? ":
                                jump bestBros
                            "Do you want to eat lunch with just yourself? ":
                                jump lonerTime

                "Do you chicken out and decide to just enjoy a normal lunchtime? ":
                    jump bestBros
                "Do you decide to just eat alone instead? ":
                    jump lonerTime


        label lunchPopularKid:
            "You talk casually with her for a bit and bring up sports, one of your favourite pastimes. "
            J "What's your favourite sport? "
            menu:
                "basketball ":
                    pass
                "soccer ":
                    pass
            n "My favourite sport would definitely be either basketball or soccer. "
            J "What a coincidence! "
            J "Basketball is my favourite sport! "
            J "MJ is the GOAT. "
            n "Sorry, but Lebron is miles clear of Jordan. "
            J "Let's settle this outside with a basketball game then. "

            menu:
                "Take on her challenge ":
                    jump basketballTime
                "Chicken out like a snivelling coward ":
                    "You take a good look at her fierce face. Intimidated, you try to run away from her. "
                    n "Uhhhh sorry, I have something urgent to do right now. "
                    n "I've got to go sorry. "
                    $ randomChoice4 = renpy.random.randint(1,2)
                    if randomChoice4 == 1:
                        J "What a coward, chickening out of my challenge. "
                        n "I told you, I have something to do! "
                        "You quickly scramble away and find your best friend Bobby. "
                        B "What took you so long [n]? "
                        n "Sorry, I was in the toilet before. "
                        jump bestBros
                    if randomChoice4 == 2:
                        J "Wait JUST A MINUTE [n]! "
                        "Then, she drags you to the basketball court. "
                        J "I won't let you run away. "
                        J "Now, it's time for your punishment. "
                        jump basketballTime

        label basketballTime:
            "Suddenly, you receive a text from your friend Bobby who wants you to play basketball with him. You invite her to play a game of bump with the three of you. "
            scene BG029
            show basketball
            pause
            "HI"
        label bestBros:
            "You decide to have lunch with your best friend Bobby. "
            jump covidTime

        label lonerTime:
            n "I'll have lunch with me, myself, and I. "
            jump covidTime


        label covidTime:
            "You got COVID! "
            "YOU LOSE! xD "
            return







    # loop for basketball scene
# init python:
#     def WeightedChoice(choices):
#         """
#         @param choices: A list of (choice, weight) tuples. Returns a random
#         choice (using renpy.random as the random number generator)
#         """
#         totalweight = 0.0
#         for choice, weight in choices:
#             totalweight += weight
#         randval = renpy.random.random() * totalweight
#         for choice, weight in choices:
#             if randval <= weight:
#                 return choice
#             else:
#                 randval -= weight
#
# label start:
#     $rand_choice = WeightedChoice([("Route_A", 0.50),
#                                    ("Route_B", 0.35),
#                                    ("Route_C", 0.10),
#                                    ("Route_D", 0.05)])
#     jump expression rand_choice
#     return
#
# label Route_A:
#     "This is Route A"
#     return
#
# label Route_B:
#     "This is Route B"
#     return
#
# label Route_C:
#     "This is Route C"
#     return
#
# label Route_D:
#     "This is Route D"
#     return
