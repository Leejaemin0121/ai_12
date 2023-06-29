# %%
kakao3 = []

def add_data(friend):
    
    kakao3.append(None)
    kLen = len(kakao3)
    kakao3[kLen - 1] = friend
    
add_data("다현")
add_data("정연")
add_data("쯔위")
add_data("사나")
add_data("지효")

print(kakao3)

# %%

kakao5 = ["다현", "정연", "쯔위", "사나", "지효"]

def insert_data(position,friend):
    
    if position < 0 or position > len(kakao5):
        print("데이터를 삽입할 범위를 벗어났습니다,")
        return
    
    kakao5.append(None)
    kLen = len(kakao5)
    
    for i in range(kLen - 1, position, -1):
        kakao5[i] = kakao5[i - 1]
        kakao5[i - 1] = None
        
    kakao5[position] = friend
    
insert_data(2,"솔라")
print(kakao5)  
insert_data(6,"문별")
print(kakao5)  
    
# %%

kakao5 = ["다현", "정연", "쯔위", "사나", "지효"]

def delete_data(position):
    
    if position < 0 or position > len(kakao5):
        print("데이터를 삽입할 범위를 벗어났습니다,")
        return
    
    kLen = len(kakao5)
    kakao5[position] = None
    
    for i in range(position + 1, kLen):
        kakao5[i - 1] = kakao5[i]
        kakao5[i] = None
        
    del(kakao5[kLen - 1])
    
delete_data(1)
print(kakao5)
delete_data(3)
print(kakao5)

# %%
