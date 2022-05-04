import member_dao as dao


def set_data():  # 한건 insert
    result = dao.insert_one(username="hong", password="1234")
    print(f"result : {result}")


def get_datas():  # 전체 가져오기 select
    my_members_entity = dao.select_all()
    print(my_members_entity)


def get_data():  # 한건 가져오기 select
    my_member_entity = dao.select_one(id=1)
    print(my_member_entity)


def update_data():  # 한건 업데이트하기
    result = dao.update_one(id=1, username="kkk", password="4321")
    print(f"result : {result}")


def delete_data():  # 한건 삭제하기
    result = dao.delete_one(id=1)
    print(f"result : {result}")
