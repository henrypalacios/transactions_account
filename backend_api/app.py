from flask import Flask
from flask_cors import CORS

from src.http.routes import account_routes, transaction_routes
from src.http.exception_handler import register_exception_handler
from src.account.repository import InMemoryAccountRepository


def create_app(testing_repo: InMemoryAccountRepository = None) -> Flask:
    app = Flask(__name__)
    
    app.account_repo = InMemoryAccountRepository.build() if not testing_repo else testing_repo
    CORS(app, resources={r"/*": {"origins": "*"}})
    account_routes(app)
    register_exception_handler(app)
    transaction_routes(app)

    return app 


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args= parser.parse_args()
    port = args.port

    app = create_app()

    app.run(host="0.0.0.0", port=port, threaded=True)
