import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.curdir, '../../../../')))

import logging
import webview

from contextlib import redirect_stdout
from io import StringIO
from server import server

logger = logging.getLogger(__name__)
stream = StringIO()
with redirect_stdout(stream):
    window = webview.create_window('My first pywebview application', server)
    print('WINDOW IS CREATED')
    webview.start(debug=True)

if __name__ == '__main__':
    pass
    # stream = StringIO()
    # with redirect_stdout(stream):
    #     window = webview.create_window('My first pywebview application', server)
    #     print('WINDOW IS CREATED')
    #     webview.start(debug=True)
