#Word puzzle
import time
import threading
import random
import sys


def game():
    print("  " * 8, end=" ")
    print("WELCOME", end=" ")
    time.sleep(1)
    print("TO THE GAME OF", end=" ")
    time.sleep(1)
    print("WORD PUZZLE")
    time.sleep(2)
    print("\n" * 2)
    print("Kindly set the level of game", end=" ")
    time.sleep(1)
    print("(Enter 1,2 or 3", end=" ")
    time.sleep(1)
    print("to set the level as", end=" ")
    select = int(input("easy,medium,difficult level respectively):\n"))
    time.sleep(2)
    print("\n" * 2)
    print("Lets get started with LEVEL-", select, "\n")
    time.sleep(2)
    print("You will be given five jumbled words", end=" ")
    time.sleep(2)
    print("and you are supposed to give", end=" ")
    time.sleep(2)
    print("the meaningful word for each of them.\n")
    time.sleep(3)
    word_list = []
    word_list1 = [('napl', 'plan'), ('kobo', 'book'), ('kreab', 'break'), ('hclun', 'lunch'), ('pish', 'ship'),
                  ('mudr', 'drum'), ('rouh', 'hour'), ('idam', 'amid'), ('hurs', 'rush'), ('reptyt', 'pretty'),
                  ('tesb', 'best'), ('ezacr', 'craze'), ('salcs', 'class'), ('morw', 'worm'), ('resds', 'dress'),
                  ('iarh', 'hair'), ('etim', 'time'), ('lwid', 'wild'), ('rewot', 'tower'), ('morst', 'storm'),
                  ('macl', 'calm'), ('kcalb', 'black'), ('shflu', 'flush'), ('teart', 'treat'), ('kicrt', 'trick'),
                  ('doclu', 'cloud'), ('ribd', 'bird'), ('dolob', 'blood'), ('hpypa', 'happy'), ('ytrpa', 'party')]
    word_list2 = [('efeerug', 'refugee'), ('eapsce', 'escape'), ('dreab', 'bread'), ('arodkbblac', 'blackboard'),
                  ('rentruc', 'current'), ('tenscon', 'consent'), ('itqulay', 'quality'), ('cucapke', 'cupcake'),
                  ('reroust', 'trouser'), ('moconm', 'common'), ('regstnar', 'stranger'), ('yapogol', 'apology'),
                  ('ececffredi', 'difference'), ('raguit', 'guitar'), ('shiofan', 'fashion'), ('gebalar', 'algebra'),
                  ('shaceri', 'cashier'), ('tuditearg', 'gratitude'), ('locochate', 'chocolate'), ('ezbree', 'breeze'),
                  ('nobburst', 'stubborn'), ('figrth', 'fright'), ('yteshon', 'honesty'), ('orberb', 'robber'),
                  ('olrtonc', 'control'), ('iltlet', 'little'), ('utforne', 'fortune'), ('riedp', 'pride'),
                  ('inddewg', 'wedding'), ('igrig', 'rigid')]
    word_list3 = [('anetiottn', 'attention'), ('ymsthapy', 'sympathy'), ('isctasfaiotn', 'satisfaction'),
                  ('tneacihemev', 'achievement'), ('tattnemcha', 'attachment'), ('yuruxl', 'luxury'),
                  ('yagecn', 'agency'), ('missartsnoin', 'transmission'), ('treimgen', 'regiment'),
                  ('talehicts', 'athletics'), ('emmrebishp', 'membership'), ('gagealnu', 'language'),
                  ('errudnti', 'intruder'), ('ummoment', 'momentum'), ('yalstrc', 'crystal'), ('timmnyui', 'immunity'),
                  ('temnettsa', 'statement'), ('rmeeasu', 'measure'), ('deutsoil', 'solitude'),
                  ('alintmer', 'terminal'), ('rempisonis', 'permission'), ('simmitop', 'optimism'),
                  ('telilgceneni', 'intelligence'), ('tinoentde', 'detention'), ('aptietpe', 'appetite'),
                  ('yenttora', 'attorney'), ('chanisdemer', 'merchandise'), ('ntoitoamau', 'automation'),
                  ('cetetmoim', 'committee'), ('osoyphilph', 'philosophy')]

    list2 = []
    if (select == 1):  # list and period selection according to the level chosen
        word_list = word_list1
        period = 30
    elif (select == 2):
        word_list = word_list2
        period = 45
    elif (select == 3):
        word_list = word_list3
        period = 60

    def prompt_with_timeout():
        return

    points = 0
    c = 0
    for i in range(0, 5):

        while (True):
            if (c == 0):  # choosing a unique item every time
                item = random.choice(word_list)
                list2 = list2 + [item]
                c = c + 1
                break
            elif (c != 0):
                item = random.choice(word_list)
                if item not in list2:
                    list2 = list2 + [item]
                    break
                else:
                    continue

        pos = -1
        for j in range(0, len(word_list)):  # finding the position of the item in word_list
            pos = pos + 1
            if (item == word_list[j]):
                break
        t = threading.Timer(period, prompt_with_timeout)
        t.start()
        start_time = time.time()
        print("\n" * 2)
        print("(", (i + 1), ")Jumbled word:", word_list[pos][0])  # displaying the jumbled word
        time.sleep(1)
        print("You have exactly", period, " seconds to answer",
              end="")  # displaying the time period allotted for giving an answer
        answer = input("\n")
        t.cancel()
        end_time = time.time()
        time_elapse = end_time - start_time  # calculating the time taken by the player to answer

        if (time_elapse >= 60):  # no point given if times up
            print("Times up!   ❌")
        else:
            if (answer == word_list[pos][1]):  # 1 point given if the player answered correctly within the given period
                print("Gotcha!    ✔")
                points = points + 1
            else:
                print("Oops!     ❌")  # no point given if answered wrong within the given period

    print("\n" * 2)
    if (points == 5):
        print("Woah!You scored a perfect 5/5!")
    else:
        print("Your score is ", points, "/5")
    print("\n\nDo you want to play again?")  # prompting the player to answer if he wants to play again
    time.sleep(1)
    regame = input(" (Answer in yes or no)\n")
    if (regame == "yes"):
        print("\n" * 10)
        game()
    elif (regame == "no"):
        print("\n" * 2)
        print("\nThankyou for playing")
        time.sleep(2)
        sys.exit()


game()


