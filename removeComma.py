import re 
import csv

print("\n★ ★ ★ ★ ★\t콤마(,) 제거기\t★ ★ ★ ★ ★\n")
print('입력은 확장자 제외한 파일명만 넣으면 됩니다. (CSV파일 전용)\n')
st1 = input("파일 이름 입력 : ")
print("변환될 파일의 이름은 {}입니다.\n".format(st1+"_out.csv"))

try:
    f = open(st1+".csv")                        # 불러올 csv 파일
    r = open((st1+"_out.csv"), 'w', newline='')    # 생성할 csv 파일, 위와 같은 이름으로 설정하면 파일 날아감.
    k = []
    data = csv.reader(f)
    wr = csv.writer(r)
    for row in data :
        for i in row :
            if re.search('[a-z가-힣]', i) :
                index = i
            else :
                index = re.sub(',','',i)
            k.append(str(index))
        wr.writerow(k)
        k = []
    print("제거 성공")
except FileNotFoundError as e:
    print("제거 실패", e)
    print("파일이 없거나 찾을 수 없습니다.\n")
    print("이 코드는 사용할 파일과 같은 디랙터리에 있어야합니다.\n")
except Exception as e:
    print("제거 실패", e)
    print()

print("작업 종료")

