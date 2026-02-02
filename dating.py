


Ralationship = 0
Day = 0
Money = 0
Food = 5
Demon_Hunger = 3
Demon_mood = 0


def daily_morning ():

    global Day
    global Food
    global Demon_Hunger
    global Demon_mood
    global Money

    chapter_early = (f"วันนี้คือวันที่ {Day} ตอนเช้า...คุณจะเลือกทําอะไร \n  1)ไปทํางาน \n 2)ให้อาหาร {Demon} \n 3)พา {Demon} ไปเที่ยวสวนสาธารณะ \n 4)อาบนํ้าให้ {Demon}")
    print(chapter_early)
    answer = int(input("คุณเลือกที่จะ : "))

    if(answer == 1):
        print(f"{Demon}: โชคดีนะคะนายท่าน\n")
        Demon_Hunger -= 1
        Demon_mood -= 1
        Money += 100
        Food += 0

        print(f"ค่าความสุข {Demon} -1 ")
        print(f"ค่าอาหาร {Demon} -1 ")
        print(f"เงิน +100 \n")

        print(f"ค่าอาหาร {Demon} เหลือ",Demon_Hunger)
        print(f"ค่าความสุข {Demon} เหลือ",Demon_mood)
        print(f"คุณมีเงิน {Money}")
        print(f"อาหารเหลือ {Food}\n")

    elif(answer == 2):
        print(f"{Demon}: อาหารอร่อยมากคะนายท่าน {User}")
        print(f"{Demon}: ฉันจะรอนายท่านอยู่ที่บ้านนะคะ โชคดีนะคะ\n")

        Demon_Hunger +=1
        Demon_mood +=1
        Money +=100
        Food -=1

        print(f"ค่าความสุข {Demon} +1")
        print(f"ค่าความอาหาร {Demon} +1")
        print(f"เงิน +100")
        print(f"อาหาร -1\n")

        print(f"ค่าอาหาร {Demon} เหลือ",Demon_Hunger)
        print(f"ค่าความสุข {Demon} เหลือ",Demon_mood)
        print(f"คุณมีเงิน {Money}")
        print(f"อาหารเหลือ {Food}\n")

    elif(answer == 3):
        print(f"{Demon}: ขอบคุณที่พาฉันไปเที่ยวนะคะ นายท่าน {User}\n")
        
        Demon_Hunger -=1
        Demon_mood +=2
        Money +=0
        Food += 0

        print(f"ค่าความสุข {Demon} +2")
        print(f"ค่าความอาหาร {Demon} -1\n")
    
        print(f"ค่าอาหาร {Demon} เหลือ",Demon_Hunger)
        print(f"ค่าความสุข {Demon} เหลือ",Demon_mood)
        print(f"คุณมีเงิน {Money}")
        
        print(f"อาหารเหลือ {Food}\n")
        
    elif(answer == 4):
        print(f"{Demon}: นายท่านดูเเลฉันดีจังเลย //^_^// \n")
        
        Demon_Hunger -=0
        Demon_mood +=1
        Money +=50
        Food += 0

        print(f"ค่าความสุข {Demon} +1")
        print(f"เงิน +50\n")
        
        print(f"ค่าอาหาร {Demon} เหลือ",Demon_Hunger)
        print(f"ค่าความสุข {Demon} เหลือ",Demon_mood)
        print(f"คุณมีเงิน {Money}")
        print(f"อาหารเหลือ {Food}\n")
    print("end of day--------------------------\n")



print("คุณบังเอิญได้เจอกับลูกปีศาจสาวตนนึง...คุณตัดสินใจที่จะรับเลี้ยงเธอ \n ลูกปีศาจสาว: นายท่านจะรับเลี้ยงฉันงั้นเหรอค่ะ...ได้โปรดมอบชื่อให้ดิฉันด้วยคะ(สายตาอ้อนวอน)")
Demon = input("กรุณาป้อนชื่อปีศาจของคุณ : ")
print(f"ลูกปีศาจสาว: ท่านตั้งชื่อให้ข้าว่า {Demon} งั้นเหรอคะ ช่างไพเราะสะจริง...ขอบคุณมากนะคะ //^_^// \n {Demon}: ว่าเเต่นายท่านชื่ออะไรเหรอคะ?")
User = input("กรุณากรอกชื่อของคุณ : ")
print(f"{Demon}: นายท่าน {User} สินะคะ...ฝากตัวด้วยนะคะ")
while Day <= 10000000000 :
    daily_morning()
    Day += 1




    

