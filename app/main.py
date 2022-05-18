from flask import Flask, request
import json
import pandas as pd
import math


app = Flask(__name__)

##계산기 로직
def cals(opt_operator, number01, number02):
    if opt_operator == "+":
        return number01 + number02
    elif opt_operator == "-": 
        return number01 - number02
    elif opt_operator == "*":
        return number01 * number02
    elif opt_operator == "/":
        return number01 / number02

#계산기_output
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

#helloworld
@app.route('/')
def hello_world():
    return "hello world!"

# 카카오톡 텍스트형 응답_output
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

   
#매매조회_input
def search_pro_buy(number01,number02,number03,number04,number05):
    p1 = "주택도시기금 디딤돌 대출"
    p2 = "주택도시기금 신혼부부전용 구입자금"
    p3 = "오피스텔 구입자금"
    p4 = "한국주택금융공사 보금자리론"
    p5 = "한국주택금융공사 디딤돌대출"

    
    q1 = number01
    q2 = number02
    q3 = number03
    q4 = number04
    q5 = number05
    
    print(q1,q2,q3,q4,q5, type(q1))
    
    p_lst = []
    if q1 in [1,2] and q2 in [2,3] and q3 in [1,2,3] and q4 in [1,2] and q5 in [1,2]:
        p_lst.append(p1)
    if q1 in [1,2] and q2 in [2,3] and q3 == 2 and q4 in [1,2] and q5 in [1,2]:
        p_lst.append(p2)
    if q1 in [1,2] and q2 in [2,3] and q3 in [1,2,3] and q4 == 2 and q5 == 2:
        p_lst.append(p3)
    if q1 in [1,2,3] and q2 in [2,3] and q3 in [1,2] and q4 in [1,2] and q5 in [1,2,3]:
        p_lst.append(p4)
    if q1 in [1,2] and q2 in [1,2,3] and q3 == 2 and q4 in [1,2] and q5 in [1,2,3]:
        p_lst.append(p5)
    
    if len(p_lst) == 1:
        return f'고객님은 현재 {p_lst[0]} 상품을 대출 받을 수 있습니다.'
    elif len(p_lst) == 2:
        return f'고객님은 현재 {p_lst[0]}, {p_lst[1]} 상품을 대출 받을 수 있습니다.'
    elif len(p_lst) == 3:
        return f'고객님은 현재 {p_lst[0]}, {p_lst[1]}, {p_lst[2]} 상품을 대출 받을 수 있습니다.'
    elif len(p_lst) == 4:
        return f'고객님은 현재 {p_lst[0]}, {p_lst[1]}, {p_lst[2]}, {p_lst[3]} 상품을 대출 받을 수 있습니다.'
    elif len(p_lst) == 5:
        return f'고객님은 현재 {p_lst[0]}, {p_lst[1]}, {p_lst[2]}, {p_lst[3]}, {p_lst[4]} 상품을 대출 받을 수 있습니다.'
    else:
        return "현재 대출 받을 수 있는 상품이 없습니다."
    
    
#매매조회_output
@app.route('/api/search_buy', methods=['POST'])
def search_buy():
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

    answer_text = str(search_pro_buy(number01, number02,number03,number04,number05))

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


#전세조회_input_지원
def search_pro_borrow(number01,number02,number03,number04,number05):
    p6 = "신혼부부전용 전세자금"
    p7 = "버팀목전세자금"
    p8 = "중소기업취업청년 전월세 대출"
    p9 = "청년전용 보증부월세대출"
    p10 = "청년전용 버팀목전세자금"
    p11 = "주거안정월세대출(일반형)"
    p12 = "주거안정월세대출(우대형/취업준비생)"
    p13 = "주거안정월세대출(우대형/사회초년생)"
    p14 = "청년전용 버팀목전세자금(신혼가구,다자녀가구,2자녀가구)"

    
    q1 = number01
    q2 = number02
    q3 = number03
    q4 = number04
    q5 = number05
    
    print(q1,q2,q3,q4,q5, type(q1))
    
    p_lst = []
    if q1 == 1 and q2 in [2,3] and q3 == 2 and q4 in [1,2] and q5 == 1:
        p_lst.append(p6)
    if q1 == 1 and q2 in [2,3] and q3 in [1,2,3] and q4 == 1 and q5 == 1:
        p_lst.append(p7)
    if q1 in [1,2,3] and q2 == 2 and q3 in [1,2,3] and q4 == 1 and q5 == 1:
        p_lst.append(p8)
    if q1 in [1,2,3] and q2 in [2,3] and q3 in [1,2,3] and q4 == 1 and q5 == 1:
        p_lst.append(p9)
    if q1 in [1,2,3] and q2 == 2 and q3 in [1,2,3] and q4 in [1,2] and q5 == 1:
        p_lst.append(p10)
        p_lst.append(p14)
    if q1 in [1,2,3] and q2 == 2 and q3 in [1,2,3] and q4 == 1 and q5 == 1:
        p_lst.append(p11)
        p_lst.append(p12)
        p_lst.append(p13)
    
    if len(p_lst) == 1:
        return f'고객님은 현재 {p_lst[0]} 상품을 대출 받을 수 있습니다.'
    elif len(p_lst) == 2:
        return f'고객님은 현재 {p_lst[0]}, {p_lst[1]} 상품을 대출 받을 수 있습니다.'
    elif len(p_lst) == 3:
        return f'고객님은 현재 {p_lst[0]}, {p_lst[1]}, {p_lst[2]} 상품을 대출 받을 수 있습니다.'
    elif len(p_lst) == 4:
        return f'고객님은 현재 {p_lst[0]}, {p_lst[1]}, {p_lst[2]}, {p_lst[3]} 상품을 대출 받을 수 있습니다.'
    elif len(p_lst) == 5:
        return f'고객님은 현재 {p_lst[0]}, {p_lst[1]}, {p_lst[2]}, {p_lst[3]}, {p_lst[4]} 상품을 대출 받을 수 있습니다.'
    elif len(p_lst) == 6:
        return f'고객님은 현재 {p_lst[0]}, {p_lst[1]}, {p_lst[2]}, {p_lst[3]}, {p_lst[4]}, {p_lst[5]} 상품을 대출 받을 수 있습니다.'
    elif len(p_lst) == 7:
        return f'고객님은 현재 {p_lst[0]}, {p_lst[1]}, {p_lst[2]}, {p_lst[3]}, {p_lst[4]}, {p_lst[5]}, {p_lst[6]} 상품을 대출 받을 수 있습니다.'
    elif len(p_lst) == 8:
        return f'고객님은 현재 {p_lst[0]}, {p_lst[1]}, {p_lst[2]}, {p_lst[3]}, {p_lst[4]}, {p_lst[5]}, {p_lst[6]}, {p_lst[7]} 상품을 대출 받을 수 있습니다.'
    elif len(p_lst) == 9:
        return f'고객님은 현재 {p_lst[0]}, {p_lst[1]}, {p_lst[2]}, {p_lst[3]}, {p_lst[4]}, {p_lst[5]}, {p_lst[6]}, {p_lst[7]}, {p_lst[8]} 상품을 대출 받을 수 있습니다.'
    else:
        return "현재 대출 받을 수 있는 상품이 없습니다."

#전세조회_output
@app.route('/api/search_borrow', methods=['POST'])
def search_borrow():
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

    answer_text = str(search_pro_borrow(number01, number02,number03,number04,number05))

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


#매매계산_input
def calc_buy():
    return "pass"

#전세계산_input
def calc_borrow_year():
    return "pass"

#월세계산_input
def calc_borrow_month():
    return "pass"

#매매계산_output
def calc_buy():
    return "pass"

#전세계산_output
def calc_borrow_year():
    return "pass"

#월세계산_output
def calc_borrow_month():
    return "pass"


#테스트_input
def test_calc(amount, period, rate):
    rate=float(rate)/12.0# 연이율을 월 rate로 변환

    # 대출경과월 세팅
    interest1_table = pd.DataFrame({"대출경과월":range(period)}) + 1

    # 매월 납입하는 amount 계산
    interest1_table["원금납입액"] = round(amount / period)

    # 마지막 납입월 보정 (1200만원 / 36의 값이 무한소수로 표현되므로 마지막 납입금액 보정 작업 수행
    interest1_table.loc[period-1,"원금납입액"] =math.floor(amount/period)

    # 대출 경과월에 따른 대출잔액, 월이자납입금액 계산
    for i in range(interest1_table["대출경과월"].size) :
        if i == 0 :
            interest1_table.loc[i, "대출잔액"] = round(amount - interest1_table.loc[i,"원금납입액"])
        else :
            interest1_table.loc[i, "대출잔액"] = round(interest1_table.loc[i-1, "대출잔액"] - interest1_table.loc[i, "원금납입액"]) 
            interest1_table.loc[i, "월이자납입금액"] = interest1_table.loc[i, "대출잔액"] * rate
        
    print (interest1_table)
    # 대출상환표 출력
    return interest1_table

#test_output
@app.route('/api/interest_calCulator', methods=['POST'])
def calCulator():
    body = request.get_json()
    print(body)
    params_df = body['action']['params']
    print(type(params_df))
    opt_operator = params_df['operators']
    amount = json.loads(params_df['sys_number01'])['amount']
    period = json.loads(params_df['sys_number02'])['amount']
    rate = json.loads(params_df['sys_number02'])['amount']

    # print(opt_operator, type(opt_operator), amount, type(amount))

    answer_text = str(test_calc(amount, period,rate))

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