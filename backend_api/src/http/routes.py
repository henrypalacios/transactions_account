from flask import Response, Flask
from flask import jsonify, abort, make_response, request

from src.http.serialization import get_dto, BaseSchema, get_outDto
from src.account import CreateTransactionInputDto, TransactionId, TransactionOutputDto

def account_routes(app: Flask) :
    @app.route('/', methods=['GET'])
    def get_balance() -> Response:
        
        return make_response(jsonify({}))


def transaction_routes(app: Flask):
    @app.route('/transactions', methods=['GET'])
    def list_transactions():
        result = app.account_repo.list_all()
        if result is None:
            abort(404)

        output_dto = get_outDto(result, TransactionOutputDto, many=True)
          

        return make_response(jsonify(output_dto))

    @app.route('/transactions', methods=['POST'])
    def create_transaction(): 
        input_dto = get_dto(request.get_json(), CreateTransactionInputDto)
        transaction = app.account_repo.save(input_dto)
        output_dto = get_outDto(transaction.__dict__, TransactionOutputDto)

        return make_response(jsonify(output_dto))

    @app.route('/transactions/<string:id>', methods=['GET'])
    def find_transaction(id: TransactionId):
        transaction = app.account_repo.get(id)
        if transaction is None:
            abort(404)

        output_dto = get_outDto(transaction.__dict__, TransactionOutputDto)

        return make_response(jsonify(output_dto))
