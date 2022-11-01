class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):                            # hasattr 'instance'가 있는지 확인하여 True, False 반환
            cls.instance = super(Singleton, cls).__new__(cls)       # super(Singleton, cls)는 실행할때마다 메모리 다른곳에 올리던데
        return cls.instance                                         # super() 이렇게하면 실행해도 같은곳에 올라가 있던데 의미가 있을 듯

s = Singleton()
print("Object created", s)

s1 = Singleton()
print("Object created", s1)
