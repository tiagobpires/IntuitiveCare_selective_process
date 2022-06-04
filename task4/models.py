from typing import List

from pydantic import BaseModel

from factory import db


class RelatorioCadop(db.Model):
    __tablename__ = "relatorio_cadop"

    reg_ans = db.Column(db.Integer, primary_key=True)
    cnpj = db.Column(db.Text)
    razao_social = db.Column(db.Text)
    nome_fantasia = db.Column(db.Text)
    modalidade = db.Column(db.Text)
    logradouro = db.Column(db.Text)
    numero = db.Column(db.Text)
    complemento = db.Column(db.Text)
    bairro = db.Column(db.Text)
    cidade = db.Column(db.Text)
    uf = db.Column(db.String(2))
    cep = db.Column(db.String(10))
    ddd = db.Column(db.String(3))
    telefone = db.Column(db.String(14))
    fax = db.Column(db.String(24))
    endereco_eletronico = db.Column(db.Text)
    bairro = db.Column(db.Text)
    representante = db.Column(db.Text)
    cargo_representante = db.Column(db.Text)
    data_registro_ans = db.Column(db.Text)

    def __repr__(self) -> str:
        return f"<Registro {self.reg_ans}>"


class RelatorioResponse(BaseModel):
    reg_ans: int = None
    cpnj: str = None
    razao_social: str = None
    numero: str = None
    cnpj: str = None
    complemento: str = None
    bairro: str = None
    cidade: str = None
    uf: str = None
    cep: str = None
    ddd: str = None
    telefone: str = None
    fax: str = None
    endereco_eletronico: str = None
    representante: str = None
    cargo_representante: str = None
    data_registro_ans: str = None

    class Config:
        orm_mode = True


class RelatorioResponseList(BaseModel):
    relatorios: List[RelatorioResponse]
