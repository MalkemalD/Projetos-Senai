Algoritmo "Maior_Deles"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 19/05/2023
Var
// Se��o de Declara��es das vari�veis 
N1,N2, N3 : REAL

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
   Escreva ("Digite um numero:")
   Leia(N1)
   Escreva ("Digite OUTRO numero:")
   Leia(N2)
   Escreva ("Digite OUTRO numero:")
   Leia(N3)
   SE (N1>N2) e( N1>N3) ENTAO
      Escreva(" o primeiro numero � maior")
   Fimse
   Se (N2>N1) e (N2>N3) Entao
      Escreva ("o segundo numero � o maior")
   Fimse
   Se (N3>N1) e (N3>N2) Entao
      Escreva ("o terceiro numero � o maior")
   Fimse
Fimalgoritmo