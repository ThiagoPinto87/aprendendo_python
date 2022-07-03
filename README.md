<h6 align="center"> 🚧 Atualmente em produção 🚧 </h6>
<h1> Aprendendo Python </h1>

Estou iniciando os estudos em programação.
Já hávia iniciado o curso sobre HTML e CSS _(mesmo sabendo que são linguagens de marcação)_ pois eu estava querendo ter como próximo passo aprender Java Script. Porém, ao pesquisar sobre a linguagem de programação, um colega de trabalho comentou comigo sobre o Python e fui buscar informações e foi onde eu decidi que ele me ajudaria bastante nos objetivos de minha carreira profissional conforme exposto na bio.
<a> Este curso estou fazendo através do site: <https://www.cursoemvideo.com/>.</a>

<h2>Diário de Aprendizagem</h2>

---


<h3>Em 03/06/2022</h3>

* Aprendi como subir finalmente do PyCharm para o GitHub, eu havia feito sem querer inicialmente, mas agora entendi como funciona a ferramenta.
* Aprendi a estilizar um pouco melhor o GitHub para ficar mais amigável aos parceiros que quiserem colaborar comigo. _(Sejam todos bem vindos)_


<h3>Em 04/06/2022</h3>

* Por não ter conseguido resolver o exercício 86 e 87 tão satisfatóriamente quanto eu gostaria, eu decidi reassistir às aulas 17 e 18 do curso em vídeo. (Assisti também alguns exercícios pois dentro dos exercícios às vezes o professor insere informações importantes.)
    * Aula 17: [link para a aula](<https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/listas-em-python/modulos/listas-parte-1/>)
    * Aula 18: [link para a aula](<https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/listas-em-python/modulos/listas-parte-2/>)
* Entendi que meu erro no exercício 86 foi de não deixar preparada a variável "matriz_numeros" já com os números zerados, devendo serem só substituídos. Pois por mais que o professor guanabara tivesse dito, eu tentei (teimosamente) inserir as informações com o método <code>.append()</code>, visto que eu não havia preenchido a variável com "0".
* Foi importante também que por falta de praticar a manipulação de string's eu havia esquecido como deixar um resultado da forma como eu quero como por exemplo o resultado ser em 5 caractéres e centralizado, usando o comando <code>:^5</code>.


<h3>Em 08/06/2022</h3>

* No final de semana do dia 04/06, fiquei bastante ruim com uma gripe muito forte. Até suspeitei de COVID, mas graças a Deus o resultado foi negativo para a doença mas vamos lá, sem chorumelas!
* Na atualização de hoje é que fui cair na real que a variável <code>matriz_numeros[l][c]</code> onde <code>[l][c]</code> trata-se dos respectivos índices dos valores da variável. Depois que entendi isso ficou mais fácil, mesmo assim, precisei assistir o vídeo da resolução do exercício mais uma vez para consertar alguns erros. Identifiquei também que cada vez que faço comentários sobre cada passo, consigo absorver melhor o conhecimento do que estou fazendo.
* Estou também apendendo e mexer no aplicativo notion do site <notion.so>, muito bacana. Dá pra fazer muita coisa nele!


<h3>Em 18/06/2022</h3>

* Fiquei bastante dia sem estudar e isso me deixou muito triste comigo mesmo, me mantenho empenhado em aprender, porém, a desculpa dessa vez foi a visita de meu pai que chegou de viagem e como vejo ele poucas vezes no ano, dei prioridade a ele.
* Hoje finalizei os exercícios 088 e 089. Fiquei bravo comigo mesmo pois percebi que fiz o exercício 088 mais copiando do que de fato aprendendo, sorte a minha que me exijo bastante comentando cada string o que me ajuda a absorver as informações.
* No Exercício 088: Apesar de copiar, pode reparar que fiz ao meu modo o que deu um toque de originalidade. Eu havia me esquecido do detalhe em fazer a cópia da lista que usa o serguinte termo <code>[:]</code>. Isso é muito importante na manipulação das listas. Esse termo quer dizer cópia e se assemelha bastante à manipulação de strings onde ao ter uma string qualquer com uma informação, podemos colocar que queremos do índice 3 até o índice 5 <code>[3:5]</code> ou do índice 4 até o final da string <code>[4:]</code>.
* No Exercício 089: Pode observar que fiz ao meu modo, onde gostei mais da minha solução à solução do prof. Guanabara, pois pude praticar mais a manipulação das listas e, mesmo que na lista composta dele tenha uma lista a mais, eu conseguiria inseri-la com facilidade. Só não fiz por não me parecer lógico criá-la (sei que se trata de exercício, mas achei que dessa forma pratiquei mais).
* Gostei também de relembrar a manipulação das strings, visto que tenho quase "toc" por ver tabelas desorganizadas. 
```Python
print(f'{i:<4}{a[0]:<15}{a[3]:>4.1f}')
```


<h3>Em 20/06/2022</h3>

* Hoje consegui somente assistir a aula 19 do curso de Python do curso em vídeo, fiz diversas anotações das quais vou compartilhar com vocês aqui embaixo.


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


<h3>Em 25/06/2022</h3>

* Hoje somente criei os exercícios, nem tentei executá-los pois tive um dia bastante corrido e gostaria de ao menos ter deixado isso pronto hoje. Sei que foi bastante rapido, porém, me comprometo no próximo commit ter um progresso melhor.


<h3>Em 26/06/2022</h3>

* Na resolução dos exercícios de hoje, fiz com facilidade o exercício 090, porém o 091 tive dificuldades pois além do professor ensinar um novo import, eu estava tentando criar dicionários com nome e jogo para depois inserir no dicionário, como não consegui, tentei fazer como na explicação da aula 19 e fazer como lista, porém, sem sucesso.
Mas pude perceber que não é o caminho totalmente errado, pois no import do <code>operator</code>, ele tranforma o dicionário em lista, pois inicialmente o prof. Guanabara até chegou de orientar a colocar o "ranking" como dicionário e o <code>operator</code> transformou o dicionário em lista. Com isso, me despertou a curiosidade de fazer como eu estava imaginando, bater um pouco a cabeça e tentar concluir o exercício como fiz inicialmente e depois usar o método <code>sort()</code> na lista de cada jogada.


<h3>Em 28/06/2022</h3>

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

<h3>Em 02/07/2022</h3>

* Solucionei o exercício 094. Foi muito divertido resolver ele, apesar de quebrar um pouco a cabeça. A primeira parte que foi de escrever o programa em si, foi até facil, fazendo as validações e tudo mais.

* Na hora de imprirmir os resultados foi que quebrei um pouco mais a cabeça, foi bom que aprendi sozinho uma forma diferente da que o prof. Guanabara ensina e gostei de fazê-lo dessa forma, por isso até permaneci desse jeito.
