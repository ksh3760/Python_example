# 로또 번호 생성
import random

# 방법1
if 0:
    def lotto():
        numList = list(range(1, 46))
        random.shuffle(numList)
        for i in range(1, 7):
            print(numList[i], end=' ', )
        print()


    lotto()

# 방법2
if 0:
    def lotto2():
        ok = set()

        while True:
            ok.add(random.randint(1, 45))
            if len(ok) == 6: break
        return ok


    print(lotto2())

    lotto2()