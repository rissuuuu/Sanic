from sanic import Sanic
from sanic.response import json

app = Sanic("My Hello, world app")
# app.ctx.db=Databse()

@app.route('/')
async def test(request):
    return json({'hello': 'world'})

@app.route('/name')
async def test1(request):
    return json({'name':'rishav'})

if __name__ == '__main__':
    app.run()