"""
A sample Hello World server.
"""
import os
import requests

from flask import Flask, render_template

import ms_pb2
import ms_pb2_grpc
import grpc

# pylint: disable=C0103
app = Flask(__name__)


def get_metadata(item_name):
    metadata_url = 'http://metadata.google.internal/computeMetadata/v1/'
    headers = {'Metadata-Flavor': 'Google'}
    
    try:
        r = requests.get(metadata_url + item_name, headers=headers)
        return r.text
    except:
        return 'Unavailable'


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    message = "Frontend Server"
    helloservice = os.getenv('HELLO_SERVICE_ADDR')
    channel = grpc.insecure_channel(helloservice)
    stub = ms_pb2_grpc.HelloStub(channel)
    response = stub.SayHello(
         ms_pb2.SayHelloRequest(name=message)
    )
    channel.close()
    project = get_metadata('project/project-id')


    return render_template('index.html',
        message=message,
        hellomessage=response.message,
        Project=project)


@app.route('/health')
def health():
    return "Healthy"

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')

if __name__ == '__main__':
    app.debug = True
    app.run()
