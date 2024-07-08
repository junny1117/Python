_cls = []

class Cls():
    def __init__(self):
        pass
    def register(self, index, cls_code, cls_year,Cls_semester, cls_lecture, cls_credit, cls_tot, cls_subscription):
        _cls[index].append(cls_code)
        _cls[index].append(cls_year)
        _cls[index].append(Cls_semester)
        _cls[index].append(cls_lecture)
        _cls[index].append(cls_credit)
        _cls[index].append(cls_tot)
        _cls[index].append(cls_subscription)

class Manage():
    def __init__(self):
        pass
    def add_subscription(self, cls_code):
        self.f_index = self.search_index(cls_code)
        if _cls[self.f_index][5]<=_cls[self.f_index][6]:
            print("수강인원이 모두 찼습니다.")
            return False
        else: 
            print("수강신청이 되었습니다")
            _cls[self.f_index][6]+=1
            return True

    def search_index(self, cls_code):
        self.i=1
        for chk in range(len(_cls)):
            if cls_code in _cls[chk]:
                self.i = chk
        return self.i
    def search_code(self, cls_code):
        self.mark = False
        for chk in range(len(_cls)):
            if cls_code in _cls[chk][0]:
                self.mark = True
                break
        return self.mark
    
    def get_lecture(self, cls_code):
        self.f_index = self.search_index(cls_code)
        return _cls[self.f_index][3]

    def get_tot(self, cls_code):
        self.f_index = self.search_index(cls_code)
        return _cls[self.f_index][5]

    def get_tot(self, cls_subscription):
        self.f_index = self.search_index(cls_code)
        return _cls[self.f_index][6]
