from Injective import Injective

NAME_TO_CODE = \
'''Alabama,AL
Alaska,AK
Arizona,AZ
Arkansas,AR
California,CA
Colorado,CO
Connecticut,CT
Delaware,DE
District of Columbia,DC
Florida,FL
Georgia,GA
Hawaii,HI
Idaho,ID
Illinois,IL
Indiana,IN
Iowa,IA
Kansas,KS
Kentucky,KY
Louisiana,LA
Maine,ME
Montana,MT
Nebraska,NE
Nevada,NV
New Hampshire,NH
New Jersey,NJ
New Mexico,NM
New York,NY
North Carolina,NC
North Dakota,ND
Ohio,OH
Oklahoma,OK
Oregon,OR
Maryland,MD
Massachusetts,MA
Michigan,MI
Minnesota,MN
Mississippi,MS
Missouri,MO
Pennsylvania,PA
Rhode Island,RI
South Carolina,SC
South Dakota,SD
Tennessee,TN
Texas,TX
Utah,UT
Vermont,VT
Virginia,VA
Washington,WA
West Virginia,WV
Wisconsin,WI
Wyoming,WY'''

name_to_code = Injective()

def main() -> None:
    for row in NAME_TO_CODE.split('\n'):
        split_row = row.split(',')
        name_to_code[split_row[0]] = split_row[1]

    code_to_name = name_to_code.inverse()
    while True:
        entry = input('Enter state name, code or exit:')
        if entry.casefold() == 'exit'.casefold():
            break
        if entry in name_to_code:
            print(name_to_code[entry])
        elif entry in code_to_name:
            print(code_to_name[entry])
        else:
            print(f'Code/Name {entry} not found')


if __name__ == '__main__':
    main()
