# 這是練習文件
# string 字串
#helloworld="Hello World" #左邊是變數，第一個字必須要是字母
#hellopython="Hello Python" #右邊是變數值，也是字串
# number 數字
#a=100
#b=1
# print
#print(helloworld) #xxxx()是一個函式
#print(a+b)
# array 陣列
#hello=[helloworld, hellopython, a, 200, "100"] #變數,變數,數字,數字,字串
#print(hello[0]+ " " + hello[1])
#print(hello[2] + hello[3]) 
#print(hello[0] + str(hello[2])) #用str將數字轉換成字串，才印得出來 Hello World100
#print(str(hello[3]) + (hello[4])) #[4]本身就是字串 不用轉str 200100
#print(hello[3] + int(hello[4])) #用int把(hello[4])字串轉換成數字，才能運算 300
# 使用者輸入
# input_article = input("請輸入網址")
# if input_article:
#   print(input_article)
# else:
#   print("沒有資料")

#input_article = input("請輸入數字")
#print(type(input_article)) #檢查並印出輸入的類型

#if input_article and type(input_article) == int: # 值是存在的而且是整數 ==是比較的意思
  #input_article = int(input_article) #更新變數字串成數字
  #print(type(input_article)) #檢查並印出輸入的類型
  #if input_article > 10:  #有冒號下一行就要縮排
    #print("你的值大於 10")
  #else:
    #print("你的值小於 10")
#else:
  #print("沒有資料")

# 2024-9-1 學習進度
# list 列表和列表的基本涵式
list = [1,2,3] # 用中括號來包住資料
# tuple 元組
tuple = (1,2,3) # 用小括號來包住資料
# tuple不同於list，資料不能被新程式碼新增、刪除、變更，適合儲存經緯度等資料
# function 涵式
def hello(name,age): # 定義涵式
  print("hello"+ name + "你今年" + age + "歲")  # 函式內容

hello("小白","87") # 呼叫涵式並填入資料
# if else
# for loop 迴圈
# function 自訂函數

