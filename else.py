def strength(rm): # 스트렝스 프로그램 함수
    result = [
        {'program':'5곱5', 'weight':str(rm*.8)+'KG','break':'3분~3분30초'},
        {'program':'3곱5','weight':str(rm*.85)+'KG','break':'3분30초~5분'}
        ]
    return result

def mass(rm): # 근비대 프로그램 함수
    result = [
        {'program':'10곱5','weight':str(rm*.7),'break':'1분30초~2분30초'},
        {'program':'8곱5','weight':str(rm*75),'break':'2분~3분'}
    ]
    return result
