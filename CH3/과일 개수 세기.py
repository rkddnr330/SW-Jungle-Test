fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
ans={}
for i in fruits:
    if i not in ans:
        ans[i]=1
    else:
        ans[i]+=1
print(ans['사과'])