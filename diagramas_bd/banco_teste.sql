TRUNCATE TABLE "Contratos", "Alugueis", "Imoveis", "Inquilinos", "Proprietarios";

INSERT INTO "Proprietarios" ("id", "nome", "data_de_nascimento")
VALUES 
	('1', 'caio', '18/12/1996'),
	('2', 'augusto', '18/12/1996');

INSERT INTO "Inquilinos" ("id", "nome", "data_de_nascimento")
VALUES 
	('1', 'oiac', '12/08/1969'),
	('2', 'otsugua', '12/08/1969');

INSERT INTO "Imoveis" ("id", "logradouro", "cep", "bairro", "cidade")
VALUES
	('1', 'Rua que sobe', '00000000', 'Centro', 'Udi'),
	('2', 'Rua a outra', '12345678', 'Canto', 'Berlandia');

INSERT INTO "Alugueis" ("id", "imovel", "proprietario")
VALUES ('1', '1', '1');
