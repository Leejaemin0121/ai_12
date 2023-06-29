#함수 선언
def add_data(friend):
    
    kakao.append(None)
    kLen = len(kakao)
    kakao[kLen - 1] = friend
    

def insert_data(position,friend):
    
    if position < 0 or position > len(kakao):
        print("데이터를 삽입할 범위를 벗어났습니다,")
        return
    
    kakao.append(None)
    kLen = len(kakao)
    
    for i in range(kLen - 1, position, -1):
        kakao[i] = kakao[i - 1]
        kakao[i - 1] = None
        
    kakao[position] = friend
    
    
def delete_data(position):
    
    if position < 0 or position > len(kakao):
        print("데이터를 삽입할 범위를 벗어났습니다,")
        return
    
    kLen = len(kakao)
    kakao[position] = None
    
    for i in range(position + 1, kLen):
        kakao[i - 1] = kakao[i]
        kakao[i] = None
        
    del(kakao[kLen - 1])
    

#전역 변수 선언
kakao = []
select = -1 # 1: 추가, 2: 삽입, 3: 삭제, 4: 종료


#메인 코드 부분
if __name__ == "__main__":
    
    while (select != 4):
        
        select=int(input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> "))
        
        if (select == 1):
            data = input("추가할 데이터--> ")
            add_data(data)
            print(kakao)
        elif (select == 2):
            pos=int(input("삽입할 위치--> "))
            data = input("추가할 데이터--> ")
            insert_data(pos, data)
            print(kakao)
        elif (select == 3):
            pos=int(input("삭제할 위치--> "))
            delete_data(data)
            print(kakao)
        elif (select == 4):
            print(kakao)
            exit
        else:
            print("1~4 중 하나를 입력하세요.")
            continue