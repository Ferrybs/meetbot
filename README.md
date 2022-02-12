<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">MEET BOT</h3>

  <p align="center">
    Um bot para fazer presença em salas do google meet!
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Tabela de Conteúdos</summary>
  <ol>
    <li>
      <a href="#sobre">Sobre</a>
      <ul>
        <li><a href="#dependências">Dependências</a></li>
      </ul>
    </li>
    <li>
      <a href="#começando">Começando</a>
      <ul>
        <li><a href="#pré-requisitos">Pré-requisitos</a></li>
        <li><a href="#installation">Instalação</a></li>
      </ul>
    </li>
    <li>
      <a href="#Como-Usar">Como Usar</a>
      <ul>
        <li><a href="#Iniciar">I</a></li>
      </ul>
    </li>
    <li><a href="#conhecimentos">Conhecimentos</a></li>
    <li><a href="#licença">Licença</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## Sobre

Esse é um bot para fins de de estudo. Usando um web driver, acessa uma sala do google meet. Anuncia o início de uma chamada até o cliente para. Coleta o nomes dos usuários que responderam a chamada e faz uma lista de alunos ausentes. Essa lista é postada em uma site que compartilha arquivos em txt. 

### Dependências

Esses foram os frameworks usados no projeto.
* [Selenium](https://selenium-python.readthedocs.io/)


<!-- GETTING STARTED -->
## Começando

Esse é um tutorial de como instalar esse projeto.

### Pré-requisitos

Essa é a lista de comandos para instalar as dependências.
* pip
  ```sh
  pip install selenium
  pip install webdriver-manager
  ```
### Instalação

1. Clone o repo
   ```sh
   git clone https://github.com/Ferrybs/meetbot
   ```
2. Criar um arquivo em `docs/auth.json`
   ```JS
   {
    "meet":"https://meet.google.com/exemplo",
    "path": "diretorio/onde/se/encontra/google-chrome"
    }   
   ```
3. Criar um arquivo em  `docs/alunos.txt` com os nomes dos alunos.
    Separados por `\n`, em uma unica linha. Ou mudar o modo no src.


## Como-Usar

Esse é um totorial de como usar o bot.

### Iniciar

1. Executar o aquivo `src\app\main.py` como adminstrador.
2. O arquivo main contem uma função menu como apenas uma opção. Essa opção inicia o Selenium entra em uma sala do google meet usando as credenciais especificadas aquivo json em `docs/auth.json`. Apos o login, ele pede permissão para entrar na sala e inicia uma chamada usando o arquivo `docs/alunos.txt` como referencia de alunos. Apos o usuario determinar o fim da chamad faz a diferença desse arquivo de aluno e os que responderam a chamada no chat. Envia esse para um site que salva texto e retorna para a chamada onde envia o link do site com o nome dos alunos que não responderam a chamada. 

<!-- LICENSE -->
## Licença

Distributed under the MIT License. See `LICENSE` for more information.

## Conhecimentos
* [Selenium](https://selenium-python.readthedocs.io/)
* [Python](https://docs.python.org/)
* [Design Pattern Strategy](https://refactoring.guru/pt-br/design-patterns/strategy)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[forks-shield]: https://img.shields.io/github/forks/Ferrybs/meetbot.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/Ferrybs/meetbot.svg?style=for-the-badge
[stars-url]: https://github.com/Ferrybs/meetbot/stargazers
[issues-shield]: https://img.shields.io/github/issues/Ferrybs/meetbot.svg?style=for-the-badge
[issues-url]: https://github.com/Ferrybs/meetbot/issues
[license-shield]: https://img.shields.io/github/license/Ferrybs/meetbot.svg?style=for-the-badge
[license-url]: https://github.com/Ferrybs/meetbot/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/felipe-araujo-a0473818b/
