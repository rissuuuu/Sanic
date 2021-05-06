from sanic import Sanic
from sanic.response import json

app = Sanic("My Hello, world app")

@app.route('/')
async def test(request):
    return json({'hello': 'world'})

#modified manish


if __name__ == '__main__':
    app.run()