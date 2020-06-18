DROP SCHEMA IF EXISTS `carteira-global.challenge.db`;

CREATE SCHEMA `carteira-global.challenge.db` DEFAULT CHARACTER SET utf8;
USE `carteira-global.challenge.db`;

CREATE TABLE `carteira-global.challenge.db`.`fii` (
	id int(11) not null auto_increment,
    ticker varchar(10) not null,
	nome_fundo varchar(50) not null,
	setor varchar(20) not null,
	preco_atual float not null,
	variacao_dia float not null,
	ultimo_dividendo float not null,
	ultimo_dy float not null,
	var_cota_ipo float not null,
	var_cota_div_ipo float not null,
	p_vp float not null,
	percent_em_caixa float not null,
	numero_cotistas int not null,
	patrimonio float not null,
	liquidez_diaria float not null,
	favoritar tinyint not null default 0,
    
    primary key(id)
) ENGINE = InnoDB;
