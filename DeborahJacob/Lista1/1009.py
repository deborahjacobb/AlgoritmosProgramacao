##https://www.beecrowd.com.br/judge/pt/problems/view/1009

NOMEVEND = input()
SALARIOFIXO = float(input())
TOTVENDAS = float(input())
 
BONUS = float(TOTVENDAS * 15/100)
VALORTOTAL = (SALARIOFIXO + BONUS)
 
print("TOTAL = R$ %.2f" %(VALORTOTAL))
