vote = input("enter your age :")
if int(vote)>=18:
    print("you are eligible to vote")
elif int(vote)<14:
    print("you are minor to vote")
else :
    print("you are not eligible to vote")