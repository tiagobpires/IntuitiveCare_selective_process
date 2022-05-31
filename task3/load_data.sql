-- Carrega dados do relatório cadop
COPY relatorio_cadop 
FROM PROGRAM 'more +2 C:\Users\Home\Desktop\Tiago\IntuitiveCare_selective_process\task3\archives\Relatorio_cadop_teste_3.csv'
DELIMITER ';'
ENCODING 'LATIN1'
CSV HEADER;

-- Utiliza plpgsql para iterar na lista dos arquivos do 1º Trimestre de 2020 ao 3º de 2021

DO
$do$
DECLARE
    documents TEXT[]:= array ['1T2020', '1T2021', '2T2020', '2T2021', '3T2020', '3T2021', '4T2020'];
    document_name TEXT;
    path_document TEXT;
BEGIN
    FOREACH document_name in array documents
    LOOP
        path_document := 'C:\Users\Home\Desktop\Tiago\IntuitiveCare_selective_process\task3\archives\' || document_name || '.csv';
		
		EXECUTE format('
			COPY demonstracoes_contabeis (data_reg, reg_ans, cd_conta_contabil, descricao, vl_saldo_final)
			FROM ''%s''
			DELIMITER '';''
			CSV HEADER
			ENCODING ''LATIN1''
			QUOTE ''"'' ', path_document);
    END loop;
END
$do$;

-- O último relatório de 2021 possui uma coluna a mais

-- Criação de uma tabela temporária para receber dados
CREATE TEMPORARY TABLE temp_demonstracoes_contabeis(
    data_reg date,
    reg_ans integer,
    cd_conta_contabil integer,
    descricao text,
    vl_saldo_inicial text,
    vl_saldo_final text
);

COPY temp_demonstracoes_contabeis 
FROM 'C:\Users\Home\Desktop\Tiago\IntuitiveCare_selective_process\task3\archives\4T2021.csv'
DELIMITER ';'
CSV HEADER
QUOTE '"';

-- Insere dados na tabela demosntracoes_contabeis retirando coluna não necessária
INSERT INTO demonstracoes_contabeis (data_reg, reg_ans, cd_conta_contabil, descricao, vl_saldo_final)
SELECT data_reg, reg_ans, cd_conta_contabil, descricao, vl_saldo_final
	FROM temp_demonstracoes_contabeis;