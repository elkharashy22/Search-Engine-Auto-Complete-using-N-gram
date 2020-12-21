import nltk
import re
emma = nltk.corpus.gutenberg.words('austen-emma.txt')
popw=1
resw=[]
respw=[]
poppw=1
liii=[]
listk=[]
listk=emma
listkk=[]
for xx in listk:
 if(xx.isalpha()==False):
  continue
 listkk.append(xx)
listkkk=" ".join(listkk)
 
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import gutenberg

corpus22 = " ".join(map(str, emma))
sentense=sent_tokenize(corpus22)
print(type(listkk))
inputs=raw_input("enter the word    ")
li=[]
il=[]
#print(sentense[0])
for ws in sentense[0:200]:
        soo=ws.split(" ")
        
        for wso in soo:
           if(len(inputs.split())==1): 
             if(wso==inputs):
               # print(ws)
                li.append(ws)
                
                il.append(soo.index(inputs))
              #  print(soo.index(inputs))
                break
           else:
               rro=inputs.split()
               vari=rro[0]
               varis=re.compile(r'\b%s\b' % inputs, re.I)
               if(len(re.findall(inputs,ws))==1):
                 li.append(ws)
                 il.append(soo.index(vari))
                # print(soo.index(vari))
                 break
 

pop=1
popp=1
co=0
res=[]
resp=[]
for w in li :
    x=w.split()
    cl=len(x)
    sv=x[il[co]]
    c=0
    #print(il[co]+1)
    for v in x[il[co]+1:cl-1]:
        if(v.isalpha()==False):
            continue
        c+=1
        sss=sv
        sss+=" "
        sss+=v
        #print(sss)
        #print("-------")
        #print(sv)
        rsv=re.compile(r'\b%s\b' % sv, re.I)
        rsss=re.compile(r'\b%s\b' % sss, re.I)
        #print("-------")
        #print len(re.findall(rsss,listkkk))
        #print len(re.findall(rsv,listkkk))
        pop*=float(len(re.findall(rsss,listkkk)))/len(re.findall(rsv,listkkk))
        if(c>len(inputs.split())+1):
           sv=v 
           continue 
        
        popp*=float(len(re.findall(rsss,listkkk)))/len(re.findall(rsv,listkkk))
        sv=v
    co+=1              
    #print("--------------")    
    res=[]
    #print(pop)
    
    res.append(pop)
    #for l in res :
     #print (l)
    resp=[]
    #print(popp)
    resp.append(popp)
    #for r in resp :
     #print (r)
    popp=1
    pop=1
if(len(res)!=0):
    print(li[res.index(max(res))])
    rooo=li[resp.index(max(resp))].split()
    print(rooo[il[resp.index(max(resp))]+len(inputs.split())])
elif(len(inputs.split())==1):
    for wordss in listkkk:
        if(wordss.startwith(inputs)):
           liii.append(wordss)
    for wordsss in liii:
        svw=wordsss.split()
        svws=svw[0]
        cw=0
        for chss in svw[1:len(svw)]:
            cw+=1
            wsvws=re.compile(r'\b%s\b' % svws, re.I)
            new=svws
            new+=chss
            wchss=re.compile(r'\b%s\b' % new, re.I)
            popw*=float(len(re.findall(wchss,listkkk)))/len(re.findall(wsvws,listkkk))
            if(cw==len(inputs,split())+1):
                svws=chss
                continue
            poppw*=float(len(re.findall(wchss,listkkk)))/len(re.findall(wsvws,listkkk))
            svws=chess
        resw.append(popw)
        respw.append(poppw)
        poppw=1
        popw=1
            
    print(liii[resw.index(max(resw))])
    rooo=liii[res.index(max(respw))].split()
    print(rooo[len(inputs.split())])         
        
            
        
    
        
    
else:
 print(" ")
    

