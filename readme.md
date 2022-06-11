Django 프로젝트 실행 방법
=========================

## 1. 가상환경 실행하기
    source myvenv/Scripts/activate

## 2. 필요 라이브러리 설치하기
    pip install -r requirements.txt

### 만약 위의 명령어 실행 시 오류가 발생한다면
    pip install django
    pip install django-allauth
    pip install pillow
### 를 순서대로 입력해줍니다.

## 3. 프로젝트 폴더 디렉토리(zoonggoMarket)로 이동
    cd zoonggoMarcket

## 4. 데이터 migration하기
    python manage.py makemigrations
    python manage.py migrate
### 을 순서대로 입력해줍니다.

## 5. 로컬 서버 실행하기
    python manage.py runserver