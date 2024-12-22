from ray import serve
from fastapi import FastAPI

app = FastAPI()


@serve.deployment()
@serve.ingress(app)
class SimpleAPI:
    def __init__(self):
        self.counter = 0

    @app.get("/")
    def hello(self):
        self.counter += 1
        return f"Hello, World! {self.counter}"


ray_app = SimpleAPI.bind()
