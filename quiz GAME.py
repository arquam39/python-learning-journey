# Prize-winning quiz game

question = [
    ["What is the capital of Canada?","Toronto","Vancouver","Ottawa", "Montreal" , 3 ],
    ["Which data structure follows the Last In, First Out (LIFO) principle?","Stack","Array","Ottawa", "Montreal", 1 ],
    ["What is the chemical symbol for gold?","Br","Au","Mg", "Nal" , 2 ],
    ["Which of the following is a cloud computing service model?","Naas","Saas","Oaas", "Maas" , 2 ],
    ["What is the capital of India?","Toronto","Delhi","Ottawa", "Montreal" , 2 ],
    ["What is the capital of Japan?","Tokyo","Osaka","Kyoto", "Hokkaido" , 1 ],
]

amount = [1000,2000,5000,10000,20000,100000,200000,50000]
money = 0

for i in range (0,len(question)):
    questions = question[i]
    print(questions[0])
    print(f"a.{questions[1]}   b.{questions[2]}   c.{questions[3]}   d.{questions[4]}")
    reply = int(input("Give answer from 1-4: "))
    print()
    if reply != questions[5]:
        print("Wrong asnwer ")
        print(f"You have won an amount of Rs.{money} today")
        break
    else:
        print(f"You have Rs.{amount[i]} at the moment")
        print()
        if i == 2 or i == 5:
            money = amount[i]
        elif i < 2:
            money = 0
        elif i < 5 and i > 2:
            money = 5000
        elif i < 7 and i > 5:
            money = 100000
