boat_side = 'Right'
missionary_on_right = 3
cannibals_on_right = 3
missionary_on_left = 0
cannibals_on_left = 0


def display_screen():
  print('M =',missionary_on_left, end=" ")
  print('C =',cannibals_on_left, end=" ")

  if boat_side == 'Right':
    print('|-----B|', end=" ")
  if boat_side == 'Left':
    print('|B-----|', end=" ")



  print('M =',missionary_on_right, end=" ")
  print('C =',cannibals_on_right, end=" ")
display_screen()


while True:
    missionary = int(input("Enter number of Missionary in boat on "+ boat_side + ":"))
    cannibals = int(input("Enter number of Cannibals in boat on " + boat_side + ":"))


    if (missionary+cannibals) != 1 and (missionary+cannibals) != 2:
        print("Invalid move")
        continue


    if boat_side == "Right":
        if missionary > missionary_on_right or cannibals > cannibals_on_right:
            print("Invalid move")
            continue

        missionary_on_right -= missionary
        cannibals_on_right -= cannibals
        missionary_on_left += missionary
        cannibals_on_left += cannibals


        boat_side = "Left"
        display_screen()

    else:
        if missionary > missionary_on_left or cannibals > cannibals_on_left:
            print("Invalid move")
            continue

        missionary_on_right += missionary
        cannibals_on_right += cannibals
        missionary_on_left -= missionary
        cannibals_on_left -= cannibals

        boat_side = "Right"
        display_screen()

    if (missionary_on_right != 0 and missionary_on_right < cannibals_on_right) or (missionary_on_left != 0 and missionary_on_left < cannibals_on_left):
        print("\n ===YOU LOSE===")
        break

    if missionary_on_left == 3 and cannibals_on_left == 3:
        print("YOU WIN")
        print("Thank You for playing!")
        print("Made with" + "\u2764\ufe0f" + " "+" by Shubham")
        break
    

print("====Game Over!====")
