create schema if not exists `fatec_api`;
use `fatec_api`;

/* TABELA DO USUARIO */

create table if not exists `fatec_api`.`usuario` (
	`user_id` int not null auto_increment,
    `user_email` varchar (80) not null,
    `user_nome` varchar (255) not null,
    `user_senha` varchar (20) not null,
    `confirmacao` tinyint default 0,
    primary key (user_id),
    unique index `user_email_unique` (`user_email` asc) visible
);

select * from usuario;

/* TABELA DO CURSO */

create table if not exists `fatec_api`.`curso` (
	`cur_id` int not null,
    `cur_nome` varchar (80),
    primary key (cur_id)
);

select * from curso;

/* TABELA DA RELACAO ENTRE USUARIO E CURSO */

create table if not exists `fatec_api`.`participa` (
	`cur_id` int,
    `user_id` int not null,
    constraint `fk_cur_id_2`
		foreign key (`cur_id`)
        references `curso`(`cur_id`),
	constraint `fk_user_id`
		foreign key (`user_id`)
        references `usuario`(`user_id`)
        
);

select * from participa;

/* TABELA DE PERMISSOES */

create table if not exists `fatec_api`.`permissoes` (
	`per_id` int not null,
    `per_desc`varchar (250),
    primary key (per_id)
);

/* TABELA DE CARGOS */

create table if not exists `fatec_api`.`cargo` (
	`car_id` int not null,
    `car_nome` varchar (20) not null,
    `per_id` int not null,
    primary key (car_id),
    constraint `fk_per_id`
		foreign key (`per_id`)
        references `permissoes`(`per_id`)
);

select * from cargo;

/* TABELA DA RELACAO ENTRE USUARIO E CARGO */

create table if not exists `fatec_api`.`exerce` (
	`car_id` int not null,
	`user_id` int not null,
    constraint `fk_car_id_2`
		foreign key (`car_id`)
        references `cargo`(`car_id`),
	constraint `fk_user_id_3`
		foreign key (`user_id`)
        references `usuario`(`user_id`)
);

select * from exerce;

/* TABELA DE REGISTRO */

create table if not exists `fatec_api`.`registro` (
	`user_rm` int not null,
    `car_id` int not null,
    primary key (user_rm),
    unique index `user_rm_unique` (`user_rm` asc) visible,
    constraint `car_id_3`
		foreign key (`car_id`)
        references `cargo`(`car_id`)
	
);

select * from registro;

/* TABELA DE FUNCIONARIO */

create table if not exists `fatec_api`.`funcionario` (
	`user_id` int not null,
    `user_rm` int not null,
	unique index `user_rm_unique` (`user_rm` asc) visible,
    constraint `user_id_7`
		foreign key (`user_id`)
        references `usuario`(`user_id`),
	constraint `user_rm` 
		foreign key (`user_rm`)
        references `registro`(`user_rm`)
);

select * from funcionario;

create table if not exists `fatec_api`.`coordena`(
	`user_id` int not null,
    `cur_id` int not null,
	constraint `fk_user_id_6`
		foreign key (`user_id`)
        references `usuario`(`user_id`),
    constraint `fk_cur_id_3`
		foreign key (`cur_id`)
        references `curso`(`cur_id`)
);

select * from coordena;

/* TABELA DO FEED */ 

create table if not exists `fatec_api`.`feed` (
	`post_id` int not null auto_increment,
    `post_titulo` varchar (150) not null,
    `post_assunto` varchar (150) not null,
    `post_data` datetime not null,
    `post_anexo` longblob null,
    `post_mensagem` text not null,
    `post_remetente` varchar (80) not null,
    `car_nome` varchar (200) not null,
	primary key (post_id)
);

select * from feed;

/* TABELA DA RELACAO ENTRE USUARIO E FEED */

create table if not exists `fatec_api`.`publica` (
	`user_id` int not null,
    `post_id` int not null,
    constraint `fk_user_id_5`
		foreign key (`user_id`)
        references `usuario`(`user_id`),
	constraint `fk_post_id`
		foreign key (`post_id`)
        references `feed`(`post_id`)
);

select * from publica;

/* TABELA DE MENSAGENS RECEBIDAS */

create table if not exists `fatec_api`.`recebe` (
	`post_id` int not null,
    `cur_id` varchar (4) not null,
    constraint `fk_post_id_2`
		foreign key (`post_id`)
        references `feed`(`post_id`)
);

select * from recebe;

/* TABELA DE MENSAGENS ARQUIVADAS */

create table if not exists `fatec_api`.`arquivado` (
	`post_id` int not null,
	`user_id` int not null,
    constraint `fk_post_id_3`
		foreign key (`post_id`)
        references`feed`(`post_id`),
	constraint `fk_user_id_2`
		foreign key (`user_id`)
        references `usuario`(`user_id`)
);

select * from arquivado