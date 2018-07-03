
# coding: utf-8

# In[4]:


def hangman(word):
    wrong = 0
    stages = ["",
             "_______       ",
             "|      |      ",
             "|      |      ",
             "|      @      ",
             "|     /|\     ",
             "|     / \     ",
             "|             "
             ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ようこそ・・・ハングマンの館へ・・・")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "・・・一文字を予想せよ・・・"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("お主の勝ちじゃ・・・チッ、つまらぬ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("貴様の負けじゃ！正解は {} じゃよ.ウヒヒヒヒヒイヒ・・・・".format(word))
        
        
hangman("cat")

