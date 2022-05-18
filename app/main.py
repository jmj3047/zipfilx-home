from flask import Flask, request
import json
import pandas as pd
import math
import numpy as np



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
def calc_pro_buy(number01, number02, number03, number04):
    amount = number01
    period = number02
    income = number03
    method = number04

    '''
    각 상품별 적용금리 계산 함수
    '''

    # Product 1
    multicol1 = pd.MultiIndex.from_tuples([("이용기간", "10년"),
                                  ("이용기간", "20년"),
                                  ("이용기간", "30년")])
    df1 = pd.DataFrame([[0.0215, 0.0235, 0.024],
                        [0.025, 0.027, 0.0275],
                        [0.0275, 0.0295, 0.03]],
                    index = ["2천만원 이하", "2천만원 초과 4천만원 이하", "4천만원 초과 6천만원 이하"],
                    columns = multicol1)

    def cal_1():
        if income <= 2000:
            ind = 0
        elif 2000 < income <= 4000:
            ind = 1
        else:
            ind = 2
        
        if period == 10:
            col = 0
        elif period == 20:
            col = 1
        elif period == 30:
            col = 2
        else:
            col = 0
        
        interest = df1.iloc[ind,col]
        
        return(round(interest,3))

    # Product 2
    multicol2 = pd.MultiIndex.from_tuples([("이용기간", "10년"),
                                    ("이용기간", "20년"),
                                    ("이용기간", "30년")])
    df2 = pd.DataFrame([[0.0185, 0.0205, 0.021],
                        [0.022, 0.024, 0.0245],
                        [0.0245, 0.0265, 0.027]],
                    index = ["2천만원 이하", "2천만원 초과 4천만원 이하", "4천만원 초과 7천만원 이하"],
                    columns = multicol2)

    def cal_2():
        if income <= 2000:
            ind = 0
        elif 2000 < income <= 4000:
            ind = 1
        else:
            ind = 2
        
        if period == 10:
            col =  0
        elif period == 20:
            col =  1
        elif period == 30:
            col =  2
        else:
            col = 0

        interest = df2.iloc[ind,col]

        return(round(interest,3))

    # Product 3
    df3 = pd.DataFrame([0.023, 0.025, 0.028],
                    index = ["2천만원 이하", "2천만원 초과 4천만원 이하", "4천만원 초과 6천만원 이하"])
    df3.columns = ['금리']

    def cal_3():
        if income <= 2000:
            ind = 0
        elif 2000 < income <= 4000:
            ind = 1
        else:
            ind = 2

        interest = df3.iloc[ind,0]
        
        return(round(interest,3))

    # Product 4
    multicol4 = pd.MultiIndex.from_tuples([("이용기간", "10년"),
                                  ("이용기간", "20년"),
                                  ("이용기간", "30년")])
    df4 = pd.DataFrame([[0.041, 0.043, 0.0435]],
                    columns = multicol4)
    df4.index = ["금리"]

    def cal_4():
        if period == 10:
            col =  0
        elif period == 20:
            col =  1
        elif period == 30:
            col =  2
        else:
            col = 0

        interest = df4.iloc[0,col]

        return(round(interest,3))

    # Product 5
    multicol5 = pd.MultiIndex.from_tuples([("이용기간", "10년"),
                                  ("이용기간", "20년"),
                                  ("이용기간", "30년")])
    df5 = pd.DataFrame([[0.0215, 0.0235, 0.024],
                        [0.025, 0.027, 0.0275],
                        [0.0275, 0.0295, 0.03]],
                    index = ["2천만원 이하", "2천만원 초과 4천만원 이하", "4천만원 초과 6천만원 이하"],
                    columns = multicol5)

    def cal_5():
        if income <= 2000:
            ind = 0
        elif income <= 4000:
            ind = 1
        else:
            ind = 2

        if period == 10:
            col =  0
        elif period == 20:
            col =  1
        elif period == 30:
            col =  2
        else:
            col = 0

        interest= df5.iloc[ind,col]

        return(round(interest,3))


    '''
    상환방식별 납입금액 반환 함수
    '''

    # 만기일시상환
    def cal_method1(amount, period, rate):

        rate = float(rate)/12.0

        # 대출경과월 세팅
        table1 = pd.DataFrame({"대출경과월":range(period)}) + 1

        # 매월 납입하는 이자액 계산
        table1["월이자납입금액"] = amount * rate

        # 대출 경과월에 따른 대출잔액 및 월이자납입금액 계산
        for i in range(table1["대출경과월"].size) :
            if table1.loc[i,"대출경과월"] == period :
                table1.loc[i, "대출잔액"] = 0 
                table1.loc[i, "월이자납입금액"] = 0
            else :
                table1.loc[i, "대출잔액"] = amount
                
        # 대출상환표 출력
        return table1

    # 원리금균등상환
    def cal_method2(amount, period, rate):

        rate = float(rate)/12.0

        # X : 월 원리금균등상환금액
        X = (amount * rate * ((1 + rate)**period)) / (((1 + rate)**period) - 1)
        interest2_table = pd.DataFrame({'대출경과월' : np.arange(1, period + 1 , 1)}) # 대출경과월 셋팅 1 ~ 36 개월
        interest2_table["원리금균등상환액"] = X # 위에서 산출한 월 원리금균등상환금액 삽입

        # 매월 원금납입액, 이자납입액, 이자납입비율 산출
        for i in range(interest2_table["대출경과월"].size) :
            interest2_table.loc[i, "원금납입액"] = interest2_table.loc[i,"원리금균등상환액"] / ((1 + rate)**(period - i))
            interest2_table.loc[i, "이자납입액"] = interest2_table.loc[i,"원리금균등상환액"] - interest2_table.loc[i, "원금납입액"]
        
        return interest2_table

    # 원금균등상환
    def cal_method3(amount, period, rate):

        rate=float(rate)/12.0# 연이율을 월 rate로 변환

        # 대출경과월 세팅
        table3 = pd.DataFrame({"대출경과월":range(period)}) + 1

        # 매월 납입하는 이자액 계산
        table3["원금납입액"] = round(amount / period)

        # 마지막 납입월 보정
        table3.loc[period-1,"원금납입액"] =math.floor(amount/period)

        # 대출 경과월에 따른 대출잔액, 월이자납입금액 계산
        for i in range(table3["대출경과월"].size) :
            if i == 0 :
                table3.loc[i, "대출잔액"] = round(amount - table3.loc[i,"원금납입액"])
            else :
                table3.loc[i, "대출잔액"] = round(table3.loc[i-1, "대출잔액"] - table3.loc[i, "원금납입액"]) 
                table3.loc[i, "월이자납입금액"] = table3.loc[i, "대출잔액"] * rate
            
        # 대출상환표 출력
        return table3

    '''
    첫번째 상품 출력 코드
    '''
    if method == 1:
        return "상품1 - 만기일시상환" + '\n' + cal_method1(amount, period, cal_1()).to_string() + '\n'\
            + "상품2 - 만기일시상환" + '\n' + cal_method1(amount, period, cal_2()).to_string() + '\n'\
            + "상품3 - 만기일시상환" + '\n' + cal_method1(amount, period, cal_3()).to_string() + '\n'\
            + "상품4 - 만기일시상환" + '\n' + cal_method1(amount, period, cal_4()).to_string() + '\n'\
            + "상품5 - 만기일시상환" + '\n' + cal_method1(amount, period, cal_5()).to_string()
    elif method == 2:
        return "상품1 - 원리금균등상환" + '\n' + cal_method2(amount, period, cal_1()).to_string() + '\n'\
            + "상품2 - 원리금균등상환" + '\n' + cal_method2(amount, period, cal_2()).to_string() + '\n'\
            + "상품3 - 원리금균등상환" + '\n' + cal_method2(amount, period, cal_3()).to_string() + '\n'\
            + "상품4 - 원리금균등상환" + '\n' + cal_method2(amount, period, cal_4()).to_string() + '\n'\
            + "상품5 - 원리금균등상환" + '\n' + cal_method2(amount, period, cal_5()).to_string()
    elif method == 3:
        return "상품1 - 원금균등상환" + '\n' + cal_method3(amount, period, cal_1()).to_string() + '\n'\
            + "상품2 - 원금균등상환" + '\n' + cal_method3(amount, period, cal_2()).to_string() + '\n'\
            + "상품3 - 원금균등상환" + '\n' + cal_method3(amount, period, cal_3()).to_string() + '\n'\
            + "상품4 - 원금균등상환" + '\n' + cal_method3(amount, period, cal_4()).to_string() + '\n'\
            + "상품5 - 원금균등상환" + '\n' + cal_method3(amount, period, cal_5()).to_string()
    else:
        return "계산이 잘못되었습니다."

#매매계산_output
@app.route('/api/calc_buy', methods=['POST'])
def calc_buy():
    body = request.get_json()
    print(body)
    params_df = body['action']['params']
    print(type(params_df))
    # opt_operator = params_df['division']
    number01 = json.loads(params_df['sys_number01'])['amount']
    number02 = json.loads(params_df['sys_number02'])['amount']
    number03 = json.loads(params_df['sys_number03'])['amount']
    number04 = json.loads(params_df['sys_number04'])['amount']
    print('==========매매 계산기===========',number01,number02,number03,number04,'============================')
    # print(opt_operator, type(opt_operator), number01, type(number01))

    answer_text = str(calc_pro_buy(number01, number02,number03,number04))

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

#전세계산_input
def calc_pro_year(number01, number02, number03, number04,number05):
    amount = number01
    period = number02
    income = number03
    method = number04
    deposit = number05

    '''
    각 상품별 적용금리 계산 함수
    '''

    # Product 6
    multicol6 = pd.MultiIndex.from_tuples([("임차보증금", "5천만원 이하"),
                                    ("임차보증금", "5천만원 초과 ~ 1억원 이하"),
                                    ("임차보증금", "1억원 초과 ~ 1.5억원 이하"),
                                    ("임차보증금", "1.5억 초과")])
    df6 = pd.DataFrame([[0.012, 0.013, 0.014, 0.015],
                        [0.015, 0.016, 0.017, 0.018],
                        [0.018, 0.019, 0.019, 0.021]],
                    index = ["2천만원 이하", "2천만원 초과 4천만원 이하", "4천만원 초과 6천만원 이하"],
                    columns = multicol6)

    def cal_6():
        if income <= 2000:
            ind = 0
        elif income <= 4000:
            ind = 1
        elif income <= 6000:
            ind = 2
        else:
            ind = 0

        if deposit <= 5000:
            col =  0
        elif deposit <= 10000:
            col =  1
        elif deposit <= 15000:
            col =  2
        elif deposit > 15000:
            col =  3
        else:
            col = 0

        interest = df6.iloc[ind,col]

        return(round(interest,3))

    # Product 7
    multicol7 = pd.MultiIndex.from_tuples([("임차보증금", "5천만원 이하"),
                                    ("임차보증금", "5천만원 초과 ~ 1억원 이하"),
                                    ("임차보증금", "1억원 초과") ])
                                    
    df7 = pd.DataFrame([[0.018, 0.019, 0.02],
                        [0.020, 0.021, 0.022],
                        [0.022, 0.023, 0.024]], 
                    index = ["2천만원 이하", "2천만원 초과 4천만원 이하", "4천만원 초과 6천만원 이하"],
                    columns = multicol7)

    def cal_7():
        if income <= 2000:
            ind = 0
        elif income <= 4000:
            ind = 1
        elif income <= 6000:
            ind = 2
        else:
            ind = 0

        if deposit <= 5000:
            col =  0
        elif deposit <= 10000 :
            col =  1
        else:
            col = 2

        interest = df7.iloc[ind,col]

        return(round(interest,3))

    # Product 8
    def cal_8():
        interest = 0.012
        return interest

    # Product 10
    df_inter = pd.DataFrame([[0.015],
                        [0.018],
                        [0.021]],
                index = ["2천만원 이하", "2천만원 초과 4천만원 이하", "4천만원 초과 6천만원 이하"],
                columns = ["임차보증금 1억원 이하"])
    
    def select():

        if income < 2000:
            val = df_inter.iloc[0,0]
            return val
        elif income <= 4000 :
            val = df_inter.iloc[1,0]
            return val
        elif income > 4000:
            val = df_inter.iloc[2,0]
            return val

    def cal_10():
        
        if amount <= 5000 and deposit <= 7000:
            interest = select() - 0.003
            return interest
        elif (amount <= 7000 or amount <= deposit * 0.8) and deposit <=10000:
            interest = select()
            return interest
        else:
            return 0

    # Product 14
    def cal_14():
        interest = select()
        return interest


    '''
    상환방식별 납입금액 반환 함수
    '''

    # 만기일시상환
    def cal_method1(amount, period, rate):

        rate = float(rate)/12.0

        # 대출경과월 세팅
        table1 = pd.DataFrame({"대출경과월":range(period)}) + 1

        # 매월 납입하는 이자액 계산
        table1["월이자납입금액"] = amount * rate

        # 대출 경과월에 따른 대출잔액 및 월이자납입금액 계산
        for i in range(table1["대출경과월"].size) :
            if table1.loc[i,"대출경과월"] == period :
                table1.loc[i, "대출잔액"] = 0 
                table1.loc[i, "월이자납입금액"] = 0
            else :
                table1.loc[i, "대출잔액"] = amount
                
        # 대출상환표 출력
        return table1

    # 원리금균등상환
    def cal_method2(amount, period, rate):

        rate = float(rate)/12.0

        # X : 월 원리금균등상환금액
        X = (amount * rate * ((1 + rate)**period)) / (((1 + rate)**period) - 1)
        interest2_table = pd.DataFrame({'대출경과월' : np.arange(1, period + 1 , 1)}) # 대출경과월 셋팅 1 ~ 36 개월
        interest2_table["원리금균등상환액"] = X # 위에서 산출한 월 원리금균등상환금액 삽입

        # 매월 원금납입액, 이자납입액, 이자납입비율 산출
        for i in range(interest2_table["대출경과월"].size) :
            interest2_table.loc[i, "원금납입액"] = interest2_table.loc[i,"원리금균등상환액"] / ((1 + rate)**(period - i))
            interest2_table.loc[i, "이자납입액"] = interest2_table.loc[i,"원리금균등상환액"] - interest2_table.loc[i, "원금납입액"]
        
        return interest2_table

    # 원금균등상환
    def cal_method3(amount, period, rate):

        rate=float(rate)/12.0# 연이율을 월 rate로 변환

        # 대출경과월 세팅
        table3 = pd.DataFrame({"대출경과월":range(period)}) + 1

        # 매월 납입하는 이자액 계산
        table3["원금납입액"] = round(amount / period)

        # 마지막 납입월 보정
        table3.loc[period-1,"원금납입액"] =math.floor(amount/period)

        # 대출 경과월에 따른 대출잔액, 월이자납입금액 계산
        for i in range(table3["대출경과월"].size) :
            if i == 0 :
                table3.loc[i, "대출잔액"] = round(amount - table3.loc[i,"원금납입액"])
            else :
                table3.loc[i, "대출잔액"] = round(table3.loc[i-1, "대출잔액"] - table3.loc[i, "원금납입액"]) 
                table3.loc[i, "월이자납입금액"] = table3.loc[i, "대출잔액"] * rate
            
        # 대출상환표 출력
        return table3

    '''
    첫번째 상품 출력 코드
    '''
    if method == 1:
        return "상품6 - 만기일시상환" + '\n' + cal_method1(amount, period, cal_6()).to_string() + '\n'\
            + "상품7 - 만기일시상환" + '\n' + cal_method1(amount, period, cal_7()).to_string() + '\n'\
            + "상품8 - 만기일시상환" + '\n' + cal_method1(amount, period, cal_8()).to_string() + '\n'\
            + "상품10 - 만기일시상환" + '\n' + cal_method1(amount, period, cal_10()).to_string() + '\n'\
            + "상품14 - 만기일시상환" + '\n' + cal_method1(amount, period, cal_14()).to_string()
    elif method == 2:
        return "상품6 - 원리금균등상환" + '\n' + cal_method2(amount, period, cal_6()).to_string() + '\n'\
            + "상품7 - 원리금균등상환" + '\n' + cal_method2(amount, period, cal_7()).to_string() + '\n'\
            + "상품8 - 원리금균등상환" + '\n' + cal_method2(amount, period, cal_8()).to_string() + '\n'\
            + "상품10 - 원리금균등상환" + '\n' + cal_method2(amount, period, cal_10()).to_string() + '\n'\
            + "상품14 - 원리금균등상환" + '\n' + cal_method2(amount, period, cal_14()).to_string()
    elif method == 3:
        return "상품6 - 원금균등상환" + '\n' + cal_method3(amount, period, cal_6()).to_string() + '\n'\
            + "상품7 - 원금균등상환" + '\n' + cal_method3(amount, period, cal_7()).to_string() + '\n'\
            + "상품8 - 원금균등상환" + '\n' + cal_method3(amount, period, cal_8()).to_string() + '\n'\
            + "상품10 - 원금균등상환" + '\n' + cal_method3(amount, period, cal_10()).to_string() + '\n'\
            + "상품14 - 원금균등상환" + '\n' + cal_method3(amount, period, cal_14()).to_string()
    else:
        return "계산이 잘못되었습니다."


#전세계산_output
@app.route('/api/calc_borrow_year', methods=['POST'])
def calc_borrow_year():
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
    print('==========전세 계산기===========',number01,number02,number03,number04,number05,'============================')
    # print(opt_operator, type(opt_operator), number01, type(number01))

    answer_text = str(calc_pro_year(number01, number02,number03,number04,number05))

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


# #월세계산_input
# def calc_borrow_month():
#     return "pass"


# #월세계산_output
# def calc_borrow_month():
#     return "pass"


