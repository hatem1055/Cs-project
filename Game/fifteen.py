def find3Numbers(A, arr_size, sum):
    for i in range(0, arr_size - 2):
        for j in range(i + 1, arr_size - 1):
            for k in range(j + 1, arr_size):
                if A[i] + A[j] + A[k] == sum:
                    
                    return True
    return False
sum1 = 0
sum2 = 0
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list1 = []
list2 = []
for i in range(0,3):
 print("the avialable numbers are:", num)
 while True:
  x1=int(input("player1: "))
  if x1 in num:
      list1.append(x1)
      num.remove(x1)
      length1 = len(list1)
      break
  else:
      print("print please enter another number")
 sum1 += x1
 if sum1 == 15 and length1==3:
     break
 print("the avialable numbers are:",num)
 while True:
  y2=int(input("player2: "))
  if y2 in num:
      list2.append(y2)
      num.remove(y2)
      length2 = len(list2)
      break
  else:
      print(" please enter another number")
 sum2 += y2
 if  sum2 == 15 and length2==3:
     break
if sum1 == 15 :
        print("player1 wins")
elif sum2 == 15:
        print("player2 wins")
else:
     print("draw")