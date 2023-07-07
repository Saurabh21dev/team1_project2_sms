# main.py
from flask import Flask
from strawberry.flask.views import GraphQLView
from schemas import schema
from database import init_db
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:sql21@localhost:5432/p2_sms"


db=SQLAlchemy(app)
# Initialize the database
init_db()

class StockManagementApp():
    def _init_(self, database_uri):
        self.app = Flask(__name__)
        self.app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

        try:
            init_db(self.app)
        except Exception as e:
            print(f"An error occurred while initializing the database: {str(e)}")

        self.setup_routes()

    def setup_routes(self):
        self.app.add_url_rule(
            "/graphql",
            view_func=GraphQLView.as_view("graphql", schema=schema),
        )

    def run(self):
        try:
            self.app.run()
        except Exception as e:
            print(f"An error occurred while running the application: {str(e)}")

# Define the GraphQL endpoint
app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql_view", schema=schema),
    methods=["GET","POST"],
)

if __name__ == "__main__":
    app.run(debug=True)