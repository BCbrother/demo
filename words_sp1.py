#获取文本
def getText():
    txt = open("words.txt",'r').read()
    default_tags = ['Product Name','Material','Style','Fabric Type',
                'Sleeve Length(cm)','Decoration','Clothing Length','Pattern Type',
                'Collar','Sleeve Style','Model Number','Gender','Item Type',
                'Tops Type','Sleeve length','Clothing pattern','Pattern culture',
                'style','Commuter','Main color','Material composition',
                'Product Description']
    for w in default_tags:
        txt = txt.replace(w,',')
    #将特殊符号用空格代替
    for ch in ',./:()':
        txt = txt.replace(ch," ")
    return txt

def writeTxt(testList):
    f = open("words_result.txt",'w')
    for line in testList:
        f.write(line + '\n')
    f.close()

testTxt = getText()
#对文本进行切割
words = testTxt.split()
# 覆盖写入txt文档
writeTxt(words)