CREATE TABLE "Proprietarios"(
    "id" INTEGER NOT NULL PRIMARY KEY,
    "nome" VARCHAR(255) NOT NULL,
    "data_de_nascimento" DATE NOT NULL
);

CREATE TABLE "Imoveis"(
    "id" INTEGER NOT NULL PRIMARY KEY,
    "logradouro" VARCHAR(255) NOT NULL,
    "cep" INTEGER NOT NULL,
    "bairro" VARCHAR(255) NOT NULL,
    "cidade" VARCHAR(255) NOT NULL
);

CREATE TABLE "Alugueis"(
    "id" INTEGER NOT NULL PRIMARY KEY,
    "imovel" INTEGER NOT NULL,
    "proprietario" INTEGER NOT NULL
);

CREATE TABLE "Inquilinos"(
    "id" INTEGER NOT NULL PRIMARY KEY,
    "nome" VARCHAR(255) NOT NULL,
    "data_de_nascimento" DATE NOT NULL
);

CREATE TABLE "Contratos"(
    "id" INTEGER NOT NULL PRIMARY KEY,
    "id_inquilino" INTEGER NOT NULL,
    "id_aluguel" INTEGER NOT NULL
);

ALTER TABLE
    "Alugueis" ADD CONSTRAINT "alugueis_imovel_foreign" FOREIGN KEY("imovel") REFERENCES "Imoveis"("id");
ALTER TABLE
    "Alugueis" ADD CONSTRAINT "alugueis_proprietario_foreign" FOREIGN KEY("proprietario") REFERENCES "Proprietarios"("id");
ALTER TABLE
    "Contratos" ADD CONSTRAINT "contratos_id_aluguel_foreign" FOREIGN KEY("id_aluguel") REFERENCES "Alugueis"("id");
ALTER TABLE
    "Contratos" ADD CONSTRAINT "contratos_id_inquilino_foreign" FOREIGN KEY("id_inquilino") REFERENCES "Inquilinos"("id");
