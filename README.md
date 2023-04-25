# Task Management API for danbiedu
## DB Schema
- <a href="https://dbdiagram.io/d/644774ae6b31947051248964">ERD</a>
- 변경 내용
  - `team` 테이블
    - 메타 데이터로 관리하기 위해 별도의 테이블로 생성 하였습니다.
  - `task` 테이블
    - `is_deleted` & `deleted_at`: soft delete 구현을 위해 task 와 subtask 테이블에 해당 필드 추가 하였습니다.
  - `subtask` 테이블
    - `is_deleted` & `deleted_at`: soft delete 구현을 위해 task 와 subtask 테이블에 해당 필드 추가 하였습니다.
    - `task_id` : task 생성 시 subtask를 설정할 수 있어 외래키 관계로 설정하였습니다.

## 프로젝트 구조
```shell
.
├── common
│         ├── models.py
│         └── permissions.py
├── config
│         ├── settings.py
│         └── urls.py
├── task
│         ├── migrations
│         ├── models.py
│         ├── serializers.py
│         ├── urls.py
│         └── views.py
├── tests
│         ├── conftest.py
│         ├── fixtures
│         └── test_task.py
├── user
│         ├── models.py
│         └── serializers.py
├── manage.py
├── pytest.ini
├── load_fixtures.sh
├── README.md
└── requirements.txt
```
- `common` : 프로젝트 전반에 공통으로 사용 되는 모듈입니다.
- `config` : 프로젝트 전체 세팅에 대한 내용이 있는 모듈입니다.
- `task`   : `task management`의 주요 기능이 있는 모듈입니다.
- `test`   : 테스트 코드가 있는 모듈입니다.
  - `fixtures` : 테스트 전반에 사용 되는 데이터가 있는 모듈입니다.
- `user`   : 회원과 관련된 기능이 있는 모듈입니다.
- `pytest.ini` : 유닛테스트는 pytest를 이용하였습니다.
- `load_fixtures.sh` : dump data를 DB에 입력하는 스크립트 입니다.

## 실행
### 실행 환경
- Python 3.11.1

### 환경 준비
```shell
python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

export SECRET_KEY={SECRET_KEY}
```

### dump 데이터 준비
```shell
chmod +x load_fixtures.sh
./load_fixtures.sh
```
- `password`는 `username`과 동일 (ex. username: test, password: test)

### 개발 서버
```shell
python manage.py runserver
```
- API 문서 : http://127.0.0.1:8000/swagger/

### 테스트 실행
```shell
pytest -v
```