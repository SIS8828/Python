#플라스크 임포트

from flask import Flask
from flask import request


# 플라스크 앱을 생성합니다.
app = Flask(__name__)

# 편의를 위한 디버그 모드를 활성화합니다.
app.debug = True

# URL 경로에 따라 실행할 함수에 데코레이터를 사용합니다.
# 데코레이터의 파라미터는 URL 경로입니다.

@app.route("/")

# 위경로에 접근하면 실행할 합수 입니다.
def hello():
    return "hello, World!!!"

@app.route("/hello/<name>")     # <name> 자리에 오는 문자열은 name에 할당되어
                                                # 함수로 전달
def hello_to(name):
    return "Hello, {0}".format(name)

@app.route("/hello")
def hello_to_get_param():
    #/hello?name=hong 와 같은 형식의 요청을 받아서
    # ?name=<이름>의 값이 오면, <이름>을 name에 저장.
    name = request.args.get("name")
    return "Hello, {0}".format(name)

# 이 파일을 바로 실행할 때 함께 실핼할 코드를 적습니다.
if __name__ == "__main__":
    #위에서 생성한 플라스크 어플리케이션을 실행합니다.
    app.run()

