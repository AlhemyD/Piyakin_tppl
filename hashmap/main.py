import re

class SpecialDict(dict):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)    
    
    @property
    def iloc(self):
        sorted_keys = sorted(self.keys())
        return [self[k] for k in sorted_keys]

    def ploc(self, condition):
        alphabet="<>=.0987654321 (),"
        if any([i not in alphabet for i in condition]):
            raise ValueError
        return self._filter_by_condition(condition)

    
    def _convert_to_float(self, key):
        try:
            return float(key)            
        except ValueError:
            return float('nan')

    def _filter_by_condition(self, condition):
        condition_parts = condition.split(',')
        filtered = {}

        for key, value in self.items():
            match = re.match(r'^\((.*)\)$', key)
            
            if match: 
                sub_keys = match.group(1).split(',')
            else: 
                sub_keys = re.split(r'[,s]+', key)
            
            if len(sub_keys) != len(condition_parts):
                continue
            
            if all(self._evaluate_condition(self._convert_to_float(sub_key.strip()), cond.strip()) 
                   for sub_key, cond in zip(sub_keys, condition_parts)):
                filtered[key] = value

        return filtered
    

    def _evaluate_condition(self, value, condition):
        if '<=' in condition:
            return value <= float(condition.replace('<=', '').strip())
        elif '<>' in condition:
            return value != float(condition.replace('<>', '').strip())
        elif '<' in condition:
            return value < float(condition.replace('<', '').strip())
        elif '>=' in condition:
            return value >= float(condition.replace('>=', '').strip())
        elif '>' in condition:
            return value > float(condition.replace('>', '').strip())
        elif '=' in condition:
            return value == float(condition.replace('=', '').strip())
_map2=SpecialDict()
_map2["value1"] = 1
_map2["2"] = 20
print(_map2.ploc("<>2"))
