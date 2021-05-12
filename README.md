# Exam2
這個程式因為wifi在考試途中突然連不上所以readme沒有辦法放圖片  

這個程式先執行main.cpp，然後緊接著等連到wifi的時候直接執行python，接下來在main.cpp會print出5個測試訊息。  
之後打/GestureUI/run 1，如果打對了會有set up successful。  
之後就可以開始做手勢，圈圈 = 0(逆時針)，slope為1，向前為2(按鈕朝前)  
每做出一個手勢就會傳資料到pyhton，當python收到資料就會把當前收到的手勢print出來。  
當接到10次訊號後python就會在screen print出/FLIP/run 1  
這樣就會停止判斷手勢  

