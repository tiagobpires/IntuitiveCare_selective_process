import json

from flask import Blueprint, jsonify, request
from pydantic import BaseModel
from spectree import Response

from factory import api
from models import RelatorioCadop, RelatorioResponse, RelatorioResponseList

relatorio_cadop_controller = Blueprint(
    "relatorio_cadop_controller", __name__, url_prefix="/search"
)


class SearchModel(BaseModel):
    reg_ans: int = ""
    cpnj: str = ""
    razao_social: str = ""
    numero: str = ""
    cnpj: str = ""
    complemento: str = ""
    bairro: str = ""
    cidade: str = ""
    uf: str = ""
    cep: str = ""
    ddd: str = ""
    telefone: str = ""
    fax: str = ""
    endereco_eletronico: str = ""
    representante: str = ""
    cargo_representante: str = ""
    data_registro_ans: str = ""


@relatorio_cadop_controller.get("/")
@api.validate(query=SearchModel, resp=Response(HTTP_200=RelatorioResponseList))
def search():
    """Search in database"""

    reg_ans = request.args.get("reg_ans", "")
    cnpj = request.args.get("cnpj", "")
    razao_social = request.args.get("razao_social", "")
    modalidade = request.args.get("modalidade", "")
    numero = request.args.get("numero", "")
    complemento = request.args.get("complemento", "")
    bairro = request.args.get("bairro", "")
    cidade = request.args.get("cidade", "")
    uf = request.args.get("uf", "")
    cep = request.args.get("cep", "")
    ddd = request.args.get("ddd", "")
    telefone = request.args.get("telefone", "")
    fax = request.args.get("fax", "")
    endereco_eletronico = request.args.get("endereco_eletronico", "")
    representante = request.args.get("representante", "")
    cargo_representante = request.args.get("cargo_representante", "")
    data_registro_ans = request.args.get("data_registro_ans", "")

    list_relatorios = RelatorioCadop.query.filter(
        RelatorioCadop.razao_social.ilike(f"%{razao_social}%"),
        RelatorioCadop.modalidade.ilike(f"%{modalidade}%"),
        RelatorioCadop.numero.ilike(f"%{numero}%"),
        RelatorioCadop.complemento.ilike(f"%{complemento}%"),
        RelatorioCadop.bairro.ilike(f"%{bairro}%"),
        RelatorioCadop.cidade.ilike(f"%{cidade}%"),
        RelatorioCadop.uf.ilike(f"%{uf}%"),
        RelatorioCadop.cep.ilike(f"%{cep}%"),
        RelatorioCadop.ddd.ilike(f"%{ddd}%"),
        RelatorioCadop.telefone.ilike(f"%{telefone}%"),
        RelatorioCadop.fax.ilike(f"%{fax}%"),
        RelatorioCadop.endereco_eletronico.ilike(f"%{endereco_eletronico}%"),
        RelatorioCadop.representante.ilike(f"%{representante}%"),
        RelatorioCadop.cargo_representante.ilike(f"%{cargo_representante}%"),
        RelatorioCadop.data_registro_ans.ilike(f"%{data_registro_ans}%"),
        RelatorioCadop.reg_ans.ilike(f"%{reg_ans}%"),
        RelatorioCadop.cnpj.ilike(f"%{cnpj}%"),
    ).all()

    response = RelatorioResponseList(
        relatorios=[
            RelatorioResponse.from_orm(relatorio).dict()
            for relatorio in list_relatorios
        ]
    ).json()

    return jsonify(json.loads(response)), 200
