from src.account.exceptions import InsufficientBalanceException


def register_exception_handler(app):
    @app.errorhandler(InsufficientBalanceException)
    def insufficient_funds(e):
        err = {
            "error": "Insufficient Funds"
        }

        return err, 400
