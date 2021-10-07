<br id="inicio">

<h1 align="center">A.P.I - The Achievers</h1>
 <p align="center">
     <a href="#equipe">Equipe</a> • 
     <a href="#sobre">Sobre</a> • 
     <a href="#status">Status</a> • 
     <a href="#tecnologias">Tecnologias</a> • 
     <a href="#execucao">Execução</a> • 
     <a href="#organizacao">Organização</a> • 
     <a href="#user-stories">User Stories</a> • 
     <a href="#prototipo">Protótipo</a>  • 
     <a href="#requisitos">Requisitos</a> • 
     <a href="#backlog-produto">Backlog do Produto</a> • 
     <a href="#backlog-sprints">Backlog das Sprints</a> • 
     <a href="#burndown">Burndown</a>
</p>

<span id="equipe">

### :busts_in_silhouette: Equipe:
Função | Nome 
-------|------
Scrum Master | Evora de Castro
Product Owner | Fernando Satoru Eto
Dev Team | Gizeli Martins Fonseca
Dev Team | Maria Clara Alves de Faria
Dev Team | Mariana Ayumi Tamay
Dev Team | Matheus Henrique Lemes Sakuragui
Dev Team | Rikio Anzai

> Instituição: Fatec São José dos Campos - Prof. Jessen Vidal
> 
> Curso: Desenvolvimento de Software Multiplataforma/1º Semestre

<span id="sobre">

### :mag_right: Sobre o projeto:
<p>Esse projeto está sendo desenvolvido de acordo com os requisitos acordados com o cliente, o qual pediu um portal de informações, tanto para docentes, quanto para discentes, a fim de exibir avisos que seguem um determinado filtro. Os comunicados são visualizados de maneira hierárquica e, devido ao recurso de filtro, a busca por esses será mais sucinta, resolvendo o problema raíz: o grande volume de mensagens recebidas e, consequentemente, perdidas devido à grande procura durante a pandemia do novo Covid-19.</p>
 
 <span id="status">

 ### :bookmark_tabs: Status do projeto: em andamento... :hourglass_flowing_sand:
  
 <span id="tecnologias">

### :computer: Tecnologias utilizadas até o momento:
<p>
    <img src="https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white"></img>
    <img src="https://img.shields.io/badge/Microsoft_Teams-6264A7?style=for-the-badge&logo=microsoft-teams&logoColor=white"></img>
    <img src="https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white"/>
    <img src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white"></img>
    <img src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white"/>
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
    <img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E"/>
    <img src="https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white"/>
    <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/>
</p>
  
↑ [Voltar ao início](#inicio) 
  
<span id="execucao">

### :hammer: Executando a aplicação:
#### Primeiramente, certifique-se se tem o Python, caso não tenha, acesse <a href="https://www.python.org/downloads/">aqui</a> 
```python 
 # Clone este repositório;
 
 # Redirecione-se à pasta referente ao repositório clonado;
 
 # Abra o prompt de comando e confirme se este está com o endereço da pasta correto;
   
 cd API-2021-2
 
 # Instale os requisitos para rodar a aplicação;
   
 pip install -r requirements.txt
 
 # Execute a aplicação;
   
 appy.py
 
 # Acesse o link no qual a aplicação está hospedada;
   
 http://127.0.0.1:5000/
```
 
<span id="organizacao">

### :clipboard: Organização do repositório:
<p> :file_folder: <strong>doc</strong> - pasta que contém o wireframe, tanto para desktop, quanto para mobile;</p> 
<p> | - :open_file_folder: <strong>prototipo</strong> - pasta que contém demonstração do protótipo em arquivos .gif;</p>
<p> | - :open_file_folder: <strong>burndown</strong> - pasta que contém arquivos de demonstração do esforço distribuído pela equipe.</p>
<p> :file_folder: <strong>scr</strong> - pasta que contém duas outras, <em>templates</em> e <em>static</em>;</p>
<p> | - :open_file_folder: <strong>templates</strong> - pasta que contém os códigos de estruturação (.html);</p>
<p> | - :open_file_folder: <strong>static</strong> - pasta que contém outras duas, <em>css</em> e <em>img</em>;</p>
<p> | - - :open_file_folder: <strong>js</strong> - pasta que contém os códigos referentes à javascript (.js);</p>
<p> | - - :open_file_folder: <strong>bd</strong> - pasta que contém tudo referente à parte de banco de dados;</p>
<p> | - - :open_file_folder: <strong>css</strong> - pasta que contém os códigos de estilização (.css);</p>
<p> | - - :open_file_folder: <strong>img</strong> - pasta que contém a logo da FATEC e o favicon, além de outra pasta, <em>footer</em>;</p>
<p> | - - - :open_file_folder: <strong>footer</strong> - pasta que contém todas as imagens utilizadas no rodapé das páginas.</p>
 
↑ [Voltar ao início](#inicio) 
 
<span id="user-stories">

### :pushpin: User Stories:
Quem | Quer | A fim de
-----|------|---------|
Cliente | Priorizar a divulgação de informações da FATEC-SJC | Não ocorrer a perda de informações importantes
Administrador | Privilégios de acesso | Administrar e controlar as permissões de acesso de todos os usuários do sistema
Diretor | Reunir informações por evento | Repassá-las a todos os servidores da unidade
Secretário administrativo | Selecionar informações por curso | Publicar o edital interno das disciplinas do respectivo curso
Secretário acadêmico | Classificar as informações por assunto | Enviá-las para professores e alunos
Coordenador | Organizar as informações por disciplinas | Divulgá-las aos respectivos professores
Professor | Notificar os alunos sobre datas importantes | Informar sobre entregas de atividades e realização de exames
Aluno | Receber informações sobre estágios e palestras | Participar dos processos seletivos e eventos
 
↑ [Voltar ao início](#inicio) 
 
<span id="prototipo">
 
### :memo: Protótipo:
 
Página de login e, caso ainda não o tenha e seja da FATEC, faça seu cadastro.
![](https://media.giphy.com/media/BYBICx6YukGaAZqqRO/giphy.gif?cid=790b7611ca4440f776c0400150e287a10cf07c7f1f4d387c&rid=giphy.gif&ct=g)
 
Página de cadastro com as informações necessárias para aqueles que ainda não são cadastrados no sistema.
![](https://media.giphy.com/media/2x23DaSJyoq0s2WAYs/giphy.gif?cid=790b7611291bb65e552d7b1ffc1159b695db9c22093acc21&rid=giphy.gif&ct=g)
 
Página de feed para usuários sem privilégios, onde pode-se fazer uso de filtros para achar informações mais pertinentes.
![](https://media.giphy.com/media/f0q2ZWO3Bw9KIoaZK3/giphy.gif?cid=790b7611bcb5bdbf9291705864eadd8e56234db63dc3ae73&rid=giphy.gif&ct=g)
 
Página de feed para usuários com função de administrador, onde pode-se fazer uso de filtros para achar informações mais pertinentes.
![](https://media.giphy.com/media/uRrSE6b9nCiwwX7iXJ/giphy.gif?cid=790b76110765ee0b19f368aabdfba3dfa0f6a8ce909fb467&rid=giphy.gif&ct=g)
 
Página para envio de informações, onde são selecionados filtros e desenvolvida a mensagem, bem como o anexo de arquivos.</li>
![](https://media.giphy.com/media/EmS6O8Zoj4J8nvOmRg/giphy.gif?cid=790b76116e7a36c813ba3718131ac0745df329028f5902b5&rid=giphy.gif&ct=g)
 
↑ [Voltar ao início](#inicio) 
 
<span id="requisitos">
 
### :page_with_curl: Requisitos:
Código | Requisitos funcionais 
-------|----------------------
RF. #1 | Envio de informações para divulgação via sistema (Administrador)
RF. #2 | Possibilidade de anexar documentos (e.g.: PDFs, Docs etc.)
RF. #3 | Visualização de informações de divulgação via sistema de modo seletivo (filtro por data, interessados, curso etc.)
RF. #4 | Acesso às informações do sistema através de perfis de usuário/papéis (adm, usuário comum, coordenador de curso etc.)
 
Código | Requisitos Não-Funcionais
-------|---------------------------
RNF. #1 | Desenvolver o back-end com a linguagem Python 3+ e o microframework Flask
RNF. #2 | Utilizar o sistema gerenciador de banco de dados MariaDB/MySQL/PostGresSQL
RNF. #3 | Utilizar HTML-5 para arquitetura da informação da aplicação
RNF. #4 | Utilizar CSS-3 para especificação do layout e demais características de renderização da interface com o usuário
RNF. #5 | Utilizar o GitHub para controle de versão dos artefatos de projeto
RNF. #6 | Interface com navegação intuitiva (e.g.: acesso à informação com poucos "cliques")
RNF. #7 | Sistema responsivo
RNF. #8 | Utilizar JavaScript no front-end (obs: pode fazer uso de framework)
 
↑ [Voltar ao início](#inicio) 
 
<span id="backlog-produto">

### :bar_chart: Backlog do Produto:
Nome da tarefa | Prioridade | Status
---------------|------------|--------
Wireframe da interface de login do status | Alta | Completa
Wireframe da interface de cadastro de usuário | Alta | Completa
Wireframe da interface de divulgação de informações prioritárias | Alta | Completa
Repositório do projeto | Alta | Completa
Documentação do sistema | Alta | Completa
Interface de login do sistema | Alta | Completa
Interface de cadastro de usuário | Alta | Completa
Interface de divulgação de informações prioritárias | Alta | Completa
Outras interfaces conforme solicitação do cliente | Alta | Em andamento
Ajustes na responsividade do sistema | Alta | Em andamento
Tornar o protótipo navegável | Alta | Completa
Ajustes na interface | Alta | Em andamento
Ajustes com JavaScript | Média | Em andamento
Modelos conceitual e lógico do banco de dados | Alta | Não iniciada
Modelo físico do banco de dados | Alta | Não iniciada
Conexão do banco de dados | Alta | Não iniciada
Tornar o protótipo funcional | Alta | Não iniciada
Aplicação do sistema em um servidor de aplicação | Alta | Não iniciada
Testes unitários do sistema | Alta | Não iniciada
Testes de integração | Alta | Não iniciada
Testes de aceitação | Alta | Não iniciada
Melhorias contínuas | Alta | Não iniciada
 
↑ [Voltar ao início](#inicio) 

<span id="backlog-sprints"> 
 
### :chart_with_upwards_trend: Backlog das sprints:

Sprint | Nome da tarefa | Prioridade | Status
-------|----------------|------------|-------
#1 | Wireframe da interface de login do status | Alta | Completa
#1 | Wireframe da interface de cadastro de usuário | Alta | Completa
#1 | Wireframe da interface de divulgação de informações prioritárias | Alta | Completa
#1 | Repositório do projeto | Alta | Completa
#1 | Documentação do sistema | Alta | Completa
#1 | Interface de login do sistema | Alta | Completa
#1 | Interface de cadastro de usuário | Alta | Completa
#1 | Interface de divulgação de informações prioritárias | Alta | Completa
 
Sprint | Nome da tarefa | Prioridade | Status
-------|----------------|------------|-------
#2 | Ajustes na responsividade do sistema | Em andamento
#2 | Tornar o protótipo navegável | Alta | Completa
#2 | Ajustes na interface | Alta | Em andamento
#2 | Ajustes com JavaScript | Média | Em andamento
#2 | Modelo conceitual e lógico do banco de dados | Alta | Completa
#2 | Modelo físico do banco de dados | Alta | Completa
#2 | Conexão do banco de dados | Alta | Completa
#2 | Tornar o protótipo funcional | Alta | Em andamento
#2 | Aplicação do sistema em um servidor de aplicação | Alta | Em andamento

↑ [Voltar ao início](#inicio) 
 
<span id="burndown">
 
### :chart_with_downwards_trend:	Burndown:

#### Primeira Sprint;
 
<p><img src="./doc/burndown/burndown.png"></img></p>
 
↑ [Voltar ao início](#inicio) 
