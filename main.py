from sanic import Sanic
from sanic.response import text

app = Sanic("HorseRace")


@app.get("/api/v1/")
async def predict(request):
    # TODO: haven't finish
    """API @route: /api/
    - process request body
    - prediction logics
    - response
    """
    return text("Test")
