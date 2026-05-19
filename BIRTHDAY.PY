import time
def print_birthday_message(HARSHI):
    cake = r"""
       ,   ,   ,   ,
     , |_,_|_,_|_,_| ,
    |\/_  HAPPY   _\/|
    |/\ BIRTHDAY /\|
    |/  \_______/  \|
    |      | |      |
    |     *****     |
    '.___\___/___/.'
    """

    message = f"\n🎉🎂 Happy Birthday, {HARSHI}! 🎂🎉\n"
    
    print(cake)
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print("\nWishing you a fantastic year ahead!\n")