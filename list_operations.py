my_list = []
user_wants = True

while user_wants:
    print("Currently we have %d items in our list" % len(my_list))
    print("Here they are:")
    print(my_list)
    print()

    print("""Please choose the desired action:
    'A' - To add item to list
    'D' - To delete item from list
    'R' - To replace item in list
    'Q' - To quit the program and destroy the list""")
    user_decision = input("What do you want to do? ==> ").lower()

    if user_decision == 'a':
        item_to_add = input("Please type the item you want to add: ")
        my_list.append(item_to_add)
    elif user_decision == 'd':
        item_to_remove = input("Please type the item you want to remove: ")
        my_list.remove(item_to_remove)
    elif  user_decision == 'r':
        item_index_to_replace = int(input("Please type the index of item you want to replace: "))
        item_to_insert = input("Please type the item you want to replace: ")
        my_list.pop(item_index_to_replace)
        my_list.insert(item_index_to_replace, item_to_insert)
    elif user_decision == 'q':
        user_wants = False
    else:
        print("You've entered incorrect action")

