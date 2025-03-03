t=int(input())
for _ in range(t):
    a=input()
    s=[i for i in a]
    st=[]
    d={"(":")","{":"}","[":"]"}
    for i in s:
        if i in d.keys():
            st.append(i)
        else:
            if st!=[]:
                if d[st[-1]]==i:
                    st.pop()
    if st!=[]:
        print("False")
    else:
        print("True")
