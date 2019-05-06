import sys
from config import user_email,user_pass
import json
import smtplib

def sendEmail(dic,to_email):
    message="You can convert the unicode, we're not FBI\n"
    message+=json.dumps(dic,indent=4)
    try:
        server=smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.login(user_email,user_pass)
        server.sendmail(user_email,to_email,message)
        server.close()
        print("Email Sent")
    except:
        print("something went wrong")



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

def saveToFile(str,fileName):
    try:
        f=open(fileName,"w+")
    except:
        print(fileName, "File cannot be updated")
    f.write(str)

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
    if(str[-4:]==".txt"):
         f=open(str,"r")
         str=f.read()
         return str
    else:
        return str

if __name__ == "__main__": 
    print("                  Welcome to File Encrypter            ")
    dist_email=input("Please write to email: ")
    print("Encrypting Your File and sending to ",dist_email)
    str=sys.argv[1]
    dist_file=sys.argv[2]
    str=checkStrOrFile(str)
    charObj=stringToObjList(str)
    charObj=ObjListToTree(charObj)
    letter_code={}
    dict_of_letter_codes={}
    letter_code=huffman_traversal(charObj[0],myarr=letter_code)
    encrypted_str=""
    for i in str:
        if(i==" "):
            encrypted_str+="  "
        else:
            encrypted_str+=" "+letter_code[i]
            dict_of_letter_codes[i]=letter_code[i]

    saveToFile(encrypted_str,dist_file)
    sendEmail(dict_of_letter_codes,dist_email)
    print("TASK COMPLETED")
    print("""
        This Project is made by:
        Lakshya Khera (9917103014)
        Gaurav Singh Parihar (9917103015)
        Shubham Tak (9917103031)
        Naman

        Made in Love with Python and Linux <3
    """)
    