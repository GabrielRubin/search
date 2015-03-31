/**********************************************************************
 *  Hyrule's maze readme.txt template
 **********************************************************************/


Name: Gabriel de Arruda Rubin de Lima
Student ID: 101003713


Hours to complete assignment (optional): 5-6 hours


/**********************************************************************
 *  Explain briefly how you implemented the datatype for states.
 **********************************************************************/

 Cada Nodo foi implementado como uma classe no python. Não enfrentei muitos problemas de performace e acho que foi ok.



/**********************************************************************
 *  Explain briefly how you represented a search node
 *  (state + number of moves + previous search node).
 **********************************************************************/

 Os nodos de busca tem informações de x, y, seu antecessor, o tipo do nodo (que é sempre o mesmo) e o seu custo de movimento (que é sempre 1)
 Coloquei nele ainda algumas funções legais de Python que permitem a comparação mais rápida e "built-in" entre dois Nodos usando "=="

 O algoritmo funciona com uma fila de prioridade e uma lista de nodos ja visitados, sempre que um nodo já existia na lista (se tinha um objeto de mesmo x e y),
 ele verifica qual foi o ultimo custo que ele tinha na lista e decide se continua pesquisando por ele ou não. Eu demorei um pouco para me dar conta
 da importância dessa etapa para encontrar uma solução.


/**********************************************************************
 *  Explain briefly how you detected unsolvable problems.
 **********************************************************************=

 Meu algoritmo de detecção é recursivo e bem "burro", mas ele é bem rapido e barato, ele pega uma cópia do mapa e parte da posição do player. De um certo nodo,
 (o nodo do player no começo), vejo quais são meus sucessores (vizinhos) possiveis, e faço a recursão neles. A recursão em si retorna falso quando é um terreno
 "parede" (que o player não caminha), retorna verdadeiro quando é igual ao objetivo. Se ele não retornou nenhum destes dois, ele "pinta" a posição atual de "parede" e
 retorna o "ou" combinado de todos os seus vizinhos depois.

/**********************************************************************
 *  If you wanted to solve random $10^6$ problem, which would you 
 * prefer:  more time (say, 2x as much), more memory (say 2x as much), 
 * a better priority queue (say, 2x as fast), or a better priority 
 * function (say, one on the order of improvement from Hamming to 
 * Manhattan)? Why?
 **********************************************************************/

 Eu iria preferir mais memória, acho que esse é o grande problema do algoritmo. O fato dele ter que manipular várias posições e listas é bem custoso, sem contar que
 ele "visita" os Nodos diversas vezes e tem que manter eles na memória a todo o tempo, acho que em segundo lugar seria uma heuristica melhor.

/**********************************************************************
 *  If you did the extra credit, describe your algorithm briefly and
 *  state the order of growth of the running time (in the worst case)
 *  for isSolvable().
 **********************************************************************/

 A explicação do algoritmo está ali em cima, é com ele que eu detecto que o problema não tem solução. Creio que ele é rapido e eficaz em running time,
 no pior caso, ele vai entrar na recursão n vezes, sendo n o número de Nodos/posições do problema. E na média ele deve ficar bem próximo do tamanho total
 de Nodos, fora quando o mapa tiver muitas paredes.


/**********************************************************************
 *  Known bugs / limitations.
 **********************************************************************/

 Não encontrei nenhum durante meus testes.

/**********************************************************************
 *  Describe whatever help (if any) that you received.
 *  Don't include readings, lectures, and precepts, but do
 *  include any help from people (including staff, classmates, and 
 *  friends) and attribute them by name.
 **********************************************************************/



/**********************************************************************
 *  Describe any serious problems you encountered.                    
 **********************************************************************/

 Eu implementei a função de A* com um ultimo parametro opcional, este parametro diz se a pesquisa para quando a resposta foi encontrada ou para
 quando a fila de prioridade estiver totalmente vazia (o maximo de altura da arvore foi atingido nesse caso). A primeira opção é bem mais rapida, mas não
 calcula a altura máxima da arvore de pesquisa. Em testes que fiz usando exclusivamente o segundo approach, tive uma performace muito pior, então resolvi
 deixar as duas implementações prontas, com um booleano controlando qual vai ser usada.

/**********************************************************************
 *  List any other comments here. Feel free to provide any feedback   
 *  on how much you learned from doing the assignment, and whether    
 *  you enjoyed doing it.                                             
 **********************************************************************/

 Adoro Zelda yey! Gostei bastante do trabalho, aprender à usar o GitHub foi muito bom e Python é bem bonito, apesar de ser meio chato às vezes.
 Kudos pro professor e os TAs pelo trabalho bem legal e por esse framework bem robusto e facil de entender, foi bem divertido desenvolver a
 solução do problema.