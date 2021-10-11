-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema api_fatec
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema api_fatec
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `api_fatec`;
USE `api_fatec` ;

-- -----------------------------------------------------
-- Tabela com informações do usuário
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `api_fatec`.`usuario` (
  `id_usuario` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(80) NOT NULL,
  `senha` VARCHAR(255) NOT NULL,
  `nome` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `api_fatec`.`curso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `api_fatec`.`curso` (
  `id_curso` INT NOT NULL AUTO_INCREMENT,
  `nome_curso` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id_curso`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Tabela com informações da mensagem
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `api_fatec`.`feed` (
  `id_feed` INT NOT NULL AUTO_INCREMENT,
  `assunto` VARCHAR(50) NOT NULL,
  `remetente` VARCHAR(50) NOT NULL,
  `titulo` VARCHAR(80) NOT NULL,
  `destinatario`  VARCHAR(100) NOT NULL,  
  `mensagem` TEXT NOT NULL,
  `anexo` LONGBLOB NULL,
  `data_inclusao` DATE NOT NULL,
  `curso_id` INT NOT NULL,
  PRIMARY KEY (`id_feed`),
  INDEX `fk_curso_idx` (`curso_id` ) VISIBLE,
  CONSTRAINT `fk_curso`
    FOREIGN KEY (`curso_id`)
    REFERENCES `api_fatec`.`curso` (`id_curso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Tabelas para futura estrutura de Hierarquias
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `api_fatec`.`perfil` (
  `id_perfil` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `pode_cadastrar_usuarios` TINYINT NOT NULL DEFAULT 0,
  `pode_cadastrar_feed` TINYINT NOT NULL DEFAULT 0,
  `pode_cadastrar_cursos` TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY (`id_perfil`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Tabelas para futura estrutura de Hierarquias
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `api_fatec`.`usuario_perfil` (
  `usuario_id` INT NOT NULL,
  `perfil_id` INT NOT NULL,
  PRIMARY KEY (`usuario_id`, `perfil_id`),
  INDEX `fk_perfil_idx` (`perfil_id` ASC) VISIBLE,
  CONSTRAINT `fk_usuario`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `api_fatec`.`usuario` (`id_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_perfil`
    FOREIGN KEY (`perfil_id`)
    REFERENCES `api_fatec`.`perfil` (`id_perfil`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Tabela para destinatarios
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `api_fatec`.`destinatario_feed` (
  `id_destinatario_feed` INT NOT NULL AUTO_INCREMENT,
  `perfil_destinatario_id` INT NOT NULL,
  `feed_id` INT NOT NULL,
  PRIMARY KEY (`id_destinatario_feed`),
  INDEX `fk_feed_idx` (`feed_id` ASC) VISIBLE,
  INDEX `fk_perfil_idx` (`perfil_destinatario_id` ASC) VISIBLE,
  CONSTRAINT `fk_feed`
    FOREIGN KEY (`feed_id`)
    REFERENCES `api_fatec`.`feed` (`id_feed`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_perfil_destinatario`
    FOREIGN KEY (`perfil_destinatario_id`)
    REFERENCES `api_fatec`.`perfil` (`id_perfil`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- INSERINDO CURSOS ATUAIS --

insert into curso values(null, 'Análise e Desenvolvimento de Sistemas');
insert into curso values(null, 'Banco de Dados');
insert into curso values(null, 'Desenvolvimento de Software Multiplataforma');
insert into curso values(null, 'Gestão da Produção Industrial');
insert into curso values(null, 'Logística');
insert into curso values(null, 'Manufatura Avançada');
insert into curso values(null, 'Manutenção de Aeronaves');
insert into curso values(null, 'Projetos de Estruturas Aeronáuticas');

select * from usuario;
select * from curso;
select * from feed;
SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

