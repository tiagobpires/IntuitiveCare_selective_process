-- Armazenamento dos dados do arquivo csv em anexo (relatório cadop)
CREATE TABLE relatorio_cadop(
    reg_ans integer,
    cnpj text,
    razao_social text,
    nome_fantasia text,
    modalidade text,
    logradouro text,
    numero text,
    complemento text,
    bairro text,
    cidade text,
    uf varchar(2),
    cep varchar(10),
    ddd varchar(3),
    telefone varchar(14),
    fax varchar(24),
    endereco_eletronico text,
    representante text,
    cargo_representante text,
    data_registro_ans date,
    PRIMARY KEY (reg_ans)
);

-- Armazenamento dos dados trimestrais
CREATE TABLE demonstracoes_contabeis(
    id SERIAL PRIMARY KEY,
    data_reg date,
    reg_ans integer,
    cd_conta_contabil integer,
    descricao text,
    vl_saldo_final text
);