import re
class Calculator:
     numbersString=["zero","one","tow","three","four","five","six","seven","eight","nine","ten"]     
             
     def __init__(self):  
         self.numbersString=["zero","one","tow","three","four","five","six","seven","eight","nine","ten"] 
         
     def putNumbers(self,oldLine):
        i=0
        for index in range(len(self.numbersString)):
           oldLine=oldLine.replace(self.numbersString[index],str(i))
           i=i+1
        return(oldLine.replace(" ","")) 
    
    
    
    
     def doOperator(self,a,b,operator):
        if (operator=="+"):
            return(float(a) + float(b))
        if (operator=="-"):
           return(float(a) - float(b))            
        if (operator=="*"):
            return(float(a) * float(b))  
        if (operator=="/"):
            return(float(a) / float(b))
        
        
     def findFirstBrackets(self,exp):
         if "(" not in exp: return(-1,-1)
         start=exp.index("(")
         opened=0
         for pos in range(start,len(exp)):
           # print(a[pos])
            if exp[pos]=="(": opened=opened+1
            if exp[pos]==")": opened=opened-1
            if opened==0: 
                return(start+1,pos)       
            
            
     def calcFirst(self,operator):
         return(bool(re.search('\\*|/',operator)))   



     def calc(self,exp):
         if exp=="":  return "" 
         if exp.isnumeric(): return exp
         st,end=self.findFirstBrackets(exp)
         if st>-1:
            opened= exp[:st-1] + str(self.calc(exp[st:end]))  + exp[end+1:]
            print(opened)
            return(self.calc(opened))
           
         numbers=re.split('\\+|\\-|\\*|/', exp)
         numbers =list(map(float, numbers))
         operators= re.findall('\\+|\\-|\\*|/', exp)
            
         for index in range(len(operators)):
              if (self.calcFirst(operators[index])):
                  numbers=numbers[:index]  + [self.doOperator(numbers[index],numbers[index+1],operators[index])] + numbers[index+2:]
                  operators= operators[:index] + operators[index+1:]
                  if index>len(operators)-1: break
         sum=numbers[0] 
         for index in range(len(operators)):
              sum= self.doOperator(sum,numbers[index+1],operators[index])
         return(sum)
                     
            
            