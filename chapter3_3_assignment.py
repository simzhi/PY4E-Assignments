score = input("Enter Score: ")
try:
    fscore = float(score)
except:
    print('Error, not a number!')
    quit()
if fscore > 0.0 and fscore < 1.0 :
    if fscore >= 0.9:
        print('A')
    elif fscore >= 0.8:
        print('B')
    elif fscore >= 0.7:
        print('C')
    elif fscore >= 0.6:
        print('D')
    elif fscore < 0.6:
        print('F')
else:
    print('Error, out of range!')
