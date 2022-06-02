# READ_ME

![Python](https://img.shields.io/badge/Python-3.10.4-3776AB?logo=Python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14.3-4169E1?logo=PostgreSQL&logoColor=white)
![Heroku](https://img.shields.io/badge/Heroku-7.53.0-430098?logo=Heroku&logoColor=white)
![Keras](https://img.shields.io/badge/keras-2.8.0-D00000?logo=Keras&logoColor=white)
![Numpy](https://img.shields.io/badge/Numpy-1.22.3-013243?logo=Numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-1.4.2-150458?logo=pandas&logoColor=white)
![Psycopg2](https://img.shields.io/badge/Psycopg2-2.9.3-430098)
![Flask](https://img.shields.io/badge/Flask-2.1.2-000000?logo=Flask&logoColor=white)
![Flask-python](https://img.shields.io/badge/Flask_python-3.9.2-000000?logo=Flask&logoColor=white)
![gitdb](https://img.shields.io/badge/gitdb-4.0.9-F050320?logo=Git&logoColor=white)
![jupyter](https://img.shields.io/badge/jupyter_client-7.1.2-F37626?logo=Jupyter&logoColor=white)
![jupyter](https://img.shields.io/badge/jupyter_core-4.9.2-F37626?logo=Jupyter&logoColor=white)
![Kakao](https://img.shields.io/badge/Kakao-Open_builder-FFCD00?logo=KakaoTalk&logoColor=white)


# About

    집플릭스는 무주택자를 위한 대출 상품 조회 및 금리계산서비스를 위한 카카오톡 챗봇서비스를 이용한 프로젝트이다.

    집플릭스는 Database로 PostgreSQL,pgAdmin 와 Webserver로 Heroku, 챗봇툴인 Kakao open builder를 연결시키기 위해 Python로 작성하여 Keras, numpy, pandas, psycopg2, Flask, GitPython 라이브러리를 사용하여 프로젝트가 진행되었다.

# Installation from sources

### Packages

- Installing essential packages in python
    
    `Flask` `pandas` `psycopg2` `numpy` `math` `json`
    

### Requirements.txt

```
	certifi==2021.10.8
	charset-normalizer==2.0.12
	click==8.1.3
	colorama==0.4.4
	et-xmlfile==1.1.0
	Flask==2.1.2
	gunicorn==20.1.0
	idna==3.3
	importlib-metadata==4.11.3
	itsdangerous==2.1.2
	Jinja2==3.1.2
	MarkupSafe==2.1.1
	numpy==1.22.3
	openpyxl==3.0.9
	pandas==1.4.2
	python-dateutil==2.8.2
	pytz==2022.1
	requests==2.27.1
	six==1.16.0
	urllib3==1.26.9
	Werkzeug==2.1.2
	xlrd==2.0.1
	zipp==3.8.0
	psycopg2==2.8.6
```

### How to Use

```python
	git clone
	git clone ~..git

	Install virtual environment
	$ virtualenv venv

	Install library
	$ pip install -r requirements.txt

	Run
	$ python main.py
```
  

# Algorithm

- 대출상품 조회 서비스
    - `search_pro_buy(number01,number02,number03,number04,number05)`
        - 매매 상품 조회에 필요한 값을 argument로 받는다.
            
            number01 - 무주택 세대주 여부
            
            number02 - 연령대
            
            number03 - 혼인여부 및 기간
            
            number04 - 부부합산 연 소득
            
            number05 - 순자산가액
            
        - 각 상품별 조건문에서 argument에 따라 출력될 상품의 번호를 리스트 형태로 저장한다.
        - 연동된 데이터베이스에서 상품 정보를 import한 후, 위의 리스트에 저장된 상품 번호에 해당하는 정보를 문자열로 출력한다.
    - `search_buy()`
        - 카카오톡 챗봇에서 사용자에게 입력받은 값을 json 형태로 불러온 후 value 값을 각 변수에 저장한다.
        - `search_pro_buy`를 호출하고 위의 변수를 argument로 지정한다.
        - 위의 함수의 반환값을 dictinary 형태로 반환한다.
    - `search_pro_borrow(number01,number02,number03,number04,number05)`
        - 전세 상품 조회에 필요한 값을 argument로 받는다.
            
            number01 - 무주택 세대주 여부
            
            number02 - 연령대
            
            number03 - 혼인여부 및 기간
            
            number04 - 부부합산 연 소득
            
            number05 - 순자산가액
            
        - 각 상품별 조건문에서 argument에 따라 출력될 상품의 번호를 리스트 형태로 저장한다.
        - 연동된 데이터베이스에서 상품 정보를 import한 후, 위의 리스트에 저장된 상품 번호에 해당하는 정보를 문자열로 출력한다.
    - `search_borrow()`
        - 카카오톡 챗봇에서 사용자에게 입력받은 값을 json 형태로 불러온 후 value 값을 각 변수에 저장한다.
        - `search_pro_borrow`를 호출하고 위의 변수를 argument로 지정한다.
        - 위의 함수의 반환값을 dictinary 형태로 반환한다.

- 금리계산 서비스
    - `calc_pro_buy(number01,number02,number03,number04)`
        - 매매 대출 상품 별 금리 계산을 위한 값을 argument로 받아주는 함수
        - amount = number01, period = number02, income = number03, method = number04
        - 각 상품의 조건별 우대금리를 데이터 프레임 형태로 저장해 놓은 후, 들어온 값에 따라 우대금리를 반환한다
        - 만기일시상환, 원리금균등상환, 원금균등상환 방식별로 납입금액을 계산한다
        - 결과적으로 대출금액, 대출기간, 상환방법, 적용 금리, 총 이자액을 사용자에 출력해준다
    - `calc_buy()`
        - 카카오톡 챗봇에서 사용자에게 입력받은 값을 json 형태로 불러온 후 value 값을 각 변수에 저장한다.
        - `calc_pro_buy`를 호출하고 위의 변수를 argument로 지정한다.
        - 위의 함수의 반환값을 dictinary 형태로 반환한다.
    - `calc_pro_year(number01,number02,number03,number04,number05)`
        - 전세 대출 상품 별 금리 계산을 위한 값을 argument로 받아주는 함수
        - amount = number01, period = number02, income = number03, method = number04, deposit = number05
        - 각 상품의 조건별 우대금리를 데이터 프레임 형태로 저장해 놓은 후, 들어온 값에 따라 우대금리를 반환한다
        - 만기일시상환, 원리금균등상환, 원금균등상환 방식별로 납입금액을 계산한다
        - 결과적으로 대출금액, 대출기간, 상환방법, 적용 금리, 총 이자액을 사용자에 출력해준다
    - `calc_borrow_year()`
        - 카카오톡 챗봇에서 사용자에게 입력받은 값을 json 형태로 불러온 후 value 값을 각 변수에 저장한다.
        - `calc_pro_year`를 호출하고 위의 변수를 argument로 지정한다.
        - 위의 함수의 반환값을 dictinary 형태로 반환한다.
    - `calc_pro_month(number01,number02,number03)`
        - 월세 대출 상품 별 금리 계산을 위한 값을 argument로 받아주는 함수
        - amount = number01, period = number02, method = number03
        - 각 상품의 조건별 우대금리를 데이터 프레임 형태로 저장해 놓은 후, 들어온 값에 따라 우대금리를 반환한다
        - 만기일시상환, 원리금균등상환, 원금균등상환 방식별로 납입금액을 계산한다
        - 결과적으로 대출금액, 대출기간, 상환방법, 적용 금리, 총 이자액을 사용자에 출력해준다
    - `calc_borrow_month()`
        - 카카오톡 챗봇에서 사용자에게 입력받은 값을 json 형태로 불러온 후 value 값을 각 변수에 저장한다.
        - `calc_pro_month`를 호출하고 위의 변수를 argument로 지정한다.
        - 위의 함수의 반환값을 dictinary 형태로 반환한다.

# Connecting Database

- Postgre SQL 에 Import 되어진 데이터베이스를 Heroku와 연동하는 부분이다.
    
    ```python
    db=psycopg2.connect(host='ec2-52-86-115-245.compute-1.amazonaws.com',dbname='d6b5cq66b2ua5t',user='wtpphkajtmedfy',password='*************************',port=5432)
        cursor = db.cursor()
        cursor.execute('SELECT * FROM realzip')
        rows=cursor.fetchall()
    ```
    
    <postgre SQL에 탑재된 사용자 DB의 host,dbname,user,password 를 parameter로 하는 connect() 함수를 이용하여 Heroku와 연동시켜준다.>
    
- 위의 코드로 사용자의 db에 연동이 된다면, heroku sever를 통해, postgre SQL 에 탑재된 데이터를 자유자재로 이용 할 수 있다. 이후, Kakaotalk open builder를 통해 사용자의 input 을 제공받아, database를 이용하였다.
    
    ![Untitled](https://github.com/jmj3047/zipfilx-home/blob/master/README/Untitled.png)
    

# Sever

- heroku server의 main.py에 작성한 코드들을 카카오톡 오픈빌더 서비스와 연결하는 부분이다.
    
    ```python
    @app.route('/api/search_borrow', methods=['POST'])
    def search_borrow():
    ...
        return responseBody
    ```
    
    ‘/api/search_borrow’ 부분이 함수의 해당 url이며 카카오톡 스킬서버에 연결할 핵심이 된다.
    
- heroku에 로그인 후 해당 프로젝트의 settings> Domain을 보면 기본 url을 얻을 수 있다.
- [https://your_project_name.herokuapp.com/](https://your_project_name.herokuapp.com/)이 기본 형태이고 카카오톡에 업로드 할때는 
스킬서버에 먼저 url([https://your_project_name.herokuapp.com/](https://your_project_name.herokuapp.com/)api/search_borrow) 올리고
    
    ![Untitled](https://github.com/jmj3047/zipfilx-home/blob/master/README/Untitled%201.png)
    
- 답변을 원하는 해당 시나리오 블록의 파라미터 설정에서 저장한 스킬을 선택해준다.
    
    ![Untitled](https://github.com/jmj3047/zipfilx-home/blob/master/README/Untitled%202.png)
    
- 그리고 봇 응답에서 스킬데이터 사용을 눌러주면 된다.
    
    ![Untitled](https://github.com/jmj3047/zipfilx-home/blob/master/README/Untitled%203.png)
