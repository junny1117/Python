_st = [] 

class Student():

    def __init__(self):
        pass
    def register(self, index, st_id, st_pass, st_num, st_name, st_dept, st_year, st_code):
        _st[index].append(st_id)
        _st[index].append(st_pass)
        _st[index].append(st_num)
        _st[index].append(st_name)
        _st[index].append(st_dept)
        _st[index].append(st_year)
        _st[index].append(st_code)

class Sugang():
    def __init__(self):
        pass

    def add_sugang_list(self,st_id,code):
        self.f_index = self.search_index(st_id)
        _st[self.f_index][6] = code

    def search_index(self, st_id):
        self.i=-1
        for chk in range(len(_st)):
            if st_id in _st[chk]:
                self_i = chk
            return self.i

    def search_id(self, st_id):
        self.mark = False
        for chk in range (len(_st)):
            if st_id in _st[chk][0]:
                self.mark = True
                break
        return self.mark

    def search_pass(self, st_id):
        self.f_index = self.search_index(st_id)
        return _st[self.f_index][1]
    
    def get_code(self, st_id):
        self.f_index = self.search_index(st_id)
        return _st[self.f_index][6]



            

