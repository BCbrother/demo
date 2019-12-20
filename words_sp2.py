import jieba

# 获取文本并做简单处理
def getText():
    txt = open("words2.txt",'r',encoding='utf-8').read()
    # 默认词组需要排除
    default_tags = ['产品名称','品牌名称','型号','电池类型','颜色分类',
                    '生产企业','附加功能','外壳材质','尺寸','电池类型',
                    '电池容量','款式','类别']
    for w in default_tags:
        txt = txt.replace(w,',')
    for ch in '\n,:、。，：/':
        txt = txt.replace(ch,"")
    return txt

# 利用jieba库和自建字典库进行分词
def split_words(txt):
    jieba.load_userdict("dict.txt")     #更准去的自主词典库，需要主动手动添加
    words = jieba.lcut(txt)                            
    new_words = list()
    for word in words:
        if len(word)==1:
            continue
        else:
            new_words.append(word)
    return new_words

# 写入结果txt文档中，已每个词组单独一行进行写入
def writeTxt(testList):
    f = open("results2.txt",'w',encoding='utf-8')
    for line in testList:
        f.write(line + '\n')
    f.close()

txt = getText()      #依次调用：获取文本函数、文本分词函数、写入文本函数
words = split_words(txt)       
writeTxt(words)                