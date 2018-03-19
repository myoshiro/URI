def CheckPrior(char):
    
    
    if (char == "+" or char == "-"):
        prior = 1
    elif (char == "*" or char == "/"):
        prior = 2
    elif (char == "^"):
        prior = 3
    else:
        prior = 0
    return prior


def InToPost():

  Input=[]
  MyIndex = 0
  numTests = int(input())
  
  while MyIndex < numTests:
    Input.append(input())
    MyIndex += 1


  outputText = ""
  
  while len(Input) > 0:
  
      operators=[]

      expression=Input.pop(0)
      expSize = len(expression)
  
      for j in range (0,expSize):

          if expression[j] not in "+-*/^()" :
              outputText += expression[j]
  
          elif len(operators) == 0 or expression[j] == "(" or operators[-1] == "(":
               operators.append(expression[j])
                         
          elif (expression[j] == ")"):
              while operators[-1] != "(":
                  outputText += operators.pop()
              
              operators.pop()
              
  
          elif (CheckPrior(operators[-1]) < CheckPrior(expression[j])):
              operators.append(expression[j])
              
          else:
              while CheckPrior(operators[-1]) >= CheckPrior(expression[j]):
                  outputText += operators.pop()
                  if len(operators) == 0:
                      break

              operators.append(expression[j]) 
          
        
      while(len(operators) > 0):
        if operators[-1] != "(" and operators[-1] != ")":
           outputText += operators.pop()
        else:
          operators.pop()
           
      if (len(Input) >= 1):     
          outputText+= "\n"    
  

  print(outputText)
  return 0
  
InToPost()
