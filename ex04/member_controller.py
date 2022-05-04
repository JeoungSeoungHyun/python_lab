# C:\Users\Administrator\AppData\Local\Programs\Python\Python310\Scripts
# python -m pip install flask (경량 웹 프레임워크) (버전에 따라 pip와 pip3를 구분해서 설치해야한다)
# pip가 있는 scripts 폴더까지는 환경변수로 잡혀있지 않기 때문에 python -m 을 사용하여 해당 경로로 이동하여 실행한다?

from flask import Flask, request, jsonify
import member_dao as dao

flask = Flask(__name__)  # import해서 실행하는 건지 그냥 main이 실행하는건지 알려줄수있다?


@flask.route("/my-member")
def list():
    return jsonify(dao.select_all())


@flask.route("/my-member/<id>")
def detail(id):
    return jsonify(dao.select_one(id=id))


@flask.route("/my-member/<id>", methods=["DELETE"])
def delete(id):
    return jsonify(dao.delete_one(id=id))


@flask.route("/my-member/<id>", methods=["PUT"])
def update(id):
    # data = request.data # x-www-form-urlencoded
    data = request.get_json()  # application/json
    # print(f"update call - id : {id}")
    # print("="*50)
    # print(f"data : {data}")
    return jsonify(dao.update_one(id=id, username=data["username"], password=data["password"]))


@flask.route("/my-member", methods=["POST"])
def save():
    data = request.get_json()
    # print(f"save call ")
    # print("="*50)
    # print(f"data : {data}")
    return dao.insert_one(username=data["username"], password=data["password"])


flask.run(
    host="0.0.0.0",  # 0.0.0.0 은 anyone 모든 ip에서 접근 가능한것
    port=5000,  # 기본 포트
    debug=True  # 이 부분이 설정되면 파일 저장시 서버 자동 리로드 된다.
)
