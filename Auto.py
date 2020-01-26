import random
import time
def check(choose,drinks,M,drinksName):
  if choose in drinks.keys():
      total = drinks[choose]
      print(drinksName[int(choose)-1]+"を選びました、"+str(total)+"円です！")
      koka = 0
      while True:
        money=input("コインを選びください：")
        if money in M:
          koka=koka+int(money)
          if koka==total:
            print("ちょうどいいです！ご利用いただきありがとうございます。")
            time.sleep(1.2)
            Seven()
            break
          elif koka < total:
            print("{}円です。{}円預かりいたしました、{}円足りません。".format(total,koka,total-koka))
          else:
            print("{}円です。{}円預かりいたしました、{}円のお釣りです。ご利用いただきありがとうございます。".format(total,koka,koka-total))
            time.sleep(1.2)
            Seven()
            break
        else:
          print("この硬貨または紙幣がありますか？お金をいれてください。")
  elif choose.lower()=="q":
      print("quit")
  else:
      print("error")
def JdohanB():
  drinks = {"1":150,"2":180,"3":100,"4":130}
  M = ["10","50","100","500","1000"]
  drinksName = ["オレンジ","ココナッツ","コーラ","コーヒー"]
  while True:
    choose = input("飲み物を選択してください:\n"
    "1:オレンジ(150円) \n"
    "2:ココナッツ(180円)\n"
    "3:コーラ(100円)\n"
    "4:コーヒー(130円)\n"
    "Q:quit\n")
    check(choose,drinks,M,drinksName)

def Seven():
    num1=random.randint(0,9)##本当の確率
    num2=random.randint(0,8)##表示する数字
    print("今から抽選します。")
    time.sleep(0.5)
    if num1==0:               ##もし乱数は0の時      
        for i in range(3):
            print(num2,end=" ")
            time.sleep(0.8)
        time.sleep(0.8)
        print(num2)
        time.sleep(0.8)
        print("当たりました！おめでとう！もう一本出します")
        time.sleep(0.8)
    else:
        for i in range(3):
            print(num2,end=" ")
            time.sleep(0.8)
        time.sleep(0.8)
        print(num2+1)
        time.sleep(0.8)
        print("外れてしまいました！残念！")
        time.sleep(0.8)
JdohanB()

