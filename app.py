from flask import Flask, request
import requests


app = Flask(__name__)


@app.route('/', methods=('GET', 'POST', 'HEAD', 'PUT', 'PATCH', 'DELETE'))
def hello():
    kwargs = {
        'data': request.form.get(None),
        'headers': {},
    }

    for k, v in request.headers.items():
        kwargs['headers'][k] = v
    kwargs['headers'].update({'Content-Type': 'application/json'})
    kwargs['headers'].pop('Accept-Encoding', None)
    kwargs['headers'].pop('Content-Length', None)
    kwargs['headers'].pop('Host', None)

    resp = requests.post('https://nodered.roach.work/emby-webhooks', **kwargs)

    return (resp.text, resp.status_code, resp.headers.items())


if __name__ == '__main__':
    app.run(host='0.0.0.0')
