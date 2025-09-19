<h1 align="center"; style="font-weight: bold;">FinTrack</h1>

<p>
    <img src="https://img.shields.io/badge/Status-Em_Desenvolvimento-orange" alt="Status = Em Desenvolvimento">
    <img src="https://img.shields.io/badge/Documentação-Em_Andamento-yellow" alt="Documentação: Em Andamento">
    <img src="https://img.shields.io/badge/License-MIT-blue" alt="License = MIT">
</p>

<br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

<p align="center">
    <a href="#sobre">Sobre</a> •
    <a href="#grupo">Integrantes</a> •
    <a href="#requisitos">Requisitos</a> •
    <a href="#diagrama">Entidades</a> •
    <a href="#how-it-works">Funcionamento</a>
</p>

<h2 id="sobre" align="center">Sobre</h2>
Projeto desenvolvido como parte da avaliação da Matéria Programação Orientada a Objetos do curso de Análise e Desenvolvimento de Sistemas na Faculdade Impacta.
O FinTrack é um sistema de controle financeiro onde o usuário poderá realizar a organização de suas finanças, tendo lançamento de gastos e ganhos e as categorias a quais eles pertencem, bem como separação para metas. O programa ainda pode analisar os dados e retornar as categorias que se tem mais gastos e se alguma categoria ultrapassou o limite.

<h2 id="grupo" align="center">Integrantes</h2>
<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/ErickXr.png" width="100" alt="Foto"/><br>
      <b>Erick Xavier Ribeiro</b><br><br>
        <a href="https://www.linkedin.com/in/erick-xavier-0a0b572a9/" target="_blank"><img title="Conecte-se" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Perfil Linkedin"/></a>
        <a href="https://github.com/ErickXr" target="_blank"><img title="Siga-Me" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="Perfil GitHub"/></a>
    </td>
    <td align="center">
      <img src="https://media.licdn.com/dms/image/v2/D4D35AQGsDRT2-i2P3w/profile-framedphoto-shrink_800_800/B4DZjT_bE1GkAg-/0/1755903275706?e=1758765600&v=beta&t=Nf_-BvwZOHRTRn-yq-H2IVusyIsNVRRwVhIa67M77js" width="100" alt="Foto"/><br>
      <b>Gustavo Silva Ferreira</b><br><br>
        <a href="https://www.linkedin.com/in/gustavo-silva-15b681275/" target="_blank"><img title="Conecte-se" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Perfil Linkedin"/></a>
        <a href="" target="_blank"><img title="Siga-Me" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="Perfil GitHub"/></a>
    </td>
    <td align="center">
      <img src="https://github.com/Jloren051.png" width="100" alt="Foto"/><br>
      <b>Julia Lourenço Nogueira</b><br><br>
        <a href="https://www.linkedin.com/in/julia-louren%C3%A7o-8065082ba/" target="_blank"><img title="Conecte-se" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Perfil Linkedin"/></a>
      <a href="https://github.com/Jloren051" target="_blank"><img title="Siga-Me" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="Perfil GitHub"/></a>
    </td>
    <td align="center">
      <img src="https://github.com/LucasAguiarN.png" width="100"  alt="Foto"/><br>
      <b>Lucas Aguiar Nunes</b><br><br>
      <a href="https://www.linkedin.com/in/lucas-aguiar-nunes" target="_blank"><img title="Conecte-se" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Perfil Linkedin"/></a>
      <a href="https://github.com/LucasAguiarN" target="_blank"><img title="Siga-Me" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="Perfil GitHub"/></a>
    </td>
  </tr>
</table>

<h2 id="requisitos" align="center">Requisitos</h2>
Para a utilização do Sistema deve-se instalar a biblioteca sqlalchemy.<br><br>
Comando no Terminal para Instalação:<br>
pip install sqlalchemy

<h2 id="diagrama" align="center">Entidades</h2>

<div align="center">
    <h3>DER</h3>
    <img src="DER.png" alt="DER" width="1000px">
</div>

<div align="center">
    <h3>UML</h3>
    <img src="UML.png" alt="DER" width="1000px">
</div>

<h3>Usuario</h3>
Cifrão da Moeda como Atributo de Classe com Método de Classe para alterar entre "R$" e "U$"<br><br>
Métodos Get e Setter via Property para acessar e alterar Coluna Saldo (Atributo Privado)

<h3>Categoria</h3>
Cifrão da Moeda como Atributo de Classe com Método de Classe para alterar entre "R$" e "U$"<br><br>
Métodos Get e Setter via Property para acessar e alterar Coluna Saldo (Atributo Privado)

<h3>Transacao</h3>
Classe Abstrata para servir de base para Pagamento e Provento<br><br>Cifrão da Moeda como Atributo de Classe com Método de Classe para alterar entre "R$" e "U$"<br><br>
Metodo Abstrato para servir de base para o Método Transacao de Pagamento e Provento

<h3>Pagamento</h3>
Herda de Transacao os atributos e métodos<br><br>
Método de Transacao altera saldo de Usuário e Categoria ou Meta

<h3>Provento</h3>
Herda de Transacao os atributos e métodos<br><br>
Método de Transacao altera saldo de Usuário

<h3>Meta</h3>
Cifrão da Moeda como Atributo de Classe com Método de Classe para alterar entre "R$" e "U$"<br><br>
Métodos Get e Setter via Property para acessar e alterar Coluna Saldo (Atributo Privado)

<h2 id="how-it-works" align="center">Funcionamento</h2>
A interação com o Sistema se deve a Interface, onde o usuário deverá informar a opção desejada conforme o que será exibido.<br>
O Sistema permite Inserir, Atualizar, Consultar e Deletar os dados no Banco de Dados, sendo também possivel alterar a moeda, apenas para fins de visualização.
