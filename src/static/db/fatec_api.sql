create schema if not exists `fatec_api`;
use `fatec_api`;

/* TABELA USUARIO */

create table if not exists `fatec_api`.`usuario` (
	`user_id` int not null auto_increment,
    `user_email` varchar (80) not null,
    `user_nome` varchar (255) not null,
    `user_senha` varchar (20) not null,
    primary key (user_id)
);

select * from usuario;

/* TABELA DO ATRIBUTO MULTIVALORADO CARGO*/

create table if not exists `fatec_api`.`cargo_user` (
	`car_id` int,
    `user_id` int not null,
    primary key (car_id, user_id),
    constraint `fk_user_id_6`
		foreign key (`user_id`)
        references `usuario`(`user_id`)
);

/* TABELA DO ATRIBUTO MULTIVALORADO TURMA */

create table if not exists `fatec_api`.`turma_user` (
	`tur_id` varchar (4) not null,
    `user_id` int not null,
    primary key (tur_id, user_id),
    constraint `fk_user_id_7`
		foreign key (`user_id`)
        references `usuario`(`user_id`)
);

/* TABELA DA ESPECIALIZACAO ALUNO */ 

create table if not exists `fatec_api`.`aluno` (
	`alu_ra` int not null,
    `user_id` int not null,
    primary key (alu_ra, user_id),
    constraint `fk_user_id` 
		foreign key (`user_id`)
        references `usuario`(`user_id`)
);

/* TABELA DA ESPECIALIZAÇÃO FUNCIONARIO */

create table if not exists `fatec_api`.`funcionario` (
	`fun_rm` int not null,
    `user_id` int not null,
    primary key (fun_rm, user_id),
    constraint `fk_user_id_2`
		foreign key (`user_id`)
        references `usuario`(`user_id`)
);

/* TABELA DO CURSO */

create table if not exists `fatec_api`.`curso` (
	`cur_id` int not null,
    `cur_nome` varchar (80),
    primary key (cur_id)
);

/* TABELA DA TURMA */

create table if not exists `fatec_api`.`turma` (
	`tur_id` varchar (4) not null,
    `tur_semestre` int not null,
    `cur_id` int not null,
    primary key (tur_id),
    constraint `fk_cur_id_2`
		foreign key (`cur_id`)
        references `curso`(`cur_id`)
);

/* TABELA DO RELACAO ENTRE CURSO E TURMA */

create table if not exists `fatec_api`.`pertence` (
	`cur_id` int not null,
    `tur_id` varchar (4) not null,
    primary key (cur_id, tur_id),
    constraint `fk_cur_id`
		foreign key (`cur_id`)
        references `curso`(`cur_id`),
	constraint `fk_tur_id`
		foreign key (`tur_id`)
        references `turma`(`tur_id`)
);

/* TABELA DA RELACAO ENTRE USUARIO E TURMA */

create table if not exists `fatec_api`.`participa` (
	`tur_id`  varchar (4) not null,
    `user_id` int not null,
    `cur_id` int not null,
    primary key (tur_id, user_id),
    constraint `fk_tur_id_2`
		foreign key (`tur_id`)
        references `turma`(`tur_id`),
	constraint `fk_cur_id_3`
		foreign key (`cur_id`)
        references `curso`(`cur_id`)
);

/* TABELA DE CARGOS */

create table if not exists `fatec_api`.`cargo` (
	`car_id` int not null,
    `car_nome` varchar (20) not null,
    `per_id` int not null,
    primary key (car_id)
);

/* TABELA DE PERMISSOES */

create table if not exists `fatec_api`.`permissoes` (
	`per_id` int not null,
    `per_desc`varchar (250),
    primary key (per_id)
);

/* TABELA DA RELACAO ENTRE USUARIO E CARGO */

create table if not exists `fatec_api`.`exerce` (
	`car_id` int not null,
	`user_id` int not null,
    primary key (car_id, user_id),
    constraint `fk_car_id_2`
		foreign key (`car_id`)
        references `cargo`(`car_id`),
	constraint `fk_user_id_3`
		foreign key (`user_id`)
        references `usuario`(`user_id`)
);

/* TABELA DE HISTORICO DE ATIVIDADE */

create table if not exists `fatec_api`.`historico` (
	`hist_id` int not null auto_increment,
    `hist_data_inicio` date,
    `hist_data_fim` date,
    `user_id` int not null,
    primary key (hist_id, user_id),
    constraint `fk_user_id_4`
		foreign key (`user_id`)
        references `usuario`(`user_id`)
);

/* TABELA DO FEED */ 

create table if not exists `fatec_api`.`feed` (
	`post_id` int not null auto_increment,
    `post_assunto` varchar (150) not null,
    `post_data` date not null,
    `tur_id` varchar (4) not null,
    `car_id` int not null,
	primary key (post_id, car_id),
	constraint `fk_car_id_3`
		foreign key (`car_id`)
        references `cargo`(`car_id`)
);

/* TABELA DA RELACAO ENTRE USUARIO E FEED */

create table if not exists `fatec_api`.`interage` (
	`user_id` int not null,
    `post_id` int not null,
    primary key (user_id),
    constraint `fk_user_id_5`
		foreign key (`user_id`)
        references `usuario`(`user_id`),
	constraint `fk_post_id`
		foreign key (`post_id`)
        references `feed`(`post_id`)
)