#!/usr/bin/env python3
"""TODO docs
"""

import json

from klein import Klein

CSVFILE  = './data.csv'
PORT     = 8500

app = Klein()

@app.route('/', methods=['POST'])
def save(request):
    request.setHeader('Content-Type', 'application/json')

    data = json.loads(request.content.read().decode('utf-8'))
    return json.dumps({'success': True})

@app.route('/', methods=['GET'])
def get(request):
    return "blah"


resource = app.resource()

if __name__ == '__main__':
    app.run(endpoint_description=r'tcp6:port={}:interface=\:\:'.format(PORT))  # bind to v6 and v4
