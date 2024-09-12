import os
from strawberry.asgi import GraphQL
from fastapi import FastAPI
from app.controllers.graphql.schema import schema


def serve():
    app = FastAPI()
    graphql_app = GraphQL(schema)
    app.add_route("/graphql", graphql_app)

    return app


if __name__ == "__main__":
    import uvicorn

    app = serve()
    uvicorn.run(
        app,
        host=os.getenv("SERVICE_GRAPHQL_HOST", "0.0.0.0"),
        port=int(os.getenv("SERVICE_GRAPHQL_PORT", 8000)),
    )
