import requests

url = 'http://ec2-3-34-4-109.ap-northeast-2.compute.amazonaws.com:8000'
def print_mechanic(result):
    print('[MECHANIC]')
    print("---------------------------------------------------------------------------------------------------------")
    m_info = ['ID', '정비공 이름', 'MON', 'TUE', 'WED', 'THU', 'FRI']
    for m in m_info:
        print(m.center(8, ' '), end='\t')
    print("\n---------------------------------------------------------------------------------------------------------")
    m_codes = ['mechanic_id', 'mechanic_name', 'MON', 'TUE', 'WED', 'THU', 'FRI']
    for r in result:
        for c in m_codes:
            print(str(r[c]).center(8, ' '), end='\t')
        print(" ")
    print("---------------------------------------------------------------------------------------------------------")

def print_customer(result):
    print('[CUSTOMER]')
    print("-----------------------------------------------------------")
    m_info = ['고객ID', '고객명', '전화번호', '생년월일']
    for m in m_info:
        print(m.center(10, ' '), end='\t')
    print("\n-----------------------------------------------------------")
    m_codes = ['cust_id', 'cust_name', 'cust_phone', 'cust_birth']
    for r in result:
        for c in m_codes:
            print(str(r[c]).center(10, ' '), end='\t')
        print(" ")
    print("-----------------------------------------------------------")

def print_car(result):
    print('[CAR]')
    print("--------------------------------------------------------------------------")
    m_info = ['ID', '자동차명', '색상', '제조국가', '판매상태']
    for m in m_info:
        print(m.center(8, ' '), end='\t')
    print("\n--------------------------------------------------------------------------")
    m_codes = ['car_id', 'car_name', 'color', 'made_by','sales']
    for r in result:
        for c in m_codes:
            print(str(r[c]).center(8, ' '), end='\t')
        print(" ")
    print("--------------------------------------------------------------------------")
def print_invoice(result):
    print('[INVOICE]')
    print("-----------------------------------------------")
    m_info = ['구매번호', '직원ID', '고객ID', '자동차ID']
    for m in m_info:
        print(m.center(1, ' '), end='\t')
    print("\n-----------------------------------------------")
    m_codes = ['invoice_number', 'sales_id', 'cust_id', 'car_id']
    for r in result:
        for c in m_codes:
            print(str(r[c]).center(5, ' '), end='\t')
        print(" ")
    print("-------------------------------------------------")

def print_part(result):
    print('[PART]')
    print("-----------------------------------------------")
    m_info = ['부품ID', '부품명', '가격']
    for m in m_info:
        print(m.center(5, ' '), end='\t')
    print("\n-----------------------------------------------")
    m_codes = ['part_id', 'part_name', 'price']
    for r in result:
        for c in m_codes:
            print(str(r[c]).center(5, ' '), end='\t')
        print(" ")
    print("-------------------------------------------------")

while True:
    print('\n=============================================')
    carstr=' CAR DEALER SHOP '
    print(carstr.center(40, ' '),end='\t')
    print('\n=============================================')
    try:
        cmd=int(input('\t1) 고객 정보\n\t2) 자동차 정보\n\t3) 자동차 구매\n\t4) 자동차 서비스\n\t5) 종료 \n\t**번호를 입력해주세요(1~5) -> '))
    except:
        print('**메뉴는 1~5사이의 숫자만 입력해주세요.**')
        continue

    if cmd==1: #고객정보
        print('\n\t<고객정보 메뉴입니다.>')
        try : 
            cmd=int(input('\t1) 고객 정보 입력\n\t2) 고객정보 조회\n\t3) 고객정보 수정\n\t4) 고객정보 삭제\n\t5) 메인으로 이동 \n\t**메뉴를 입력해주세요(1~5) -> '))
        except:
            print('**1~5사이의 숫자만 입력해주세요. **')
            continue

        if cmd==1: #고객입력
            # print('\t신규 고객정보를 입력하세요.')
            cust_name=input('\t이름 : ')
            cust_phone=input('\t핸드폰 번호(010-0000-0000) : ')
            cust_birth=input ('\t생년월일(6자리) : ')

            data = {
                'cust_name': cust_name, 
                'cust_phone': cust_phone, 
                'cust_birth': cust_birth
            }
            res = requests.post(url + "/Customer/insert", data=data)


        elif cmd==2: #고객조회
            print('\t현재 고객정보를 조회합니다.')
            response = requests.get(url + "/Customer/select")
            print_customer(response.json())

        elif cmd==3: #고객수정
            print('\t고객정보를 수정합니다. 현재 데이터를 출력합니다.')
            response = requests.get(url + "/Customer/select")
            print_customer(response.json())

            update=input('\t수정하고 싶은 고객의 ID를 입력해주세요 -> ')
            newName=input('\t새로운 이름을 입력해주세요 -> ')
            newPhone=input('\t새로운 번호를 입력해주세요 -> ')
            newBirth=input('\t새로운 생년월일을 입력해주세요 -> ')
            data = {
                'cust_name': newName, 
                'cust_phone': newPhone, 
                'cust_birth': newBirth,
                'cust_id': update
            }
            res = requests.post(url + "/Customer/update", data=data)
            print('\t{}번 고객의 데이터가 수정되었습니다.'.format(update))
            continue
            
        elif cmd==4:#고객삭제
            cust_id=input('\t고객정보를 삭제합니다. 고객ID를 입력해주세요 ->')
            data = {
                'cust_id': cust_id, 
            }
            response = requests.delete(url + "/Customer/delete", data=data)
            print('\t데이터가 삭제되었습니다. \n\t[현재 고객 정보]')
            response = requests.get(url + "/Customer/select")
            print_customer(response.json())
            continue

        elif cmd==5:
                breakpoint
    
    elif cmd == 2: #자동차정보
        print('\n\t<자동차정보 메뉴입니다.>')
        try:
            cmd_car = int(input('\n\t1) 자동차 등록\n\t2) 자동차 검색 \n\t3) 자동차 정보 변경 \n\t4) 자동차 정보 삭제 \n\t**번호를 입력해주세요(1~4)-> '))
        except:
            print('\t**1~4 사이의 숫자만 입력해주세요.**')
            continue

        if cmd_car==1: #자동차 등록
            
            print('\t신규 자동차 정보를 입력해주세요.')
            # @app.route('Car/insert', methods=['POST'])
            car_name = input('\t자동차 이름 : ')
            color = input('\t색상 : ')
            made_by = input('\t제조국가 : ')
            car_data = {
                'car_name':car_name,
                'color':color,
                'made_by' : made_by
            }
            res = requests.post(url+"/Car/insert", data=car_data)
            # res = requests.post(url_car_insert, data=car_data)
            print("\t해당 데이터의 입력이 완료되었습니다. 현재 데이터를 출력합니다.\n") 
            response = requests.get(url+'/Car/select')
            print_car(response.json())


        if cmd_car==2: #자동차
            try:
                cmd_car_search = int(input('\n\t1) 자동차 전체 보기\n\t2) 특정 자동차 검색\n\t**번호를 입력해주세요(1~2) -> '))
            except:
                print('\t**번호는 1,2번만 입력해주세요.**')
                continue

            if cmd_car_search==1:
                print('\t현재 자동차정보를 조회합니다.')
                response = requests.get(url+'/Car/select')
                print_car(response.json())
                
            elif cmd_car_search == 2: #2-2 특정 검색
                car_name = input('\t**검색할 자동차의 이름을 입력해주세요 : ')
                data={
                    'car_name': car_name
                }
                response = requests.post(url+'/Car/select/name', data=data)
                print_car(response.json())
                # print(response.json())
        
        if cmd_car==3: # 자동차 정보 수정
            print('\t자동차 정보를 수정합니다. 현재 데이터를 출력합니다.')
            response = requests.get(url + "/Car/select")
            print_car(response.json())
            car_id = input('\t수정 할 자동차의 ID를 입력해주세요 : ')
            car_name=input('\t차 모델을 입력해주세요 : ')
            car_color=input('\t차 색상을 입력해주세요 : ')
            made_by=input('\t제조국가를 입력해주세요 : ')
            car_data = {
                'car_name':car_name,
                'color':car_color,
                'made_by' : made_by,
                'car_id' : car_id
            }
            res = requests.post(url+'/Car/update', data=car_data)
            print('\t{}번 자동차의 데이터가 수정되었습니다.'.format(car_id))
            print('\t현재 자동차정보를 조회합니다.')
            response = requests.get(url+'/Car/select')
            print(type(response))
            print_car(response.json())
        
        if cmd_car ==4: #자동차 삭제
            print('\t*** 자동차 정보를 삭제하면 구매목록에서 조회할 수 없습니다. 주의하세요! ***')
            car_id = int(input('\t삭제할 자동차의 ID를 입력해주세요 -> '))
            car_data={
                'car_id':car_id
            }
            response = requests.delete(url+'/Car/delete',data=car_data)
            
            print('\t{}번 자동차 정보가 삭제되었습니다.'.format(car_id))
            response = requests.get(url+'/Car/select')
            print_car(response.json())

    elif cmd==3: #자동차구매
        print('\n\t\t<자동차구매 메뉴입니다.>')
        print('현재 자동차 목록을 조회합니다. Sales 상태인 자동차만 구매 가능합니다.')
        response = requests.get(url + "/Car/select")
        print_car(response.json())

        cmd_car_buy = str(input('\t구매하시겠습니까? [yes] '))
        if cmd_car_buy == 'yes':
            InputCust = input('\t구매자의 ID를 입력하세요 : ')
            InputSalesman = input('\t판매자의 ID를 입력하세요 : ')
            InputCar = input('\t구매할 자동차의 ID를 입력하세요 : ') 
            
            data={
                'car_id': InputCar
            }
            response1 = requests.post(url + "/Car/select/id", data=data)
            print('car_id = ' + InputCar + ' ' + response1.json()[0]["sales"])

            if response1.json()[0]["sales"] == 'onSale' : # 자동차가 판매 중이면
                #Car에 있는 Sales 상태 sold out으로 변경
                res1 = requests.post(url+"/Car/update/sales", data=data)
                res2 = requests.post(url + "/Car/select/id", data=data)
                print_car(res2.json())

                print('\n**구매가 완료되었습니다. 아래 내역을 확인해주세요.')
                data2={
                    'cust_id': InputCust,
                    'sales_id': InputSalesman,
                    'car_id': InputCar
                }
                response3 = requests.post(url + "/Sales_invoice/insert", data=data2)
                response4 = requests.post(url + "/Sales_invoice/select/id", data=data2)
                print_invoice(response4.json())
            
            else : #자동차 sold out
                print('{}번 자동차는 현재 SOLD OUT입니다. 다른 자동차를 선택해주세요'.format(InputCar))
            continue

    elif cmd==4: #서비스
        print('\n\t<자동차서비스 메뉴입니다.>')
        response1 = requests.get(url + "/Sales_invoice/select")
        print_invoice(response1.json())
        invoiceNum=input('\t구매번호를 입력해주세요 : ')
        
        try:
            cmd_rsv = int(input('\n\t1) 예약가능날짜 조회하기 \n\t2) 예약하기 \n\t번호를 입력해주세요(1~2) -> '))
        except:
            print('\t**번호는 1~2사이의 숫자만 입력해주세요.**')
            continue

        if cmd_rsv == 1: #날짜 조회
            print('\t다음주 예약일정을 조회합니다.\n')
            response2 = requests.get(url + "/mechanics/select")
            print_mechanic(response2.json())

        elif cmd_rsv==2: #예약하기
            rsv_day = 0 #날짜 예약
            rsv_mec = 0 #정비공 예약
            print('\t다음주 예약 시간표입니다.')
            while True:
                response3 = requests.get(url + "/mechanics/select")
                print_mechanic(response3.json())
               
                rsv_mec = input('\t기술자를 선택해주세요\n\t1)Mechanic1 \n\t2)Mechanic2 \n\t3)Mechanic3 \n\t4)Mechanic4 \n\t**정비공 번호를 입력해주세요 ->  ')
                if rsv_mec != None:
                    rsv_day = input('\n\t요일을 입력 해주세요 ( MON, TUE, WED, THU, FRI) -> ')
                    
                    if rsv_day=='MON' or rsv_day=='TUE' or rsv_day=='WED' or rsv_day=='THU' or rsv_day=='FRI' :
                        data={
                            'day': rsv_day,
                            'mechanic_name': "Mec"+rsv_mec
                        }
                        response4 = requests.post(url + "/mechanics/select/name", data=data)

                        if response4.json()[0][rsv_day] == 'reserved' :
                            print('\n\t*** 이미 예약된 날짜입니다 다른 날을 선택해주세요 ***')
                            continue
                        break;
                    else:
                        print('\t제대로 입력해주세요\n')
                        continue

                else:
                    print('\t정비공 번호를 제대로 입력해주세요\n')
                    continue
            data2 = {
                'day': rsv_day,
                'mechanic_name': "Mec"+rsv_mec
            }
            response5 = requests.post(url + "/mechanics/update", data=data2)
            
            response6 = requests.get(url + "/mechanics/select")
            print_mechanic(response6.json())
            print('\t**예약이 완료되었습니다.')

    elif cmd ==5:
        quit()

    else:
        print('\n\t**메뉴는 1~5사이의 숫자만 입력해주세요.**')