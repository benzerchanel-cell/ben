import random



Ralationship = 0
Day = 0
Money = 100
Food = 5
Demon_Hunger = 3
Demon_mood = 0

def main_status():
    
    print(f"ค่าความสุข {Demon} -1 ")
    print(f"ค่าอาหาร {Demon} -1 ")
    print(f"เงิน +100 \n")

    print(f"ค่าอาหาร {Demon} เหลือ",Demon_Hunger)
    print(f"ค่าความสุข {Demon} เหลือ",Demon_mood)
    print(f"คุณมีเงิน {Money}")
    print(f"อาหารเหลือ {Food}\n")

    print("คุณได้ทํางานเสร็จเรียบร้อยเเล้ว...คุณจะเลือกทําอะไรต่อ \n  1)ไปช๊อปปิ้ง \n 2)กลับบ้าน")

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

        
        main_status()
        
        answer = int(input("คุณเลือกที่จะ : "))

        if(answer == 1):
            item_shop = ["โทรศัพท์ ราคา 1000","หนังสือการ์ตูน ราคา 200","เสื้อผ้าผู้หญิง ราคา 500","ตุ๊กตา ราคา 200"]
            item_price = [1000, 200 , 500 , 200]
            item_random = random.randrange(0, 3)
            daily_item = item_shop[item_random]
            #daily_item = random.choice(item_shop)

            print(f"ร้านค้าของคุณมี \n 1){daily_item} เเละ 2) อาหาร ราคา 20   3)กลับบ้าน  คุณจะเลือกอะไรบ้าง " )
            answer = int(input("คุณเลือกที่จะ : "))
            if(answer == 1):
                if Money < item_price[item_random]:
                    print("คุณมีเงินไม่พอ")
                else:
                    print("ขอบคุณที่อุดหนุน")
                    Money -= item_price[item_random]
                    print(f"คุณเหลือเงิน {Money} บาท")
            elif(answer == 2): 
                Food_price = int(input("คุณต้องการซือกี่ชิ้น"))
                foodprice = Food_price * 20
                if Money < foodprice:
                    print("คุณมีเงินไม่พอ")
                else:
                    print("ขอบคุณที่อุดหนุน")
                    Money -= foodprice
                    print(f"คุณเหลือเงิน {Money} บาท")
            elif(answer == 3):
                print(f"คุณได้กลับบ้านมาเจอ {Demon}")
        
        elif(answer == 2):
            print(f"คุณได้กลับบ้านมาเจอ {Demon}")

    

    
    

                 
                 


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




    

