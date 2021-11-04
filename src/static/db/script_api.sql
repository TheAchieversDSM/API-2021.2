use fatec_api;

insert into usuario (user_id, user_nome, user_email, user_senha, confirmacao) values (1, 'Maria Clara', 'm@fatec.sp.gov.br', '1', 1);

/* INSERINDO NOMES DOS CURSOS */

insert into curso (cur_id, cur_nome) values (1, 'Análise e Desenvolvimento de Sistemas');
insert into curso (cur_id, cur_nome) values (2, 'Banco de Dados');
insert into curso (cur_id, cur_nome) values (3, 'Desenvolvimento de Software');
insert into curso (cur_id, cur_nome) values (4, 'Gestão da Produção Industrial');
insert into curso (cur_id, cur_nome) values (5, 'Logística');
insert into curso (cur_id, cur_nome) values (6, 'Manufatura Avançada');
insert into curso (cur_id, cur_nome) values (7, 'Manutenção de Aeronaves');
insert into curso (cur_id, cur_nome) values (8, 'Projetos de Estruturas Aeronáuticas');

select * from curso;

/* INSERINDO CARGOS */

insert into cargo (car_id, car_nome, per_id) values (1, 'Diretor', 1);
insert into cargo (car_id, car_nome, per_id) values (2, 'Coordenador', 2);
insert into cargo (car_id, car_nome, per_id) values (3, 'Secretaria', 1);
insert into cargo (car_id, car_nome, per_id) values (4, 'Professor', 3);
insert into cargo (car_id, car_nome, per_id) values (5, 'Alunos', 4);

select * from cargo;

/* INSERINDO PERMISSOES */

insert into permissoes (per_id, per_desc) values (1, 'Total');
insert into permissoes (per_id, per_desc) values (2, 'Professores & Alunos');
insert into permissoes (per_id, per_desc) values (3, 'Alunos');
insert into permissoes (per_id, per_desc) values (4, 'Nenhuma');

select * from permissoes;

/* INSERINDO TURMAS */

-- ANALISE E DESENVOLVIMENTO DE SISTEMAS
insert into turma (tur_id, tur_semestre, cur_id) values ('ADS1', 1, 1);
insert into turma (tur_id, tur_semestre, cur_id) values ('ADS2', 2, 1);
insert into turma (tur_id, tur_semestre, cur_id) values ('ADS3', 3, 1);
insert into turma (tur_id, tur_semestre, cur_id) values ('ADS4', 4, 1);
insert into turma (tur_id, tur_semestre, cur_id) values ('ADS5', 5, 1);
insert into turma (tur_id, tur_semestre, cur_id) values ('ADS6', 6, 1);

-- BANCO DE DADOS
insert into turma (tur_id, tur_semestre, cur_id) values ('BDD1', 1, 2);
insert into turma (tur_id, tur_semestre, cur_id) values ('BDD2', 2, 2);
insert into turma (tur_id, tur_semestre, cur_id) values ('BDD3', 3, 2);
insert into turma (tur_id, tur_semestre, cur_id) values ('BDD4', 4, 2);
insert into turma (tur_id, tur_semestre, cur_id) values ('BDD5', 5, 2);
insert into turma (tur_id, tur_semestre, cur_id) values ('BDD6', 6, 2);

-- DESENVOLVIMENTO DE SOFTWARE MULTIPLATAFORMA
insert into turma (tur_id, tur_semestre, cur_id) values ('DSM1', 1, 3);
insert into turma (tur_id, tur_semestre, cur_id) values ('DSM2', 2, 3);
insert into turma (tur_id, tur_semestre, cur_id) values ('DSM3', 3, 3);
insert into turma (tur_id, tur_semestre, cur_id) values ('DSM4', 4, 3);
insert into turma (tur_id, tur_semestre, cur_id) values ('DSM5', 5, 3);
insert into turma (tur_id, tur_semestre, cur_id) values ('DSM6', 6, 3);

-- GESTAO DE PRODUCAO INDUSTRIAL
insert into turma (tur_id, tur_semestre, cur_id) values ('GPI1', 1, 4);
insert into turma (tur_id, tur_semestre, cur_id) values ('GPI2', 2, 4);
insert into turma (tur_id, tur_semestre, cur_id) values ('GPI3', 3, 4);
insert into turma (tur_id, tur_semestre, cur_id) values ('GPI4', 4, 4);
insert into turma (tur_id, tur_semestre, cur_id) values ('GPI5', 5, 4);
insert into turma (tur_id, tur_semestre, cur_id) values ('GPI6', 6, 4);

-- LOGISTICA
insert into turma (tur_id, tur_semestre, cur_id) values ('LOG1', 1, 5);
insert into turma (tur_id, tur_semestre, cur_id) values ('LOG2', 2, 5);
insert into turma (tur_id, tur_semestre, cur_id) values ('LOG3', 3, 5);
insert into turma (tur_id, tur_semestre, cur_id) values ('LOG4', 4, 5);
insert into turma (tur_id, tur_semestre, cur_id) values ('LOG5', 5, 5);
insert into turma (tur_id, tur_semestre, cur_id) values ('LOG6', 6, 5);

-- MANUTENCAO AVANCADO
insert into turma (tur_id, tur_semestre, cur_id) values ('MAV1', 1, 6);
insert into turma (tur_id, tur_semestre, cur_id) values ('MAV2', 2, 6);
insert into turma (tur_id, tur_semestre, cur_id) values ('MAV3', 3, 6);
insert into turma (tur_id, tur_semestre, cur_id) values ('MAV4', 4, 6);
insert into turma (tur_id, tur_semestre, cur_id) values ('MAV5', 5, 6);
insert into turma (tur_id, tur_semestre, cur_id) values ('MAV6', 6, 6);

-- MANUTENCAO DE AERONAVES
insert into turma (tur_id, tur_semestre, cur_id) values ('MAE1', 1, 7);
insert into turma (tur_id, tur_semestre, cur_id) values ('MAE2', 2, 7);
insert into turma (tur_id, tur_semestre, cur_id) values ('MAE3', 3, 7);
insert into turma (tur_id, tur_semestre, cur_id) values ('MAE4', 4, 7);
insert into turma (tur_id, tur_semestre, cur_id) values ('MAE5', 5, 7);
insert into turma (tur_id, tur_semestre, cur_id) values ('MAE6', 6, 7);

-- PROJETO DE ESTRUTURAS AERONAUTICAS
insert into turma (tur_id, tur_semestre, cur_id) values ('PEA1', 1, 8);
insert into turma (tur_id, tur_semestre, cur_id) values ('PEA2', 2, 8);
insert into turma (tur_id, tur_semestre, cur_id) values ('PEA3', 3, 8);
insert into turma (tur_id, tur_semestre, cur_id) values ('PEA4', 4, 8);
insert into turma (tur_id, tur_semestre, cur_id) values ('PEA5', 5, 8);
insert into turma (tur_id, tur_semestre, cur_id) values ('PEA6', 6, 8);

select * from turma