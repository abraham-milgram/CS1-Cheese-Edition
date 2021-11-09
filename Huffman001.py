from operator import itemgetter
class Tree:
    def __init__(self, left, right):
        self.r = right
        self.l = left

txt = input("Input Text Here: ")

res = {}
for keys in txt:
    res[keys] = res.get(keys, 0) + 1

resList = list(res.items())
resFinal1 = sorted(resList, key=itemgetter(1))
resFinal = []

for a in resFinal1:
    resFinal.append(a[0])

def treeMaker(input):
    spit = []
    isTrue = 0
    for a in input:
        if isTrue == 0:
            try:
                spit.append(Tree(a, input[input.index(a) + 1]))
            except:
                spit.append(a)
            isTrue = 1

        else:
            isTrue = 0
    return spit

huff = treeMaker(resFinal)

while True:
    if len(huff) == 1:
        break
    else:
        huff = treeMaker(huff)

def detect(node):
    paths = []
    path = []
    nodes = [node]
    right = False
    latestMove = False
    touched = []
    while True:
        activeNode = nodes[-1]
        touched.append(activeNode)
        if type(activeNode) == Tree:
            latestMove = right
            if right == False:
                path.append("0")
                nodes.append(activeNode.l)
                touched.append(activeNode.l)
            elif right == True:
                path.append("1")
                nodes.append(activeNode.r)
                touched.append(activeNode.r)
                right = False

        else:
            paths.append((str(activeNode), ''.join(path)))
            nodes.remove(nodes[-1])
            count = 1
            try:
                while True:
                    if latestMove == True:
                        nodes.remove(nodes[-1])
                        count += 1
                    else:
                        break
                    
                    if nodes[-1].l not in touched or nodes[-1].r not in touched:
                        break
            except:
                return dict(paths)
            
            for i in range(count):
                path.pop()
            right = True

def encode(key, text):
    textList = list(text)
    final = []
    for char in textList:
        final.append(key[char])
    return ''.join(final)

def decode(tree, binary):
    binary1 = list(binary)
    activeNode = tree
    string = []
    for i in binary1:
        
        if type(activeNode) == str:
            string.append(activeNode)
            activeNode = tree

        if i == '0':
            activeNode = activeNode.l
        else:
            activeNode = activeNode.r
    string.append(activeNode)
    return ''.join(string)

            
tree = huff[0]
key = detect(tree)
encoded = encode(key, txt)
decoded = decode(tree, encoded)
bitSaved = 100-((len(encoded)/(len(txt) * 8))*100)
print(f"""Text: {txt}
Huffman Values: {key}
Encoded Text: {encoded}
Dedcoded: {decoded}
Size reduced by: {round(bitSaved, 2)}%""")