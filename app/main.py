from flask import Flask, request
import json

app = Flask(__name__)

##메인 로직
# def cals(opt_operator, number01, number02):
#     if opt_operator == "addition":
#         return number01 + number02
#     elif opt_operator == "subtraction": 
#         return number01 - number02
#     elif opt_operator == "multiplication":
#         return number01 * number02
#     elif opt_operator == "division":
#         return number01 / number02
def cals(opt_operator, number01, number02):
    if opt_operator == "+":
        return number01 + number02
    elif opt_operator == "-": 
        return number01 - number02
    elif opt_operator == "*":
        return number01 * number02
    elif opt_operator == "/":
        return number01 / number02


@app.route('/api/calCulator', methods=['POST'])
def calCulator():
    body = request.get_json()
    print(body)
    params_df = body['action']['params']
    print(type(params_df))
    opt_operator = params_df['operators']
    number01 = json.loads(params_df['sys_number01'])['amount']
    number02 = json.loads(params_df['sys_number02'])['amount']

    print(opt_operator, type(opt_operator), number01, type(number01))

    answer_text = str(cals(opt_operator, number01, number02))

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer_text
                    }
                }
            ]
        }
    }

    return responseBody


def search_pro(number01,number02,number03,number04,number05):
    p1 = "주택도시기금 디딤돌 대출"
    p2 = "주택도시기금 신혼부부전용 구입자금"
    p3 = "오피스텔 구입자금"
    p4 = "한국주택금융공사 보금자리론"
    p5 = "한국주택금융공사 디딤돌대출"
    p6 = "신혼부부전용 전세자금"
    p7 = "버팀목전세자금"
    p8 = "중소기업취업청년 전월세 대출"
    p9 = "청년전용 보증부월세대출"
    p10 = "청년전용 버팀목전세자금(일반)"
    p11 = "주거안정월세대출(일반)"
    p12 = "주거안정월세대출(우대/취준생)"
    p13 = "주거안정월세대출(우대/사회초년생)"
    p14 = "청년전용 버팀목전세자금(신혼/다자녀/2자녀가구)"
    
    q1 = number01
    q2 = number02
    q3 = number03
    q4 = number04
    q5 = number05
    
    print(q1,q2,q3,q4,q5, type(q1))
    
    
    if q1 in [1,2] and q2 in [2,3] and q3 in [2,3] and q4 in [2] and q5 in [1,2]:
        return p1+'\n'
    if q1 in [1,2] and q2 in [2,3] and q3 in [2] and q4 in [2] and q5 in [2]:
        return p2+'\n'
    if q1 in [1,2] and q2 in [2,3] and q3 in [2,3] and q4 in [2] and q5 in [2]:
        return p3+'\n'
    if q1 in [1,2,3] and q2 in [1,2] and q3 in [1,2] and q4 in [3] and q5 in [1,2,3]:
        return p4+'\n'
    if q1 in [1,2] and q2 in [2,3] and q3 in [2] and q4 in [2] and q5 in [1,2,3]:
        return p5+'\n'
    if q1 in [1] and q2 in [2,3] and q3 in [2] and q4 in [2] and q5 in [1]:
        return p6+'\n'
    if q1 in [1] and q2 in [2,3] and q3 [1,2,3] and q4 in [1] and q5 in [1]:
        return p7+'\n'
    if q1 in [1,2] and q2 in [2] and q3 in [1,2,3] and q4 in [1] and q5 in [1]:
        return p8+'\n',p10+'\n'
    if q1 in [1,2] and q2 in [2,3] and q3 in [1,2,3] and q4 in [1] and q5 in [1]:
        return p9+'\n', p11+'\n', p13+'\n'
    if q1 in [1,2] and q2 in [2,3] and q3 in [1] and q4 in [1] and q5 in [1]:
        return p12+'\n'
    if q1 in [1] and q2 in [2,3] and q3 in [2,3] and q4 in [2] and q5 in [1]:
        return p14+'\n'
    else: 
        return "대출상품이 없습니다."
    
    


@app.route('/api/search', methods=['POST'])
def search():
    body = request.get_json()
    print(body)
    params_df = body['action']['params']
    print(type(params_df))
    # opt_operator = params_df['division']
    number01 = json.loads(params_df['sys_number01'])['amount']
    number02 = json.loads(params_df['sys_number02'])['amount']
    number03 = json.loads(params_df['sys_number03'])['amount']
    number04 = json.loads(params_df['sys_number04'])['amount']
    number05 = json.loads(params_df['sys_number05'])['amount']
    print('============================',number01,number02,number03,number04,number05,'============================')
    # print(opt_operator, type(opt_operator), number01, type(number01))

    answer_text = str(search_pro(number01, number02,number03,number04,number05))

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer_text
                    }
                }
            ]
        }
    }

    return responseBody


@app.route('/')
def hello_world():
    return "hello world!"

# 카카오톡 텍스트형 응답
@app.route('/api/sayHello', methods=['POST'])
def sayHello():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])
    print('============================')

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "안녕 hello I'm Ryan"
                    }
                }
            ]
        }
    }

    return responseBody