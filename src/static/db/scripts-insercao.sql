use api_fatec;

insert into perfil (id_perfil, nome, pode_cadastrar_usuarios, pode_cadastrar_feed, pode_cadastrar_cursos) values(NULL, 'ADMINISTRADOR', 1, 1, 1);
insert into perfil (id_perfil, nome, pode_cadastrar_usuarios, pode_cadastrar_feed, pode_cadastrar_cursos) values(NULL, 'SECRETARIA ACADÊMICA', 0, 1, 0);
insert into perfil (id_perfil, nome, pode_cadastrar_usuarios, pode_cadastrar_feed, pode_cadastrar_cursos) values(NULL, 'PROFESSOR', 0, 1, 0);
insert into perfil (id_perfil, nome, pode_cadastrar_usuarios, pode_cadastrar_feed, pode_cadastrar_cursos) values(NULL, 'ALUNO', 0, 0, 0);
select * from perfil;

insert into usuario (id_usuario, nome, email, senha) values (null, 'Gizeli Martins Fonseca', 'gizeli.fonseca@fatec.sp.gov.br', '12345678');
insert into usuario_perfil values((select id_usuario from usuario where email = 'gizeli.fonseca@fatec.sp.gov.br'), (select id_perfil from perfil where nome = 'ADMINISTRADOR') );
insert into usuario_perfil values((select id_usuario from usuario where email = 'gizeli.fonseca@fatec.sp.gov.br'), (select id_perfil from perfil where nome = 'ALUNO') );

insert into curso values(null, 'Desenvolvimento de Softwares Multiplataforma');
insert into curso values(null, 'Logística');
insert into curso values(null, 'Banco de Dados');

select u.nome "Nome do Usuário", u.email "E-Mail do Usuário", p.nome "Nome do Perfil"
	from usuario u inner join usuario_perfil up inner join perfil p 
     on up.usuario_id=u.id_usuario and up.perfil_id = p.id_perfil;

select * from curso;
