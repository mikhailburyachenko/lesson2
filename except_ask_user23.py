dict1={"Как дела?": "Хорошо", "Что делаешь?": "Программирую", "Что делать?": "Ботай питон!"}
k = 0
def ask_user():

    while True:


        print ("Введи вопрос. Для выхода введи Пока")
        q=input()
        if q=="Пока":
            break
        for i in dict1:
            if i==q:
                global k
                k = k+1
                print (dict1[i])
                
        if k==0:
            print ("Я не знаю")

        

try:
    ask_user()
except KeyboardInterrupt:
    print("Ладно пока")