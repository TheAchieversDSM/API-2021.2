use fatec_api;

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

/* INSERINDO PERMISSOES */

insert into permissoes (per_id, per_desc) values (1, 'Total');
insert into permissoes (per_id, per_desc) values (2, 'Professores & Alunos');
insert into permissoes (per_id, per_desc) values (3, 'Alunos');
insert into permissoes (per_id, per_desc) values (4, 'Nenhuma');

select * from permissoes;

/* INSERINDO CARGOS */

insert into cargo (car_id, car_nome, per_id) values (1, 'Diretor', 1);
insert into cargo (car_id, car_nome, per_id) values (2, 'Coordenador', 2);
insert into cargo (car_id, car_nome, per_id) values (3, 'Secretaria', 1);
insert into cargo (car_id, car_nome, per_id) values (4, 'Professor', 3);
insert into cargo (car_id, car_nome, per_id) values (5, 'Alunos', 4);

select * from cargo;

/* INSERINDO INFORMAÇÕES DO ADMINISTRADOR */

insert into usuario (user_id, user_email, user_nome, user_senha, confirmacao) values (1, 'adm@fatec.sp.gov.br', 'Administrador', 'fatec', 1);
insert into exerce (car_id, user_id) values (1, 1);
insert into exerce (car_id, user_id) values (2, 1);
insert into exerce (car_id, user_id) values (3, 1);

insert into participa (cur_id,user_id) values (2, 1);
insert into participa (cur_id,user_id) values (3, 1); 