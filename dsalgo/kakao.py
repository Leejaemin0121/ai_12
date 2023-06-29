# %%
kakao = ["다현", "정연", "쯔위", "사나", "지효"]
print(kakao)

# %%
print(kakao[0])
print(kakao[4])

# %%
kakao.append(None)
print(kakao)

# %%
kakao[5]= "모모"
print(kakao)

# %%
kakao.append(None)
print(kakao)

# %%
kakao[6] = kakao[5]
kakao[5] = None
print(kakao)


# %%
kakao[5] = kakao[4]
kakao[4] = None
kakao[4] = kakao[3]
kakao[3] = None
print(kakao)

# %%
kakao[3] = "미나"
print(kakao)

# %%
kakao[4] = None
print(kakao)

# %%
kakao[4] = kakao[5]
kakao[5] = None
kakao[5] = kakao[6]
kakao[6] = None
print(kakao)

# %%
