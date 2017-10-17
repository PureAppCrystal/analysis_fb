from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO

PORT = 8000

REQUEST_MAPPING = {'/graph', 'controller.ex1'}


class TestHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 요청 매핑값 찾기
        index = self.path.find('?')
        req_url = self.path if index == -1 else self.path[:index]
        
        # 요청 매핑값이 graph인지 확인하기
        if req_url != '/graph':
            self.send_error(404, 'File Not Found')
            return

        # 입력받은 파라미터에 따른 함수 처리
        handler_name = 'ex' + self.get_params('ex')
        if handler_name not in TestHTTPRequestHandler.__dict__:
            self.send_error(404, 'File Not Found:' + req_url)
            return

        TestHTTPRequestHandler.__dict__[handler_name](self)
        # print(TestHTTPRequestHandler.__dict__)

    # 파라미터들중 입력받은 값 뽑기
    def get_params(self, name):
        index = self.path.find('?')
        if index == -1:
            return

        qs = self.path[index + 1:]
        params = parse_qs(qs)
        values = params.get(name)

        return None if values is None else values.pop()

    # 파라메터에 대한 출력 
    def ex1(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write("<h1>안녕하십니까, 식사는 하셨셰요?</h1>".encode('utf-8'))

    def ex2(self):
        arr = np.random.normal(5, 3, 500)

        fig, subplots = plt.subplots(2, 1)
        subplots[0].plot(arr, color='red', linestyle='solid')
        subplots[1].hist(arr, bins=20, edgecolor='black', linewidth=1)

        buffer = BytesIO()
        plt.savefig(buffer, dpi=100, bbox_inches='tight')

        self.send_response(200)
        self.send_header('Content-Type', 'image/png')
        self.end_headers()
        self.wfile.write(buffer.getvalue())





# 서버 실행
httpd = HTTPServer(('', PORT), TestHTTPRequestHandler)
print('Server running on port ', PORT)
httpd.serve_forever()
