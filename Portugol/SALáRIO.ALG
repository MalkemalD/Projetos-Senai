Algoritmo "Sal�rio_Total"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Marcio Carmona
// Descri��o   : o programa calcula o salario total de um vendedor sobre suas vendas
// Autor(a)    : Eduardo
// Data atual  : 19/05/2023
Var
// Se��o de Declara��es das vari�veis 
 SF, TV, P, ST, AD : REAL

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
   Escreva ("Digite o Sal�rio Fixo: ")
   Leia(SF)
   Escreva ("Digite o total de vendas em reais:")
   Leia(TV)
   Escreva ("Digite o percentual de vendas (0 a 100) :")
   Leia (P)
   AD := TV*(P/100)
   ST := SF+AD
   Escreva(" O Sal�rio Total �:",ST)
   
Fimalgoritmo