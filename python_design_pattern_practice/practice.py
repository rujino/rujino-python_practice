class Calc:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        print(self.n1 + self.n2)

    def __call__(self, n1, n2):  # __call__ 이미 존재하는 객체를 생성할때 호출되는 파이썬의 특수 메소드
        self.n1 = n1
        self.n2 = n2
        print(self.n1 + self.n2)


s = Calc(5, 5)

s(10, 5)
