import copy
import glob
import os

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def clear(self):
        del self.items[:]
    def gett(self):
        return self.items

class TemplateBC(object):
    def __init__(self, nodeNum, chindex , content, childrenNodeNums):
        self._nodeNum = nodeNum
        self._chindex = chindex
        self._content = content
        self._childrenNodeNums = childrenNodeNums

    def getChIndex(self):
        return self._chindex

    def getNodenum(self):
        return self._nodeNum

    def getContent(self):
        return self._content

    def getChildrenNodeNums(self):
        return self._childrenNodeNums

    def setContent(self, newContent):
        self._content = newContent


globchildNum = -1
def set_globvar_to_default():
    global globchildNum    # Needed to modify global copy of globchildNum
    globchildNum = -1

def parseString(input, chindex, nodeNum, tree):
    global globchildNum  # Needed to modify global copy of globchildNum
    globchildNum = globchildNum + 1
    currentList = []
    childrenNodeNums = []

    while chindex < len(input):
        ch = input[chindex]
        if ch == ')':#end of sublist, return
            content = ''.join(currentList).strip()
            del currentList[:]
            tmpTemplate = TemplateBC(nodeNum, chindex, content, childrenNodeNums)
            # print(nodeNum , content)
            tree[nodeNum] = tmpTemplate
            return tmpTemplate
        elif ch == '(':#start of sublist, recursive call
            tmpTemplate = parseString(input, chindex + 1, globchildNum, tree)
            childrenNodeNums.append(tmpTemplate.getNodenum())#] = 1
            chindex = tmpTemplate.getChIndex()
            chindex = chindex + 1
            continue
        currentList.append(ch)
        chindex = chindex + 1
    return None

def labelmaker(s):
    rets = int(s[1])
    if rets < 0 or rets > 5:
        print("error!")
    return s[1]

def putEnding(tree, st, alist):
    if st.isEmpty():
        return
    elif len(tree[st.peek()].getChildrenNodeNums()) == 0:
        # print(")", end='')
        alist.append(')')
        st.pop()
        putEnding(tree, st, alist)

#f1 = open("../chemprot-data/developPosit_chem", "r")
#f1 = open("genefusion-data/non-DL version/test_180404_2048_onlysymbols_lim_result_pre.tsv", "r", encoding='utf-8')
#f1_files = glob.glob("genefusion-data/non-DL version/*.tsv")
#f1_files = glob.glob("genefusion-data/DL version/*.tsv")
f1_files = glob.glob("genefusion-data/DL_uniqueid/*.tsv")
for f1_path in f1_files:
    print(f1_path)
    f1 = open(f1_path, "r", encoding='utf-8')
    # f1 = open("../chemprot-data/nothing2", "r")
    data = f1.readlines()
    f1.close()


    ### Sunkyu : For the old version of tree LSTM input file(keonwoo made)
    cn = 0
    fw_path = "genefusion-data/snli-dl-version/{}".format(f1_path.split("/")[-1])
    if os.path.isfile(fw_path):
        continue
    print(fw_path)
    fw = open(fw_path, "w", encoding='utf-8')
    for element in data:
        tree = {}
        set_globvar_to_default()

        splitted = element.split("\t")
        fw.write(labelmaker(splitted[10]))
        fw.write("\t")
        try:
            parseString(splitted[10], 0, -1, tree) # old format
        except:
            print("error..")
            print(splitted[10])
            continue

        #parseString(splitted[10], 0, -1, tree) # old format
        for key in tree:#arrange for SNLIformat
            tmpContent = tree[key].getContent()
            if ' ' not in tmpContent:
                tree[key].setContent("")
            else:
                tree[key].setContent(tmpContent.split(" ")[1])

        st = Stack()
        alist = []

        for key in tree:
            if len(tree[key].getChildrenNodeNums()) != 0:
                st.push(key)
            # print('(' + tree[key].getContent(), end='')
            if len(tree[key].getChildrenNodeNums()) != 0:
                alist.append('(')
            if tree[key].getContent() != "":
                alist.append(tree[key].getContent())
            for j in range(key + 1):
                removeIndex = 0
                # print(key, j)
                # print(tree[j].getChildrenNodeNums())
                childNums = tree[j].getChildrenNodeNums()
                if key in childNums:
                    removeIndex = childNums.index(key)
                    del tree[j].getChildrenNodeNums()[removeIndex]
            putEnding(tree, st, alist)

        fw.write(' '.join(alist))
        fw.write("\t")
        fw.write(splitted[11][:-1])
        fw.write("\t")
        fw.write(splitted[0])
        fw.write("\t")
        fw.write(splitted[5])
        fw.write("\t")
        fw.write(splitted[8])
        fw.write("\n")
        del alist[:]
        tree.clear()
        st.clear()
    fw.close()
















