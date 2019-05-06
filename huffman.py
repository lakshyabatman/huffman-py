import sys


class Node():
   def __init__(self,letter):
        self.letter=letter
        self.left=None
        self.right=None
        self.probability=None
        self.count=0
        self.code=""


def huffman_traversal(NodeObj,myarr):
    if(NodeObj.left!=None or NodeObj.right!=None):
            NodeObj.left.code=NodeObj.code+"🐍"
            NodeObj.right.code=NodeObj.code+"🐘"
            myarr[NodeObj.left.letter]=NodeObj.left.code
            myarr[NodeObj.right.letter]=NodeObj.right.code
            huffman_traversal(NodeObj.left,myarr)
            huffman_traversal(NodeObj.right,myarr)
    return myarr



def stringToObjList(str):
    all_freq = {} 
    for i in str: 
        if i in all_freq: 
            all_freq[i] += 1
        else: 
            all_freq[i] = 1
    try:
        all_freq.pop(' ')
    except:
        print(all_freq)
    count=len("".join(str.split(" ")))
    charObj=[]
    for key in all_freq:
        temp= Node(letter=key)
        temp.count=all_freq[key]
        temp.probability=(temp.count/count)
        charObj.append(temp)
    return charObj

def ObjListToTree(charObj):
    while(len(charObj)>1):
        charObj.sort(key=lambda x: x.probability)
        smallest=charObj[0]
        second_smallest=charObj[1]
        temp_node= Node(smallest.letter+second_smallest.letter)
        temp_node.probability=smallest.probability+second_smallest.probability
        temp_node.left=smallest
        temp_node.right=second_smallest
        charObj.append(temp_node)
        charObj.remove(smallest)
        charObj.remove(second_smallest)
    return charObj

def checkStrOrFile(str):
    print(str[-4:])
    if(str[-4:]==".txt"):
         f=open(str,"r")
         str=f.read()
         return str
    else:
        return str

if __name__ == "__main__": 
    str=sys.argv[1]
    str=checkStrOrFile(str)
    charObj=stringToObjList(str)
    charObj=ObjListToTree(charObj)
    letter_code={}
    letter_code=huffman_traversal(charObj[0],myarr=letter_code)
    enrypted_str=""
    for i in str:
        if(i==" "):
            enrypted_str+="  "
        else:
            enrypted_str+=" "+letter_code[i]
    print(enrypted_str)