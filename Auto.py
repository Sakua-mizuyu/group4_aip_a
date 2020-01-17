def JdohanB():
  drinks = {"1":150,"2":180,"3":100,"4":130}
  M = ["10","50","100","500","1000"]
  total = 0
  koka = 0
  while True:
    choose = input("飲み物を選択してください:\n"
    "1:オレンジ(150円) \n"
    "2:ココナッツ(180円)\n"
    "3:コーラ(100円)\n"
    "4:コーヒー(130円)\n"
    "Q:quit\n")
    if choose in drinks.keys():
      total=total+drinks[choose]
      while True:
        money=input("コインを選びください：")
        if money in M:
          koka=koka+int(money)
          if koka==total:
            print("ちょうどいい")
            break
          elif koka < total:
            print("{}円です。{}円預かりいたしました、{}円足りません。".format(total,koka,total-koka))
          else:
            print("{}円です。{}円預かりいたしました、{}円のお釣りです。".format(total,koka,koka-total))
            break
        else:
          print("お金をいれてください。")
    elif choose=="Q":
        print("quit")
        break
    else:
        print("error")
JdohanB()
