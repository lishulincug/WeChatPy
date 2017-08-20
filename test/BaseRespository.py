
'''
Repository
数据持久化基础类
'''

class BaseRespository:
    db = None

    def __init__(self):
        pass

    def save(self,obj):
        pass

    def update(self,obj):
        pass

    def delete(self,key):
        pass