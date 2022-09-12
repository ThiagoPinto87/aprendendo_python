<h6 align="center"> ✔️ FINALIZADO ✔️ </h6>
<h1> Aprendendo Python </h1>

Estou iniciando os estudos em programação.
Já hávia iniciado o curso sobre HTML e CSS _(mesmo sabendo que são linguagens de marcação)_ pois eu estava querendo ter como próximo passo aprender Java Script. Porém, ao pesquisar sobre a linguagem de programação, um colega de trabalho comentou comigo sobre o Python e fui buscar informações e foi onde eu decidi que ele me ajudaria bastante nos objetivos de minha carreira profissional conforme exposto na bio.
<a> Este curso estou fazendo através do site: <https://www.cursoemvideo.com/>.</a>

<h2>Diário de Aprendizagem</h2>

---
<details>
<summary><h3>Mês 06/2022</h3></summary>
<details>   
   <summary>03/06/2022</summary>
   
* Aprendi como subir finalmente do PyCharm para o GitHub, eu havia feito sem querer inicialmente, mas agora entendi como funciona a ferramenta.
* Aprendi a estilizar um pouco melhor o GitHub para ficar mais amigável aos parceiros que quiserem colaborar comigo. _(Sejam todos bem vindos)_
</details>

<details>   
   <summary>04/06/2022</summary>

* Por não ter conseguido resolver o exercício 86 e 87 tão satisfatóriamente quanto eu gostaria, eu decidi reassistir às aulas 17 e 18 do curso em vídeo. (Assisti também alguns exercícios pois dentro dos exercícios às vezes o professor insere informações importantes.)
    * Aula 17: [link para a aula](<https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/listas-em-python/modulos/listas-parte-1/>)
    * Aula 18: [link para a aula](<https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/listas-em-python/modulos/listas-parte-2/>)
* Entendi que meu erro no exercício 86 foi de não deixar preparada a variável "matriz_numeros" já com os números zerados, devendo serem só substituídos. Pois por mais que o professor guanabara tivesse dito, eu tentei (teimosamente) inserir as informações com o método <code>.append()</code>, visto que eu não havia preenchido a variável com "0".
* Foi importante também que por falta de praticar a manipulação de string's eu havia esquecido como deixar um resultado da forma como eu quero como por exemplo o resultado ser em 5 caractéres e centralizado, usando o comando <code>:^5</code>.
</details>

<details>   
   <summary>08/06/2022</summary>

* No final de semana do dia 04/06, fiquei bastante ruim com uma gripe muito forte. Até suspeitei de COVID, mas graças a Deus o resultado foi negativo para a doença mas vamos lá, sem chorumelas!
* Na atualização de hoje é que fui cair na real que a variável <code>matriz_numeros[l][c]</code> onde <code>[l][c]</code> trata-se dos respectivos índices dos valores da variável. Depois que entendi isso ficou mais fácil, mesmo assim, precisei assistir o vídeo da resolução do exercício mais uma vez para consertar alguns erros. Identifiquei também que cada vez que faço comentários sobre cada passo, consigo absorver melhor o conhecimento do que estou fazendo.
* Estou também apendendo e mexer no aplicativo notion do site <notion.so>, muito bacana. Dá pra fazer muita coisa nele!
</details>

<details>   
   <summary>18/06/2022</summary>

* Fiquei bastante dia sem estudar e isso me deixou muito triste comigo mesmo, me mantenho empenhado em aprender, porém, a desculpa dessa vez foi a visita de meu pai que chegou de viagem e como vejo ele poucas vezes no ano, dei prioridade a ele.
* Hoje finalizei os exercícios 088 e 089. Fiquei bravo comigo mesmo pois percebi que fiz o exercício 088 mais copiando do que de fato aprendendo, sorte a minha que me exijo bastante comentando cada string o que me ajuda a absorver as informações.
* No Exercício 088: Apesar de copiar, pode reparar que fiz ao meu modo o que deu um toque de originalidade. Eu havia me esquecido do detalhe em fazer a cópia da lista que usa o serguinte termo <code>[:]</code>. Isso é muito importante na manipulação das listas. Esse termo quer dizer cópia e se assemelha bastante à manipulação de strings onde ao ter uma string qualquer com uma informação, podemos colocar que queremos do índice 3 até o índice 5 <code>[3:5]</code> ou do índice 4 até o final da string <code>[4:]</code>.
* No Exercício 089: Pode observar que fiz ao meu modo, onde gostei mais da minha solução à solução do prof. Guanabara, pois pude praticar mais a manipulação das listas e, mesmo que na lista composta dele tenha uma lista a mais, eu conseguiria inseri-la com facilidade. Só não fiz por não me parecer lógico criá-la (sei que se trata de exercício, mas achei que dessa forma pratiquei mais).
* Gostei também de relembrar a manipulação das strings, visto que tenho quase "toc" por ver tabelas desorganizadas. 
```Python
print(f'{i:<4}{a[0]:<15}{a[3]:>4.1f}')
```
</details>

<details>   
   <summary>20/06/2022</summary>

* Hoje consegui somente assistir a aula 19 do curso de Python do curso em vídeo, fiz diversas anotações das quais vou compartilhar com vocês aqui embaixo.
    * Link para a [Aula 19](https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/dicionarios-em-python/modulos/dicionarios/)


<h5>Dicionário</h5>

* Os dicionários são descritos em <code>{}</code>.

* Para adicionar novas chaves (keys) à lista com dicionários, não é necessário usar o <code>append()</code>, basta declarar o novo elemento como no exemplo:

```Python
In[]
dados = {'nome': 'Thiago', 'idade': 35}
dados['sexo'] = 'M'
print(dados)

Out[]
{'nome': 'Thiago', 'idade': 35, 'sexo': 'M'}
```

* Para remover os dados, podemos usar o parâmetro <code>del()</code>.

```Python
In[]
dados = {'nome': 'Thiago', 'idade': 35, 'sexo': 'M'}
dados del ['idade']

print(dados)

Out[]
{'nome': 'Thiago', 'sexo': 'M'}
``` 

* Outra forma de se fazer um dicionário é:

```Python
filme = {'título = Stars Wars
         'ano' = 1977
         'diretor' = 'Geroge Lucas'}
```
O elementos como ‘título’, ‘ano’ e ‘diretor’, são conhecidos no python como chaves (Key’s)

* É importante identificarmos as diferenças entre: Values, Keys e Items. Conforme demonstrações baixo:
  * <code>Values</code>, são as infomações de dentro das keys
  * As <code>Keys</code> são semelhantes aos índices em uma lista.
  * Os <code>Items</code> são todas as informações da lista como Keys e Values. São muito bem utilizadas nas estruturas de repetições.
  
* Nas estruturas de repetições, podemos misturar as 3 formas de estruturas (tuplas, listas e dicionários) podendo ser criado criado uma lista de locadoras (por exemplo) e cada índice dessa lista possuir um dicionário com Keys informando o título, o ano e o diretor.
  
Ou seja um <code>print()</code> nessa estrutura seria da seguinte maneira:

```Python
locadora = [{'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}, {{'titulo': 'Avangers', 'ano': 2012, 'diretor': 'Joss Whedon'}

In[]
print(locadora[0]['ano'])
print(locadora[1]['titulo'])

Out[]
1977
Avangers
```
 
* No caso de criar cópias de dicionários ou inserir um dicionário dentro de uma lista, temos que fazer da seguinte maneira:

```Python
In[]

estado = dict()  # Cria o dicionário "estado".
brasil = list()  # Cria uma lista "brasil".

for c in range(3):  # Laço de repetição para receber inputs
    estado['uf'] = str(input('Unidade Federativa: '))  # Captura informação para inserir dentro do dicionário "estado" na key 'uf'.
    estado['sigla'] = str(input('Sigla do estado: '))  # Captura informação para inserir dentro do dicionario " estado na key 'sigla'.
    brasil.append(estado.copy())  # INSERE UMA CÓPIA DO ESTADO DENTRO DA LISTA BRASIL. ANTES QUANDO INSERIAMOS UMA LISTA DENTRO DA OUTRA USÁVAMOS O FATIAMENTO DE STRING [:].
    
for e in brasil:  # Cria laço de repetição para ler dentro da lista brasil.
    for u, s in e.items():  # Cria laço de repetição para ler dentro dos dicionários que estão dentro da lista brasil (utilizo o "e" e não o estado, pois ele está subordinado (identado) ao "for" acima.)
        print(f'O campo {u} tem valor {s}')  # Imprime os resultados dos dicionários em f'string.


Terminal[]

Unidade Federativa: "MATO GROSSO"
Sigla do estado: "MT"
Unidade Federativa: "SÃO PAULO"
Sigla do estado: "SP"
Unidade Federativa: "ACRE"
Sigla do estado: "AC"

Out[]

O campo uf tem valor MATO GROSSO
O campo sigla tem valor MT
O campo uf tem valor SÃO PAULO
O campo sigla tem valor SP
O campo uf tem valor ACRE
O campo sigla tem valor AC

```
Como podemos observar no caso de listas usávamos o fatiamento de string que demosntra o total da string <code>[:]</code>. Para dicionários usa o métido próprio chamado <code>copy()</code>.

*  Aprendi também a realçar blocos de código em _markdown_, para ficar mais amigável o entendimento com vocês. Muito legal.
</details>

<details>   
   <summary>25/06/2022</summary>

* Hoje somente criei os exercícios, nem tentei executá-los pois tive um dia bastante corrido e gostaria de ao menos ter deixado isso pronto hoje. Sei que foi bastante rapido, porém, me comprometo no próximo commit ter um progresso melhor.
</details>

<details>   
   <summary>26/06/2022</summary>

* Na resolução dos exercícios de hoje, fiz com facilidade o exercício 090, porém o 091 tive dificuldades pois além do professor ensinar um novo import, eu estava tentando criar dicionários com nome e jogo para depois inserir no dicionário, como não consegui, tentei fazer como na explicação da aula 19 e fazer como lista, porém, sem sucesso.
Mas pude perceber que não é o caminho totalmente errado, pois no import do <code>operator</code>, ele tranforma o dicionário em lista, pois inicialmente o prof. Guanabara até chegou de orientar a colocar o "ranking" como dicionário e o <code>operator</code> transformou o dicionário em lista. Com isso, me despertou a curiosidade de fazer como eu estava imaginando, bater um pouco a cabeça e tentar concluir o exercício como fiz inicialmente e depois usar o método <code>sort()</code> na lista de cada jogada.
</details>

<details>   
   <summary>28/06/2022</summary>

* Hoje senti muita facilidade em ambos os exercícios:
    * Exercício 092:
    * Notei que o prof. Guanabara, utilizou um import diferente do que vinha utilizando como aconteceu nos exercícios 032 e 039 (não li sobre o import do <code>datetime</code> que ele utilizou dessa vez);
    * Notei também que fiz codei diferente dele, conforme abaixo.
```python
Prof_Guanabara[]
trabalhador = dict()
trabalhador['nome'] = str(input('Nome: '))
...

Thiago[]
trabalhador = {'nome': str(input('Nome: ')).strip().upper(),
               'idade': date.today().year - int(input('Ano de nascimento: ')),
               'ctps': int(input('Nº CTPS (0 se não tem): '))}

```
   
   * Exercício 093:
      * Fizemos um pouco diferentes, porém dessa vez, gostei mais da minha solução, visto que tive a atenção de enumerar para o usuário preencher no relatório a informação da primeira partida mostrando o número 1 e o prof. fez mostrando o índice da lista (deu mólim professor. rsrsrs. Abçs).
      * Outro detalhe que gostei mais também, foi que no último _print_, pude treinar utilizando a toda a parte do fatiamento mesclando key com chave. Foi muito legal.
</details>
</details>


<details>
  
<summary><h3>Mês 07/2022</h3></summary>
<details>
   <summary>02/07/2022</summary>

* Solucionei o exercício 094. Foi muito divertido resolver ele, apesar de quebrar um pouco a cabeça. A primeira parte que foi de escrever o programa em si, foi até facil, fazendo as validações e tudo mais.

* Na hora de imprirmir os resultados foi que quebrei um pouco mais a cabeça, foi bom que aprendi sozinho uma forma diferente da que o prof. Guanabara ensina e gostei de fazê-lo dessa forma, por isso até permaneci desse jeito.
</details>

<details>
   <summary>13/07/2022</summary>
   
* Assisti a aula 20 do mundo 3 do curso em vídeo, muito bom aprendi sobre funções sem parâmetros, com parâmetros e com listas.
    * Segue link para [Aula 20](<https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/funcoes-em-python/modulos/funcoes-parte-1/>)

* Compartilhando o aprendizado...
    * Para criar uma função basta chamar o método <code>def()</code>, simples assim e assim criar diversas *rotinas* que o programa irá te ajudar fazer.

* Função sem Parâmetros: Para chamar uma função sem parâmetros, basta chamar o método <code>def()</code>, descrever o nome da função, colocar os <code>()</code> e abaixo e aninhado (identado), programar a função a ser criada. Ex:
        
```python
IN[]

def lin():
print('-' * 30)
# O Python pede duas linhas após as funções


lin()
print('  THIAGO PINTO É BOM ')
lin()

OUT[]
------------------------------
  THIAGO PINTO É BOM 
------------------------------
```

* Função *com* Parâmetros: Para chamar uma função com parâmetros, basta chamar o método <code>def</code>, descrever o nome da função, colocar os <code>()</code> onde dentro dele estará o nome do parâmetro a ser colocado na função ex: <code>(txt)</code> e abaixo e aninhado (identado), programar a função a ser criada. Ex:
        
        
```python

IN[]


def título(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


título('   THIAGO É MUITO BOM!    ')

OUT[]
------------------------------
   THIAGO É MUITO BOM!    
------------------------------
```

* outros exemplos de parâmetros são:
    
```python
IN[]


def soma(a, b):
    s = a + b
    print(s)


# Programa Principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(b=3, a=18)  # Pode-se inclusive indicar qual é cada parâmetro, inclusive sem seguir a ordem de parâmetros criada na função.

"""# soma(4)"""  # Essa função dará erro, pois a função criada, pede dois parâmetros "(a, b) e foi colocado somente 1 "4".


OUT[]

9
17
3
21
```

```python
IN[]

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B é: {s}')
    print(s)


# Programa Principal
soma(b=4, a=5)

OUT[]
A = 5 e B = 4
A soma de A + B é: 9
9
```

* Podemos também empacotar funções (coisa que várias linguagens não fazem) onde a única diferença da forma anterior é somente colocar um "*" antes do nome do parâmetro como nos exemplos abaixo.

```python
IN[]

def contador(* núm):
    print(núm)


contador(5, 6, 9)
contador(3, 2, 1)
contador(9, 8, 5, 1, 3, 8, 7)

OUT[]

(5, 6, 9)
(3, 2, 1)
(9, 8, 5, 1, 3, 8, 7)

```

```python
IN[]

def contador(* núm):
    for valor in núm:
        print(f'{valor} | ', end='')
    print('FIM!')


contador(5, 6, 9)
contador(3, 2, 1)
contador(9, 8, 5, 1, 3, 8, 7)

OUT[]
5 | 6 | 9 | FIM!
3 | 2 | 1 | FIM!
9 | 8 | 5 | 1 | 3 | 8 | 7 | FIM!
```

```python
IN[]
def contador(* núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} eles tem o tamanho de {tam} números.')


contador(5, 6, 9)
contador(3, 2, 1, 0)
contador(9, 8, 5, 1, 3, 8, 7)

OUT[]
Recebi os valores (5, 6, 9) eles tem o tamanho de 3 números.
Recebi os valores (3, 2, 1, 0) eles tem o tamanho de 4 números.
Recebi os valores (9, 8, 5, 1, 3, 8, 7) eles tem o tamanho de 7 números.
```

* Função com listas: Essas funções vão ser bastante úteis, visto que nas formas anteriores, os resultados das funções saem como tuplas. Porém da forma abaixo, elas saem como lista o que pode ser interessante para criar diversas funções bem específicas. veja alguns exemplos.
    
    
```python
IN[]
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

OUT[]
[12, 6, 18, 2, 0, 4]
```

```python
IN[]

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores{valores}, temos {s}.')


soma(5, 2)
soma(2, 9, 4)


OUT[]

Somando os valores(5, 2), temos 7.
Somando os valores(2, 9, 4), temos 15.
```

* Aproveitei o embalo e já fiz o exercício 096 que foi bastante intuitivo, pois agora tenho que me forçar a pensar na forma de criação das funções e seuas interações.
</details>

<details>
   <summary>15/07/2022</summary>

* Na resolução do exercício 97, fiz um pouco diferente do prof. Guanabara, mas a forma dele foi mais inteligente.
* No exercício 98, comecei até bem, porém, não tive os insights para terminar o exercício sozinho. Tive que olhar a solução do professor. Apesar de serem soluções que já aprendi, vejo que tenho que buscar a pensar mais como fatiar cada processo que o programa tem que fazer e observar mais qual string deve vir primeiro e suas corretas indentações. Mas no geral, sei que tive a idéia correta. Só não consegui implementar.

</details>

<details>
   <summary>23 e 25/07/2022</summary>

* Após alguns dias sem estudar e já sofrendo abstinência, no dia 23/07 decidi fazer o exercício 99 sem relembrar a aula 20, pois queria trabalhar um pouco minha memória. Como não consegui compreender a montagem inicial da solução do exercício, tive dificuldades e decidi no dia 23 mesmo ver a resposta e fazer junto com o professor. Pode observar que tentei, pois partes do script que fiz está diferente do professor pois reaproveitei o que eu já havia produzido.
* No dia 25, decidi recriar o exercício (99b) para tentar fazer sem olhar buscando fazer do meu jeito. Como comecei tarde, acabei não criando a funcionalidade sleep pois identifiquei que na versão que estou utilizando do pyhton (2022.1.3) ainda persiste a inconsistencia na biblioteca dentro da função conforme dito pelo professor. Como já tem quase um ano do vídeo criado, começo a me perguntar... Será que é uma inconsistencia mesmo?

</details>
</details>

<details>
<summary><h3>Mês 08/2022</h3></summary>

<details>
   <summary>09/08/2022</summary>

* Retornei aos estudos novamente já resolvendo o exercício 100. Porém para resolvê-lo precisei relembrar a aula 20 e daí foi fácil, foi só jogar as funções na tela e correr pro abraço.
* Aproveitei já assisti a aula 21 que ficou bem cumprida e vou tentar resumir a aula aqui amanhã no meu horário de almoço.
* Já criei também os exercícios 101 a 106 para começar a fazer também nessa semana.
</details>

<details>
   <summary>22/08/2022</summary>

* Sim... Estou devendo o resumo da aula 21, mas vou repassar para vocês assim que possível, pois não quero fazer somente colando aqui no corpo do README, quero fazer com todas as imagens e detalhes que vocês merecem.
* Resolvi as aulas 101 a 103 hoje aproveitando mais um momento de enfermidade que tive (já aproveitei e tomei uma benzetacil pra resolver de vez isso. Caso não saiba o que é, veja um vídeo do Thiago Ventura no youtube, é bem engraçado o jeito dele falar da experiência que ele teve ao tomá-la também).
CHEEEGAAAA de enrolação, bora pras observações.
    * Ex101 - Consegui fazê-lo com tranquilidade porém eu havia me esquecido de como utilizar a função <code>date</code> após a importação da biblioteca <code>datetime</code>, depois que relembrei assistindo a parte do vídeo onde demonstrava, pausei, e daí executei o exercício e vi que havia dado tudo certo. Sabia no fundo que esse era o único erro.
    * ex102 - Resolvi sozinho, Um desafio que tive, foi entender que o show vem como padrão <code>True</code> depois de fazer alguns testes, entendi que tem que começar com <code>False</code> e daí beleza. O único problema é que me faltou criatividade ao final em descrever na formula finalizando o total da fatoração com o símbolo de "=". Mas a formula estava OK também. Muito legal.
    * ex103 - Tive duas situações, primeiro que barrei na questão do número de gols não aceitar o 0, portanto, depois de quebrar um pouco a cabeça, decidi olhar a forma de resolver o exercício e aí comprendi e uma coisa me chamou a atenção, vi que o professor Guanabara não chamou a função <code>ficha()</code> dele. Aliás, corrijo aqui o que eu estava escrevendo, vi sim que ele chamou a função <code>ficha()</code> quando estava validando a variável <code>n</code>. A outra situação é que eu não consegui fazer com que o parâmetro "desconhecido" no meu parâmetro <code>nome_jogador()</code> ficasse como opicional já com a descrição "<desconhecido>".
OBS: Será que estou ficando preguiçoso demais ao estudar olhando diretamente o resultado no vídeo do respectivo exercício? Acho que eu deveria "googlar" mais ao invés de buscar o resultado no exercício. Puxando na memória aqui... Eu fazia isso com mais afinco no início, agora eu faço sim, porém com menos perseverança.
</details>

 <details>
 <summary>26/08/2022</summary>

* Resolvi os exercícios 104 a 106 aproveitando uma folga no serviço.
   * Ex104 - Consegui resolver, porém assistindo a resposta do exercício. O Conceito em si, eu consegui fazer mas não dava a resposta de forma satisfatória, por isso decidi assistir o vídeo.
   * Ex105 - Eu estava tentando fazer o exercício construindo as formulas e com isso, tive dificuldades em concluir o exercício. Para verificar onde estava errando, eu busquei assistir o vídeo da resposta e pude verificar que o professor estava fazendo de forma bem mais simples. Parei de assistir o vídeo ainda no início (quano identifiquei a proposta do professor) e concluí daí pra frente. Foi satisfatório também apesar de ter assistido a resposta.
   * Ex106 - Consegui chegar ao resultado final, porém, quanto a colocar as perfumarias, foi bom relembrar (quero criar aqui um repositório somente com informações e dicas de como usar as cores com o código ANSI para que no futuro eu possa usar quando necessário e deixar colaborativo com quem nos acompanha.
</details>

<details>
<summary>27 e 28/08/2022</summary>

* Assiti a aula 22, a qual já vou compartilhar aqui com vocês e resolução do exercício 107.

   <details>
   <summary><h4>MODULARIZAÇÃO</h4></summary>
   Trata-se de dividir o programa em módulos de forma a possibilitar sua melhor compreensão em leitura, bem como também sua manutenção, dividindo-o em várias partes (vários módulos).

   Um exemplo simbólico disso é quando precisamos criar um programa como o abaixo.

   ```Python
   def fatorial(n):
       f = 1
       for c in range(1, n+1):
           f *= c
       return f


   def dobro(n):
       return n * 2


   def triplo(n):
       return n * 3


   num = int(input("Digite um valor: "))
   fat = fatorial(num)
   print(f'O fatorial de {num} é {fat}.')
   print(f'O dobro de {num} é {dobro(num)}.')
   print(f'O triplo de {num} é {triplo(num)}.')
   ```

   Ocorre que o programa fica um pouco grande e para melhor dividi-lo, foi decidido que teremos que separar as funções em outro módulo.

   Com isso, basta criar um novo arquivo com extensão *.py, nomear o arquivo como por exemplo “uteis.py”, colocar as funções nela e no arquivo do programa principal, importar as funções usando o método <code>import</code>.

   Com isso as funções também deverão ser renomeadas conforme abaixo.

   * Arquivo programa principal
   ```Python
   import uteis

   num = int(input("Digite um valor: "))
   fat = uteis.fatorial(num)
   print(f'O fatorial de {num} é {fat}.')
   print(f'O dobro de {num} é {uteis.dobro(num)}.')
   print(f'O triplo de {num} é {uteis.triplo(num)}.')
   ```

   * Arquivo “uteis.py”
   ```Python
   def fatorial(n):
       f = 1
       for c in range(1, n+1):
           f *= c
       return f


   def dobro(n):
       return n * 2


   def triplo(n):
       return n * 3
   ```
   
   * É importante também ressaltar que podemos usar o método <code>from [nome do módulo] import [nome da função]</code> para que se possa importar somente as funções necessárias e não custar memória de processamento de todo o módulo como somente na função <code>import</code>
   </details>
   
   <details>
   <summary><h4>PACOTES</h4></summary>
   Os pacotes nada mais são que pastas para que armazenam modulações de forma a organizá-las como por exemplo, dividi-las por assunto conforme imagem abaixo.
   
   ![image](https://user-images.githubusercontent.com/91860056/187089210-96645293-e831-412e-a94e-ed3312518f90.png)
   
   Com isso, podemos organiza-los melhor:
   
   ![image](https://user-images.githubusercontent.com/91860056/187089273-1427ef97-3ca2-4809-b67e-2f205c1c1400.png)
   
   E para os pacotes, em sua maioria, teremos que ter os arquivos "__init__.py" em cada um deles conforme demonstrado abaixo.
   
   ![image](https://user-images.githubusercontent.com/91860056/187089295-d3c94e6c-3492-436c-a680-b34dc1e86327.png)

* Ex107 - Criei as pastas conforme recomendado pelo professor Guanabara (Por isso, excluí o arquivo anterior denominado (ex.107.py).
![image](https://user-images.githubusercontent.com/91860056/187089571-c3bfd8e4-34c9-43e2-899b-0504b0c17827.png)

   Resolvi o exercício com facilidade, criei até mais funções para praticar. Contudo, eu havia criado cada função já com a função <code>return</code> com a formula, direto e objetivo. Mas, como o professor orientou a criar a variável <code>res</code> (já visualizando soluções futuras) já fiz o devido ajuste conforme orientado.
      
</details>
</details>

<details>
<summary><h3>Mês 09/2022</h3></summary>

<details>
<summary>03/09/2022</summary>

* Ex 108 a 112 - Resolvi os exercícios praticamente tudo em uma pancada, pois como o conteúdo não foi dificil, na verdade foi bem exemplificativo, tive somente que ir acompanhando com as aulas pois como um era sequencia do outro e como o professor Guanabara recomendou no exercício 107 (resolvido no dia 28/08/22) que uma das funções serviriam para as demais, acabei fazendo juntamente com a resolução, de forma que assim que entendi a idéia, resolvi o exercício e já deixei pronto de forma somente a fazer alguns ajustes finos conforme o professor nos repassou. Quero ver se amanhã eu já assisto a aula 23 e já faço o resumo para nós.
</details>

<details>
<summary>05/09/2022</summary>

* Ex 113 a 115 - Resolvi os exercícios, porém estou muito empolgado com o exercício 115. Este exercício, tenho certeza que vou praticá-lo várias vezes, buscando idéias diferentes para poder compreender bem todos os conteúdos aplicados. Vou até listar algumas idéias: Criar agenda telefônica, Cadastro de produtos, Controle de contratos e Controle de processos.
</details>

<details>
<summary>11/09/2022</summary>

* 115 - Resolvi todo o exercício, fazendo algumas melhorias. Para resolver, antes de começar a codar, assisti as aulas 115 a, b e c umas 2 vezes para resolver. Tive que fazer olhando quando tinha dúvidas que foram poucas (basicamente em detalhes mesmo) pois entendi a idéia. Levei bastante tempo para resolver mas achei todo o curso muito legal.
Parabéns ao professor Gustavo Guanabara e toda a equipe do Curso em Vídeo. Muito obrigado por compartilhar o conhecimento de vocês que Deus os abençoe.
</details>

</details>
