-- 1ª Query (Quais as operadoras que tiveram mais despesas ... no último trimestre)

SELECT rc.reg_ans, rc.razao_social, COALESCE(rc.nome_fantasia, '') AS nome_fantasia, rc.endereco_eletronico, sq.saldo_total FROM 
    -- Agrupa dados que contém a descriação baseado no reg_ans e soma saldo_final
	(SELECT 
	 	reg_ans,
		ROUND(SUM(CAST(REPLACE(dc.vl_saldo_final, ',', '.') AS numeric)), 2) AS saldo_total
	FROM demonstracoes_contabeis dc
	WHERE dc.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR ' AND data_reg >= '2021-10-01'
	GROUP BY dc.reg_ans) AS sq
INNER JOIN relatorio_cadop AS rc ON rc.reg_ans = sq.reg_ans
ORDER BY saldo_total DESC
LIMIT 10;


-- 2ª Query (Quais as operadoras que tiveram mais despesas ... no último ano)

SELECT rc.reg_ans, rc.razao_social, COALESCE(rc.nome_fantasia, '') AS nome_fantasia, rc.endereco_eletronico, sq.saldo_total FROM 
	(SELECT 
	 	reg_ans,
		ROUND(SUM(CAST(REPLACE(dc.vl_saldo_final, ',', '.') AS numeric)), 2) AS saldo_total
	FROM demonstracoes_contabeis dc
	WHERE dc.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR ' AND data_reg >= '2020-01-01'
	GROUP BY dc.reg_ans) AS sq
INNER JOIN relatorio_cadop AS rc ON rc.reg_ans = sq.reg_ans
ORDER BY saldo_total DESC
LIMIT 10;