Algoritmo "Pe�as_e_PRE�O"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 19/05/2023
Var
// Se��o de Declara��es das vari�veis 
IPI, VU1, QP1, P2, VU2, QP2, VT   : REAL

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
   Escreva("Digite o valor da pe�a 1:")
   Leia(VU1)
   Escreva("Digite a quantidade de pe�as 1:")
   Leia(QP1)
   Escreva("Digite o valor da pe�a 2:")
   Leia(VU2)
   Escreva("Digite a quantidade de pe�as 2:")
   Leia(QP2)
   Escreva("Digite de percentagem que ser� acrescentado sobre o valor das pe�as:")
   Leia(IPI)
   VT := (VU1*QP1+VU2*QP2)*(IPI/100+1)
   Escreva(" O valor total �:", VT)
   
   

Fimalgoritmo