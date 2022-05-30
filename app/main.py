from flask import Flask, request
import json
import pandas as pd
import math
import numpy as np
import psycopg2

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

   
#매매조회_input_DB연동
def search_pro_buy(number01,number02,number03,number04,number05):
    i1 = 1
    i2 = 2
    i3 = 3
    i4 = 4
    i5 = 5
    
    q1 = number01
    q2 = number02
    q3 = number03
    q4 = number04
    q5 = number05
    
    print(q1,q2,q3,q4,q5, type(q1))
    
    i_lst = []
    if q1 in [1,2] and q2 in [2,3] and q3 in [1,2,3] and q4 in [1,2] and q5 in [1,2]:
        i_lst.append(i1)
    if q1 in [1,2] and q2 in [2,3] and q3 == 2 and q4 in [1,2] and q5 in [1,2]:
        i_lst.append(i2)
    if q1 in [1,2] and q2 in [2,3] and q3 in [1,2,3] and q4 == 2 and q5 == 2:
        i_lst.append(i3)
    if q1 in [1,2,3] and q2 in [2,3] and q3 in [1,2] and q4 in [1,2] and q5 in [1,2,3]:
        i_lst.append(i4)
    if q1 in [1,2] and q2 in [1,2,3] and q3 == 2 and q4 in [1,2] and q5 in [1,2,3]:
        i_lst.append(i5)

    
    db=psycopg2.connect(host='ec2-52-86-115-245.compute-1.amazonaws.com',dbname='d6b5cq66b2ua5t',user='wtpphkajtmedfy',password='841bff0c520a53c484118e65528ac47410f4730a8d3dd4876f96ec13776b3a59',port=5432)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM realzip')
    rows=cursor.fetchall()
    str_return = ""
    for i in range(len(i_lst)):
        str_return = str_return + str(i+1) + "." + "\n"
        for st in (rows[i_lst[i]-1]):
            st_split = st.split(":", maxsplit=1)
            str_return = str_return + "-" + ' ' + str(st_split[0]) + ":" + "\n"
            if len(st_split)==2:
                str_return = str_return + ' ' + str(st_split[1]) + '\n'
        str_return = str_return + "\n\n"
    return "고객님은 총 "+ str(len(i_lst))+"개의 상품을 대출 가능합니다."+'\n\n'+ str_return


    
    
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

#전세 조회 input_DB연동
def search_pro_borrow(number01,number02,number03,number04,number05):
    i6=6
    i7=7
    i8=8
    i9=9
    i10=10
    i11=11
    i12=12
    i13=13
    i14=14

    
    q1 = number01
    q2 = number02
    q3 = number03
    q4 = number04
    q5 = number05
    
    print(q1,q2,q3,q4,q5, type(q1))
    
    i_lst = []
    if q1 == 1 and q2 in [2,3] and q3 == 2 and q4 in [1,2] and q5 == 1:
        i_lst.append(i6)
    if q1 == 1 and q2 in [2,3] and q3 in [1,2,3] and q4 == 1 and q5 == 1:
        i_lst.append(i7)
    if q1 in [1,2,3] and q2 == 2 and q3 in [1,2,3] and q4 == 1 and q5 == 1:
        i_lst.append(i8)
    if q1 in [1,2,3] and q2 in [2,3] and q3 in [1,2,3] and q4 == 1 and q5 == 1:
        i_lst.append(i9)
    if q1 in [1,2,3] and q2 == 2 and q3 in [1,2,3] and q4 in [1,2] and q5 == 1:
        i_lst.append(i10)
        i_lst.append(i14)
    if q1 in [1,2,3] and q2 == 2 and q3 in [1,2,3] and q4 == 1 and q5 == 1:
        i_lst.append(i11)
        i_lst.append(i12)
        i_lst.append(i13)
    
    db=psycopg2.connect(host='ec2-52-86-115-245.compute-1.amazonaws.com',dbname='d6b5cq66b2ua5t',user='wtpphkajtmedfy',password='841bff0c520a53c484118e65528ac47410f4730a8d3dd4876f96ec13776b3a59',port=5432)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM realzip')
    rows=cursor.fetchall()
    str_return = ""
    for i in range(len(i_lst)):
        str_return = str_return + str(i+1) + "." + "\n"
        for st in (rows[i_lst[i]-1]):
            st_split = st.split(":", maxsplit=1)
            str_return = str_return + "-" + ' ' + str(st_split[0]) + ":" + "\n"
            if len(st_split)==2:
                str_return = str_return + ' ' + str(st_split[1]) + '\n'
        str_return = str_return + "\n\n"
    return "고객님은 총 "+ str(len(i_lst))+"개의 상품을 대출 가능합니다."+'\n\n'+ str_return



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

    m_lst = ["주택도시기금 디딤돌 대출", "주택도시기금 신혼부부전용 구입자금", "오피스텔 구입자금"
                , "한국주택금융공사 보금자리론", "한국주택금융공사 디딤돌대출"]

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
    def cal_method1(amount, period, y_rate):
        period = period*12
        m_rate = float(y_rate)/12.0

        # 월 세팅
        table1 = pd.DataFrame({"월":range(period)}) + 1

        # 매월 납입하는 이자액 계산
        table1["이자납입액"] = amount * m_rate

        # 대출 경과월에 따른 대출잔액 및 월이자납입금액 계산
        for i in range(table1["월"].size) :
            if table1.loc[i,"월"] == period :
                table1.loc[i, "대출잔액"] = 0 
                table1.loc[i, "이자납입액"] = 0
            else :
                table1.loc[i, "대출잔액"] = amount
        table1["대출잔액"] = round(table1["대출잔액"] * 10000)
        table1["이자납입액"] = round(table1["이자납입액"] * 10000)
        table1.set_index('월', inplace=True)
        pd.options.display.float_format = '{:,}'.format
        return ["만기일시상환", y_rate, np.nansum(table1["이자납입액"])]

    # 원리금균등상환
    def cal_method2(amount, period, y_rate):
        period = period*12
        m_rate = float(y_rate)/12.0

        # X : 월 원리금균등상환금액
        X = (amount * m_rate * ((1 + m_rate)**period)) / (((1 + m_rate)**period) - 1)
        table2 = pd.DataFrame({'월' : np.arange(1, period + 1 , 1)}) # 월 셋팅 1 ~ 36 개월
        table2["월 상환액"] = X # 위에서 산출한 월 원리금균등상환금액 삽입

        # 매월 원금납입액, 이자납입액, 이자납입비율 산출
        for i in range(table2["월"].size) :
            table2.loc[i, "원금납입액"] = table2.loc[i,"월 상환액"] / ((1 + m_rate)**(period - i))
            table2.loc[i, "이자납입액"] = table2.loc[i,"월 상환액"] - table2.loc[i, "원금납입액"]
        
        table2["월 상환액"] = round(table2["월 상환액"] * 10000)
        table2["원금납입액"] = round(table2["원금납입액"] * 10000)
        table2["이자납입액"] = round(table2["이자납입액"] * 10000)
        table2.set_index('월', inplace=True)
        table2 = table2[["원금납입액", "이자납입액", "월 상환액"]]
        pd.options.display.float_format = '{:,}'.format
        return ["원리금균등상환", table2.head(10).to_string(), y_rate, np.nansum(table2["이자납입액"])]

    # 원금균등상환
    def cal_method3(amount, period, y_rate):
        period = period*12
        m_rate = float(y_rate)/12.0# 연이율을 월 rate로 변환

        # 월 세팅
        table3 = pd.DataFrame({"월":range(period)}) + 1

        # 매월 납입하는 이자액 계산
        table3["원금납입액"] = round(amount / period)

        # 대출 경과월에 따른 대출잔액, 월이자납입금액 계산
        for i in range(table3["월"].size) :
            if i == 0 :
                table3.loc[i, "대출잔액"] = round(amount - table3.loc[i,"원금납입액"])
            else :
                table3.loc[i, "대출잔액"] = round(table3.loc[i-1, "대출잔액"] - table3.loc[i, "원금납입액"]) 
                table3.loc[i, "이자납입액"] = table3.loc[i, "대출잔액"] * m_rate
         
        table3["원금납입액"] = round(table3["원금납입액"] * 10000.0)
        table3["이자납입액"] = round(table3["이자납입액"] * 10000)
        table3["대출잔액"] = round(table3["대출잔액"] * 10000)
        table3.set_index('월', inplace=True)
        table3 = table3[["원금납입액", "이자납입액", "대출잔액"]]
        pd.options.display.float_format = '{:,}'.format
        return ["원금균등상환", table3.head(10).to_string(), y_rate, np.nansum(table3["이자납입액"])]

    '''
    첫번째 상품 출력 코드
    '''
    if method == 1:
        str_mtd, rate1, tot1 = cal_method1(amount, period, cal_1())
        str_mtd, rate2, tot2 = cal_method1(amount, period, cal_2())
        str_mtd, rate3, tot3 = cal_method1(amount, period, cal_3())
        str_mtd, rate4, tot4 = cal_method1(amount, period, cal_4())
        str_mtd, rate5, tot5 = cal_method1(amount, period, cal_5())
        df1, df2, df3, df4, df5 = ["","","","", ""]
    elif method == 2:
        str_mtd, df1, rate1, tot1 = cal_method2(amount, period, cal_1())
        str_mtd, df2, rate2, tot2 = cal_method2(amount, period, cal_2())
        str_mtd, df3, rate3, tot3 = cal_method2(amount, period, cal_3())
        str_mtd, df4, rate4, tot4 = cal_method2(amount, period, cal_4())
        str_mtd, df5, rate5, tot5 = cal_method2(amount, period, cal_5())
    elif method == 3:
        str_mtd, df1, rate1, tot1 = cal_method3(amount, period, cal_1())
        str_mtd, df2, rate2, tot2 = cal_method3(amount, period, cal_2())
        str_mtd, df3, rate3, tot3 = cal_method3(amount, period, cal_3())
        str_mtd, df4, rate4, tot4 = cal_method3(amount, period, cal_4())
        str_mtd, df5, rate5, tot5 = cal_method3(amount, period, cal_5())
    
    str_return = m_lst[0] + '\n'\
        + "대출금액 : " + f'{amount*10000:,}' + "원" + '\n'\
        + "대출기간 : " + str(period) + "년" + '\n'\
        + "상환방법 : " + str_mtd + '\n'\
        + "적용 금리 : " + str(round(rate1*100,2)) + "%" + '\n'\
        + "총 이자액 : " + f'{int(round(tot1)):,}' + "원" + '\n'\
        + df1 + '\n'\
        + "\n-----------------------------\n"\
        + m_lst[1] + '\n'\
        + "대출금액 : " + f'{amount*10000:,}' + "원" + '\n'\
        + "대출기간 : " + str(period) + "년" + '\n'\
        + "상환방법 : " + str_mtd + '\n'\
        + "적용 금리 : " + str(round(rate2*100,2)) + "%" + '\n'\
        + "총 이자액 : " + f'{int(round(tot2)):,}' + "원" + '\n'\
        + df2 + '\n'\
        + "\n-----------------------------\n"\
        + m_lst[2] + '\n'\
        + "대출금액 : " + f'{amount*10000:,}' + "원" + '\n'\
        + "대출기간 : " + str(period) + "년" + '\n'\
        + "상환방법 : " + str_mtd + '\n'\
        + "적용 금리 : " + str(round(rate3*100,2)) + "%" + '\n'\
        + "총 이자액 : " + f'{int(round(tot3)):,}' + "원" + '\n'\
        + df3 + '\n'\
        + "\n-----------------------------\n"\
        + m_lst[3] + '\n'\
        + "대출금액 : " + f'{amount*10000:,}' + "원" + '\n'\
        + "대출기간 : " + str(period) + "년" + '\n'\
        + "상환방법 : " + str_mtd + '\n'\
        + "적용 금리 : " + str(round(rate4*100,2)) + "%" + '\n'\
        + "총 이자액 : " + f'{int(round(tot4)):,}' + "원" + '\n'\
        + df4 + '\n'\
        + "\n-----------------------------\n"\
        + m_lst[4] + '\n'\
        + "대출금액 : " + f'{amount*10000:,}' + "원" + '\n'\
        + "대출기간 : " + str(period) + "년" + '\n'\
        + "상환방법 : " + str_mtd + '\n'\
        + "적용 금리 : " + str(round(rate5*100,2)) + "%" + '\n'\
        + "총 이자액 : " + f'{int(round(tot5)):,}' + "원" + '\n'\
        + df5 + '\n'

    return str_return


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

    j_lst = ["신혼부부전용 전세자금", "버팀목전세자금", "중소기업취업청년 전월세 대출"
            , "청년전용 버팀목전세자금(일반)", "청년전용 버팀목전세자금(신혼/다자녀/2자녀가구)"]

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
        else:
            ind = 2

        if deposit <= 5000:
            col =  0
        elif deposit <= 10000:
            col =  1
        elif deposit <= 15000:
            col =  2
        else:
            col = 3

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
        else:
            ind = 2

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
        elif amount <= min(7000, deposit*0.8):
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
    def cal_method1(amount, period, y_rate):
        period = period*12
        m_rate = float(y_rate)/12.0

        # 월 세팅
        table1 = pd.DataFrame({"월":range(period)}) + 1

        # 매월 납입하는 이자액 계산
        table1["이자납입액"] = amount * m_rate

        # 대출 경과월에 따른 대출잔액 및 월이자납입금액 계산
        for i in range(table1["월"].size) :
            if table1.loc[i,"월"] == period :
                table1.loc[i, "대출잔액"] = 0 
                table1.loc[i, "이자납입액"] = 0
            else :
                table1.loc[i, "대출잔액"] = amount
        table1["대출잔액"] = round(table1["대출잔액"] * 10000)
        table1["이자납입액"] = round(table1["이자납입액"] * 10000)
        table1.set_index('월', inplace=True)
        pd.options.display.float_format = '{:,}'.format
        return ["만기일시상환", y_rate, np.nansum(table1["이자납입액"])]

    # 원리금균등상환
    def cal_method2(amount, period, y_rate):
        period = period*12
        m_rate = float(y_rate)/12.0

        # X : 월 원리금균등상환금액
        X = (amount * m_rate * ((1 + m_rate)**period)) / (((1 + m_rate)**period) - 1)
        table2 = pd.DataFrame({'월' : np.arange(1, period + 1 , 1)}) # 월 셋팅 1 ~ 36 개월
        table2["월 상환액"] = X # 위에서 산출한 월 원리금균등상환금액 삽입

        # 매월 원금납입액, 이자납입액, 이자납입비율 산출
        for i in range(table2["월"].size) :
            table2.loc[i, "원금납입액"] = table2.loc[i,"월 상환액"] / ((1 + m_rate)**(period - i))
            table2.loc[i, "이자납입액"] = table2.loc[i,"월 상환액"] - table2.loc[i, "원금납입액"]
        
        table2["월 상환액"] = round(table2["월 상환액"] * 10000)
        table2["원금납입액"] = round(table2["원금납입액"] * 10000)
        table2["이자납입액"] = round(table2["이자납입액"] * 10000)
        table2.set_index('월', inplace=True)
        table2 = table2[["원금납입액", "이자납입액", "월 상환액"]]
        pd.options.display.float_format = '{:,}'.format
        return ["원리금균등상환", table2.head(10).to_string(), y_rate, np.nansum(table2["이자납입액"])]

    # 원금균등상환
    def cal_method3(amount, period, y_rate):
        period = period*12
        m_rate = float(y_rate)/12.0# 연이율을 월 rate로 변환

        # 월 세팅
        table3 = pd.DataFrame({"월":range(period)}) + 1

        # 매월 납입하는 이자액 계산
        table3["원금납입액"] = round(amount / period)

        # 대출 경과월에 따른 대출잔액, 월이자납입금액 계산
        for i in range(table3["월"].size) :
            if i == 0 :
                table3.loc[i, "대출잔액"] = round(amount - table3.loc[i,"원금납입액"])
            else :
                table3.loc[i, "대출잔액"] = round(table3.loc[i-1, "대출잔액"] - table3.loc[i, "원금납입액"]) 
                table3.loc[i, "이자납입액"] = table3.loc[i, "대출잔액"] * m_rate
         
        table3["원금납입액"] = round(table3["원금납입액"] * 10000.0)
        table3["이자납입액"] = round(table3["이자납입액"] * 10000)
        table3["대출잔액"] = round(table3["대출잔액"] * 10000)
        table3.set_index('월', inplace=True)
        table3 = table3[["원금납입액", "이자납입액", "대출잔액"]]
        pd.options.display.float_format = '{:,}'.format
        return ["원금균등상환", table3.head(10).to_string(), y_rate, np.nansum(table3["이자납입액"])]

    '''
    첫번째 상품 출력 코드
    '''
    if amount <= min(7000, deposit*0.8):
        if method == 1:
            str_mtd, rate1, tot1 = cal_method1(amount, period, cal_6())
            str_mtd, rate2, tot2 = cal_method1(amount, period, cal_7())
            str_mtd, rate3, tot3 = cal_method1(amount, period, cal_8())
            str_mtd, rate4, tot4 = cal_method1(amount, period, cal_10())
            str_mtd, rate5, tot5 = cal_method1(amount, period, cal_14())
            df1, df2, df3, df4, df5 = ["","","","", ""]
        elif method == 2:
            str_mtd, df1, rate1, tot1 = cal_method2(amount, period, cal_6())
            str_mtd, df2, rate2, tot2 = cal_method2(amount, period, cal_7())
            str_mtd, df3, rate3, tot3 = cal_method2(amount, period, cal_8())
            str_mtd, df4, rate4, tot4 = cal_method2(amount, period, cal_10())
            str_mtd, df5, rate5, tot5 = cal_method2(amount, period, cal_14())
        elif method == 3:
            str_mtd, df1, rate1, tot1 = cal_method3(amount, period, cal_6())
            str_mtd, df2, rate2, tot2 = cal_method3(amount, period, cal_7())
            str_mtd, df3, rate3, tot3 = cal_method3(amount, period, cal_8())
            str_mtd, df4, rate4, tot4 = cal_method3(amount, period, cal_10())
            str_mtd, df5, rate5, tot5 = cal_method3(amount, period, cal_14())
        
        str_return = j_lst[0] + '\n'\
            + "대출금액 : " + f'{amount*10000:,}' + "원" + '\n'\
            + "대출기간 : " + str(period) + "년" + '\n'\
            + "상환방법 : " + str_mtd + '\n'\
            + "적용 금리 : " + str(round(rate1*100,2)) + "%" + '\n'\
            + "총 이자액 : " + f'{int(round(tot1)):,}' + "원" + '\n'\
            + df1 + '\n'\
            + "\n-----------------------------\n"\
            + j_lst[1] + '\n'\
            + "대출금액 : " + f'{amount*10000:,}' + "원" + '\n'\
            + "대출기간 : " + str(period) + "년" + '\n'\
            + "상환방법 : " + str_mtd + '\n'\
            + "적용 금리 : " + str(round(rate2*100,2)) + "%" + '\n'\
            + "총 이자액 : " + f'{int(round(tot2)):,}' + "원" + '\n'\
            + df2 + '\n'\
            + "\n-----------------------------\n"\
            + j_lst[2] + '\n'\
            + "대출금액 : " + f'{amount*10000:,}' + "원" + '\n'\
            + "대출기간 : " + str(period) + "년" + '\n'\
            + "상환방법 : " + str_mtd + '\n'\
            + "적용 금리 : " + str(round(rate3*100,2)) + "%" + '\n'\
            + "총 이자액 : " + f'{int(round(tot3)):,}' + "원" + '\n'\
            + df3 + '\n'\
            + "\n-----------------------------\n"\
            + j_lst[3] + '\n'\
            + "대출금액 : " + f'{amount*10000:,}' + "원" + '\n'\
            + "대출기간 : " + str(period) + "년" + '\n'\
            + "상환방법 : " + str_mtd + '\n'\
            + "적용 금리 : " + str(round(rate4*100,2)) + "%" + '\n'\
            + "총 이자액 : " + f'{int(round(tot4)):,}' + "원" + '\n'\
            + df4 + '\n'\
            + "\n-----------------------------\n"\
            + j_lst[4] + '\n'\
            + "대출금액 : " + f'{amount*10000:,}' + "원" + '\n'\
            + "대출기간 : " + str(period) + "년" + '\n'\
            + "상환방법 : " + str_mtd + '\n'\
            + "적용 금리 : " + str(round(rate5*100,2)) + "%" + '\n'\
            + "총 이자액 : " + f'{int(round(tot5)):,}' + "원" + '\n'\
            + df5 + '\n'
    else:
        if method == 1:
            str_mtd, rate1, tot1 = cal_method1(amount, period, cal_6())
            str_mtd, rate2, tot2 = cal_method1(amount, period, cal_7())
            str_mtd, rate3, tot3 = cal_method1(amount, period, cal_8())
            df1, df2, df3, df4, df5 = ["","","","", ""]
        elif method == 2:
            str_mtd, df1, rate1, tot1 = cal_method2(amount, period, cal_6())
            str_mtd, df2, rate2, tot2 = cal_method2(amount, period, cal_7())
            str_mtd, df3, rate3, tot3 = cal_method2(amount, period, cal_8())
        elif method == 3:
            str_mtd, df1, rate1, tot1 = cal_method3(amount, period, cal_6())
            str_mtd, df2, rate2, tot2 = cal_method3(amount, period, cal_7())
            str_mtd, df3, rate3, tot3 = cal_method3(amount, period, cal_8())
        
        str_return = j_lst[0] + '\n'\
            + "대출금액 : " + f'{amount*10000:,}' + "원" + '\n'\
            + "대출기간 : " + str(period) + "년" + '\n'\
            + "상환방법 : " + str_mtd + '\n'\
            + "적용 금리 : " + str(round(rate1*100,2)) + "%" + '\n'\
            + "총 이자액 : " + f'{int(round(tot1)):,}' + "원" + '\n'\
            + df1 + '\n'\
            + "\n-----------------------------\n"\
            + j_lst[1] + '\n'\
            + "대출금액 : " + f'{amount*10000:,}' + "원" + '\n'\
            + "대출기간 : " + str(period) + "년" + '\n'\
            + "상환방법 : " + str_mtd + '\n'\
            + "적용 금리 : " + str(round(rate2*100,2)) + "%" + '\n'\
            + "총 이자액 : " + f'{int(round(tot2)):,}' + "원" + '\n'\
            + df2 + '\n'\
            + "\n-----------------------------\n"\
            + j_lst[2] + '\n'\
            + "대출금액 : " + f'{amount*10000:,}' + "원" + '\n'\
            + "대출기간 : " + str(period) + "년" + '\n'\
            + "상환방법 : " + str_mtd + '\n'\
            + "적용 금리 : " + str(round(rate3*100,2)) + "%" + '\n'\
            + "총 이자액 : " + f'{int(round(tot3)):,}' + "원" + '\n'\
            + df3 + '\n'
    return str_return


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


#월세계산_input
def calc_pro_month(number01,number02,number03):
    amount = number01
    period = number02 
    method = number03

    w_lst = ["청년전용 보증부월세대출", "주거안정월세대출(일반)"
            , "주거안정월세대출(우대/취준생)", "주거안정월세대출(우대/사회초년생)"]

    # 각 상품별 적용금리 계산 함수

    # Product 9
    def cal_9():
        if amount <= 480:
            interest = 0.000 
            return interest
        elif amount <= 1200:
            interest = 0.010
            return interest
        elif amount <= 3500:
            interest = 0.013
            return interest
        else:
            return 0

    # Product 11
    def cal_11():
    
        if amount <= 960:
            interest = 0.015
            return interest
        else:
            return 0


    # Product 12
    def cal_12():
    
        if amount <= 960:
            interest = 0.010
            return interest
        else:
            return 0


    # Product 13
    def cal_13():
    
        if amount <= 960:
            interest = 0.010
            return interest
        else:
            return 0

    # 상환방식별 납입금액 반환 함수

    # 만기일시상환
    def cal_method1(amount, period, y_rate):
        period = period*12
        m_rate = float(y_rate)/12.0

        # 월 세팅
        table1 = pd.DataFrame({"월":range(period)}) + 1

        # 매월 납입하는 이자액 계산
        table1["이자납입액"] = amount * m_rate

        # 대출 경과월에 따른 대출잔액 및 월이자납입금액 계산
        for i in range(table1["월"].size) :
            if table1.loc[i,"월"] == period :
                table1.loc[i, "대출잔액"] = 0 
                table1.loc[i, "이자납입액"] = 0
            else :
                table1.loc[i, "대출잔액"] = amount
        table1["대출잔액"] = round(table1["대출잔액"] * 10000)
        table1["이자납입액"] = round(table1["이자납입액"] * 10000)
        table1.set_index('월', inplace=True)
        pd.options.display.float_format = '{:,}'.format
        return ["만기일시상환", y_rate, np.nansum(table1["이자납입액"])]

    # 원리금균등상환
    def cal_method2(amount, period, y_rate):
        period = period*12
        m_rate = float(y_rate)/12.0

        # X : 월 원리금균등상환금액
        X = (amount * m_rate * ((1 + m_rate)**period)) / (((1 + m_rate)**period) - 1)
        table2 = pd.DataFrame({'월' : np.arange(1, period + 1 , 1)}) # 월 셋팅 1 ~ 36 개월
        table2["월 상환액"] = X # 위에서 산출한 월 원리금균등상환금액 삽입

        # 매월 원금납입액, 이자납입액, 이자납입비율 산출
        for i in range(table2["월"].size) :
            table2.loc[i, "원금납입액"] = table2.loc[i,"월 상환액"] / ((1 + m_rate)**(period - i))
            table2.loc[i, "이자납입액"] = table2.loc[i,"월 상환액"] - table2.loc[i, "원금납입액"]
        
        table2["월 상환액"] = round(table2["월 상환액"] * 10000)
        table2["원금납입액"] = round(table2["원금납입액"] * 10000)
        table2["이자납입액"] = round(table2["이자납입액"] * 10000)
        table2.set_index('월', inplace=True)
        table2 = table2[["원금납입액", "이자납입액", "월 상환액"]]
        pd.options.display.float_format = '{:,}'.format
        return ["원리금균등상환", table2.head(10).to_string(), y_rate, np.nansum(table2["이자납입액"])]

    # 원금균등상환
    def cal_method3(amount, period, y_rate):
        period = period*12
        m_rate = float(y_rate)/12.0# 연이율을 월 rate로 변환

        # 월 세팅
        table3 = pd.DataFrame({"월":range(period)}) + 1

        # 매월 납입하는 이자액 계산
        table3["원금납입액"] = round(amount / period)

        # 대출 경과월에 따른 대출잔액, 월이자납입금액 계산
        for i in range(table3["월"].size) :
            if i == 0 :
                table3.loc[i, "대출잔액"] = round(amount - table3.loc[i,"원금납입액"])
            else :
                table3.loc[i, "대출잔액"] = round(table3.loc[i-1, "대출잔액"] - table3.loc[i, "원금납입액"]) 
                table3.loc[i, "이자납입액"] = table3.loc[i, "대출잔액"] * m_rate
         
        table3["원금납입액"] = round(table3["원금납입액"] * 10000.0)
        table3["이자납입액"] = round(table3["이자납입액"] * 10000)
        table3["대출잔액"] = round(table3["대출잔액"] * 10000)
        table3.set_index('월', inplace=True)
        table3 = table3[["원금납입액", "이자납입액", "대출잔액"]]
        pd.options.display.float_format = '{:,}'.format
        return ["원금균등상환", table3.head(10).to_string(), y_rate, np.nansum(table3["이자납입액"])]

    '''
    첫번째 상품 출력 코드
    '''
    if amount <= 960:
        if method == 1:
            str_mtd, rate1, tot1 = cal_method1(amount, period, cal_9())
            str_mtd, rate2, tot2 = cal_method1(amount, period, cal_11())
            str_mtd, rate3, tot3 = cal_method1(amount, period, cal_12())
            str_mtd, rate4, tot4 = cal_method1(amount, period, cal_13())
            df1, df2, df3, df4 = ["","","",""]
        elif method == 2:
            str_mtd, df1, rate1, tot1 = cal_method2(amount, period, cal_9())
            str_mtd, df2, rate2, tot2 = cal_method2(amount, period, cal_11())
            str_mtd, df3, rate3, tot3 = cal_method2(amount, period, cal_12())
            str_mtd, df4, rate4, tot4 = cal_method2(amount, period, cal_13())
        elif method == 3:
            str_mtd, df1, rate1, tot1 = cal_method3(amount, period, cal_9())
            str_mtd, df2, rate2, tot2 = cal_method3(amount, period, cal_11())
            str_mtd, df3, rate3, tot3 = cal_method3(amount, period, cal_12())
            str_mtd, df4, rate4, tot4 = cal_method3(amount, period, cal_13())
        
        str_return = w_lst[0] + '\n'\
            + "대출금액 : " + f'{amount*10000:,}' + "원" + '\n'\
            + "대출기간 : " + str(period) + "년" + '\n'\
            + "상환방법 : " + str_mtd + '\n'\
            + "적용 금리 : " + str(round(rate1*100,2)) + "%" + '\n'\
            + "총 이자액 : " + f'{int(round(tot1)):,}' + "원" + '\n'\
            + df1 + '\n'\
            + "\n-----------------------------\n"\
            + w_lst[1] + '\n'\
            + "대출금액 : " + f'{amount*10000:,}' + "원" + '\n'\
            + "대출기간 : " + str(period) + "년" + '\n'\
            + "상환방법 : " + str_mtd + '\n'\
            + "적용 금리 : " + str(round(rate2*100,2)) + "%" + '\n'\
            + "총 이자액 : " + f'{int(round(tot2)):,}' + "원" + '\n'\
            + df2 + '\n'\
            + "\n-----------------------------\n"\
            + w_lst[2] + '\n'\
            + "대출금액 : " + f'{amount*10000:,}' + "원" + '\n'\
            + "대출기간 : " + str(period) + "년" + '\n'\
            + "상환방법 : " + str_mtd + '\n'\
            + "적용 금리 : " + str(round(rate3*100,2)) + "%" + '\n'\
            + "총 이자액 : " + f'{int(round(tot3)):,}' + "원" + '\n'\
            + df3 + '\n'\
            + "\n-----------------------------\n"\
            + w_lst[3] + '\n'\
            + "대출금액 : " + f'{amount*10000:,}' + "원" + '\n'\
            + "대출기간 : " + str(period) + "년" + '\n'\
            + "상환방법 : " + str_mtd + '\n'\
            + "적용 금리 : " + str(round(rate4*100,2)) + "%" + '\n'\
            + "총 이자액 : " + f'{int(round(tot4)):,}' + "원" + '\n'\
            + df4 + '\n'
    elif amount <= 3500:
        if method == 1:
            str_mtd, rate1, tot1 = cal_method1(amount, period, cal_9())
            df1 = ""
        elif method == 2:
            str_mtd, df1, rate1, tot1 = cal_method2(amount, period, cal_9())
        elif method == 3:
            str_mtd, df1, rate1, tot1 = cal_method3(amount, period, cal_9())

        str_return = w_lst[0] + '\n'\
            + "대출금액 : " + f'{amount*10000:,}' + "원" + '\n'\
            + "대출기간 : " + str(period) + "년" + '\n'\
            + "상환방법 : " + str_mtd + '\n'\
            + "적용 금리 : " + str(round(rate1*100,2)) + "%" + '\n'\
            + "총 이자액 : " + f'{int(round(tot1)):,}' + "원" + '\n'\
            + df1 + '\n'
    else:
        str_return = "입력하신 대출금액이 상품의 한도를 초과하였습니다"
    return str_return


#월세계산_output
@app.route('/api/calc_borrow_month', methods=['POST'])
def calc_borrow_month():
    body = request.get_json()
    print(body)
    params_df = body['action']['params']
    print(type(params_df))
    # opt_operator = params_df['division']
    number01 = json.loads(params_df['sys_number01'])['amount']
    number02 = json.loads(params_df['sys_number02'])['amount']
    number03 = json.loads(params_df['sys_number03'])['amount']
    print('==========월세 계산기===========',number01,number02,number03,'============================')
    # print(opt_operator, type(opt_operator), number01, type(number01))

    answer_text = str(calc_pro_month(number01, number02,number03))

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

