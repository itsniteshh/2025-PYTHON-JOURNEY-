def how_much_i_love_you(nb_petals):
    # using dict to store answers  
    answers = {
       1: "I love you",
       2:  "a little",
       3:  "a lot",
       4:  "passionately",
       5:  "madly",
       0: "not at all"
    }
    if nb_petals >= 7:
        nb_petals = nb_petals % 6
        
    
    return answers.get(nb_petals)