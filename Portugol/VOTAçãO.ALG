Algoritmo "Vota��o"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 19/05/2023
Var
// Se��o de Declara��es das vari�veis 
TE, VB, VN, VV, PV, PN, PB  : Real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
   Escreva (" Digite a quntidade total de eleitores:")
   Leia(TE)
   Escreva (" Digite a quantidade de votos validos:")
   Leia(VV)
   Escreva (" Digite a quantidade de votos brancos:")
   Leia(VB)
   Escreva (" Digite a quantidade de votos nulos:")
   Leia(VN)
   PV := ((VV/TE)*100)
   Escreva (" A porcentagem de Votos validos em rela��o ao total de eleitores �:", PV)
   PN := ((VN/TE)*100)
   Escreva (" A porcentagem de Votos Nulos em rela��o ao total de eleitores �:", PN)
   PB := ((VB/TE)*100)
   Escreva (" A porcentagem de Votos Brancos em rela��o ao total de eleitores �:", PB)
Fimalgoritmo