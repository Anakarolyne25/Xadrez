create database Xadrez;
use xadrez;

create table jogadores (Id INT AUTO_INCREMENT PRIMARY KEY, 
Nome varchar(45));

create table Resultados (Id_Partida INT,
FOREIGN KEY (id_Partida) references Partidas(id)
, Tipo_resultado varchar(45));
 
 create table Partidas_tem_jogadores (Id_Partida INT,
FOREIGN KEY (id_Partida) references Partidas(id),
Id_Jogador1 INT, 
FOREIGN KEY (id_Jogador1) references Jogadores(id),
Id_Jogador2 INT,
FOREIGN KEY (id_Jogador2) references Jogadores(id));

select * from resultados;
insert into resultados (nome) values ('Empate_Tipo_A');
select * from partidas join jogadores on id_ganhador=jogador.id;
select * from partidas;
insert into partidas (id_Resultado) values (1);
 select * from partidas_tem_jogadores;
  insert into partidas_tem_jogadores values (1, 2, 3);
  
 
 select g.nome as ganhador from jogadores g right join partidas on id_ganhador=g.id;
 select * from partidas_tem_jogadores;


create table Partidas (Id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(45),
data datetime);

select * from partidas;
select * from jogadores;

insert into partidas (nome, data) values ('Mate', '2022-12-08');
insert into partidas_tem_jogadores (Id_Partida, Id_Jogador1, Id_Jogador2)values (1,3,4);



use xadrez;

SELECT j.nome as jogador1, j2.nome as jogador2, p.nome as nome_partida, data, Tipo_resultado FROM  Partidas P 
Join Resultados R on r.Id_partida=p.id
join partidas_tem_jogadores PJ on pj.id_partida=p.id
join Jogadores J on id_Jogador1=j.id
join jogadores J2 on id_jogador2=j2.id;
