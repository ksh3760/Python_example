def convertUL(msg):
    """
    입력받은 영문 문자에 대소문자 변환 기능함수
    :param msg: 입력받은 문자열
    :return: 대소문자 변환
    """
    msg2 = ""
    for ch in msg:
        if ord('A') <= ord(ch) <= ord('Z'):  # 대문자
            msg2 = msg2 + ch.lower()  # 소문자로 변환
        elif ord('a') <= ord(ch) <= ord('z'):
            msg2 = msg2 + ch.upper()  # 대문자로 변환

    return msg2


strdata = convertUL("Hello World")
print(strdata)
print(convertUL.__doc__)  # 함수의 설명을 보고싶을때 사용