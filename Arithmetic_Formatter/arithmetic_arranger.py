def arithmetic_arranger(problems,flag=False):
  if len(problems)>5:
    return "Error: Too many problems."

  numerator=""
  denominator=""
  dashes=""
  sumx=""
  string=""

  for problem in problems:
    operand1,operator,operand2=problem.split()
    
    #conditions
    if operator!='+' and operator!='-':return "Error: Operator must be '+' or '-'."
    elif not operand1.isdigit() or not operand2.isdigit():return "Error: Numbers must only contain digits."
    elif len(operand2)>4 or len(operand1)>4:return "Error: Numbers cannot be more than four digits."


    
    ans=str(int(operand1)+int(operand2)) if operator=="+" else str(int(operand1)-int(operand2))
    length=max(len(operand1),len(operand2))+2
    top=str(operand1).rjust(length)
    bottom=operator + str(operand2).rjust(length-1)
    dash=""
    res=str(ans).rjust(length)
    for _ in range(length):
      dash+="-"

    if problem!=problems[-1]:
      numerator+=top+'    '
      denominator+=bottom+'    '
      dashes+=dash+'    '
      sumx+=res+'    '
    else:
      numerator+=top
      denominator+=bottom
      dashes+=dash
      sumx+=res
      
      
  if flag:
      string=numerator+"\n"+denominator+"\n"+dashes+"\n"+sumx
  else:
      string=numerator+"\n"+denominator+"\n"+dashes
  return string