def reversedWords(strings):
    print("원래 문장 :{}".format(strings))
    # Words=strings.split(" ")
    # result=[]
    # for word in Words:
    #     result.append(word[::-1]+" ")
    Words=strings.split(" ")[::-1]
    result=[]
    for idx,word in enumerate(Words):
        if idx!=len(Words)-1:
            result.append(word+" ")
        else:
            result.append(word)
    return "결과 문장: "+"".join(result)





if __name__ =="__main__":
    str1="Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth;"
    str2="Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,"
    print(reversedWords(str1))
    print(reversedWords(str2))


