
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************''')
print('''------------------------------------------Welcome to Kushagr's  _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 ------------------------------------------\n=> YOUR MISSION IS TO FIND THE TREASURE''')

direct = str(input("Left or Right ?:\t"))

if (direct == 'Left' or direct == 'left'): # Iska elif hoga (right space Right)

    print("Great , now you are at the end of the island and you are facing a vast sea.")

    direct_2 =str(input("Do you want to swim or wait for the boat(Just type 'swim' or 'wait'):\t"))

    if (direct_2 == 'Wait' or direct_2 == 'wait'): # Iska elif hoga (swim space Swim)

        print("boat left you at the other side of the river and there is a castle.")

        doors = str(input("There are 3 doors (chose any one 'yellow' , 'red'  or 'blue') :\t"))

        if (doors == 'yellow' or doors == 'Yellow'):

            print('''      ....
   ,od88888bo.
 ,d88888888888b
,dP""'   `"Y888b       ,.
d'         `"Y88b     .d8b. ,
'            `Y88[  , `Y8P' db
              `88b  Ybo,`',d88)
               ]88[ `Y888888P"
              ,888)  `Y8888P'
             ,d888[    `""'
          .od8888P          ...
     ..od88888888bo,      .d888b
          `""Y888888bo. .d888888b
.             `Y88b"Y88888P"' `Y8b
:.             `Y88[ `"""'     `88[
|b              |88b            Y8b.
`8[             :888[ ,         :88)
 Yb             :888) `b.       d8P'
 `8b.          ,d888[  `Ybo.  .d88[
  Y8b.        .dWARP'   `Y8888888P
  `Y88bo.  .od8888P'      "YWARP'
   `"Y8888888888P"'         `"'
      `"Y8888P""'
         `""'
YAY! you won the treasure!!''')

        elif (doors == 'blue' or doors == 'Blue' or doors ==''):

            print("Game Over!! , as you are attacked by beast.")

        elif (doors == 'red' or doors == 'Red'):

            print('Valley ahead!!')    

        else:

            print('You are out of the game.')

    elif (direct_2 == 'swim' or direct_2 == 'Swim'):

        print("Attacked by trout.")

    else:

        print("You did it dirty.")

elif (direct == 'Right' or direct == 'right' or direct == ''):

    print('Alas,You fell in a pithole.')        