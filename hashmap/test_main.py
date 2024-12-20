import pytest
from main import SpecialDict


class TestSpecialDict:

    def test_assign(self):
        _map=SpecialDict({"alice":2})
        _map["value1"]=1
        _map[0]=4
        assert _map["value1"]==1
        assert _map["alice"]==2
        assert _map[0]==4
    def test_iloc(self):
        _map=SpecialDict({"alice":2,"1":14,"(1,5)":200})
        assert _map.iloc[0]==200
        assert _map.iloc[2]==2
    def test_ploc(self):
        _map=SpecialDict()
        _map["value1"] = 1
        _map["value2"] = 2
        _map["value3"] = 3
        _map["1"] = 10
        _map["2"] = 20
        _map["3"] = 30
        _map["(1, 5)"] = 100
        _map["(5, 5)"] = 200
        _map["(10, 5)"] = 300
        _map["(1, 5, 3)"] = 400
        _map["(5, 5, 4)"] = 500
        _map["(10, 5, 5)"] = 600
        _map2=SpecialDict()
        _map2["value1"] = 1
        _map2["2"] = 20     
        assert _map.ploc(">=1")=={"1":10,"2":20,"3":30}
        assert _map.ploc(">0,>0")=={"(1, 5)":100,"(5, 5)":200,"(10, 5)":300}
        assert _map.ploc(">0,>0,>0,<0")=={}
        assert _map.ploc("<=2")=={"1":10,"2":20}
        assert _map.ploc("<2")=={"1":10}
        assert _map.ploc("=2")=={"2":20}
        print(_map2.ploc("<>2,<>5"))
        assert _map2.ploc("<>2,<>5")=={}
        
    def test_error(self):
        _map=SpecialDict()
        _map["value1"] = 1
        _map["value2"] = 2
        _map["value3"] = 3
        _map["1"] = 10
        _map["2"] = 20
        _map["3"] = 30
        _map["(1, 5)"] = 100
        _map["(5, 5)"] = 200
        _map["(10, 5)"] = 300
        _map["(1, 5, 3)"] = 400
        _map["(5, 5, 4)"] = 500
        _map["(10, 5, 5)"] = 600
        with pytest.raises(ValueError):
            _map.ploc("!")
            
        
            
