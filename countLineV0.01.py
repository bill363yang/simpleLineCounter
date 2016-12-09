import os


class language:
    def __init__(self, name):
        self.name = name
        self.totLines = 0
        self.filenum = 0
        self.blankLines = 0


def addLang(nameList):
    langList = []
    for i in nameList:
        langList.append(language(i))
    return langList

def getLineNum(language):
    return language.totLines

def count(filePath, langList):
    fileQ = []
    for root, dirs, files in os.walk(filePath):
        for i in files:
            if i.split('.')[-1] in nameList:
                fileQ.append(os.path.join(root, i))
    # count lines in each file
    while fileQ != []:
        codeArray = open(os.path.abspath(fileQ[0])).readlines()
        currentName = fileQ[0].split('.')[-1]
        indexx = nameList.index(currentName)
        currentLang = langList[indexx]
        currentLang.totLines += len(codeArray)
        currentLang.filenum += 1
        currentLang.blankLines += codeArray.count('\n')
        del (fileQ[0])


def output(langList):
    langList = sorted(langList,key = getLineNum,reverse=True)
    countList = ['language', 'total lines', 'blank lines', 'files']
    print('{:<14} {:<14} {:<14} {:<14}'.format(countList[0], countList[1],
                                               countList[2], countList[3]))
    print("------------------------------------------------------------")
    total = [0 for i in range(3)]
    for i in langList:
        if i.filenum != 0:
            total[0] += i.totLines
            total[1] += i.blankLines
            total[2] += i.filenum
            line = '{:<14} {:<14} {:<14} {:<14}'.format(
                i.name, i.totLines, i.blankLines, i.filenum)
            print(line)
    print("------------------------------------------------------------")
    print('{:<14} {:<14} {:<14} {:<14}'.format('total', total[0], total[1],
                                               total[2]))


if __name__ == '__main__':
    nameList = ['java', 'c', 'js', 'html', 'py', 'lisp', 'm', 'cpp',\
                'css','sh']
    langList = addLang(nameList)
    count('./', langList)
    output(langList)
