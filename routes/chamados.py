from flask import Blueprint, jsonify, request
from models.chamado import Chamado
from database import db

chamados_bp = Blueprint("chamados", __name__)


@chamados_bp.post("/chamados")
def criar_chamado():
    data = request.get_json() or {}

    titulo = data.get("titulo")
    descricao = data.get("descricao")

    if not titulo or not descricao:
        return jsonify(error="Campos obrigatórios"), 400

    chamado = Chamado(
        titulo=titulo,
        descricao=descricao
    )

    db.session.add(chamado)
    db.session.commit()

    return jsonify(chamado.to_dict()), 201


@chamados_bp.get("/chamados")
def listar_chamados():
    chamados = Chamado.query.all()
    return jsonify([c.to_dict() for c in chamados])
@chamados_bp.put("/chamados/<int:id>")
def atualizar_status(id):
    data = request.get_json() or {}

    novo_status = data.get("status")

    if not novo_status:
        return jsonify(error="Envie o status"), 400

    chamado = Chamado.query.get(id)

    if not chamado:
        return jsonify(error="Chamado não encontrado"), 404

    chamado.status = novo_status
    db.session.commit()

    return jsonify(chamado.to_dict())
@chamados_bp.delete("/chamados/<int:id>")
def deletar_chamado(id):

    chamado = Chamado.query.get(id)

    if not chamado:
        return jsonify(error="Chamado não encontrado"), 404

    db.session.delete(chamado)
    db.session.commit()

    return jsonify(message="Chamado removido com sucesso")
