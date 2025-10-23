from __future__ import annotations
from typing import List, Dict, Optional, Any, TypeVar

T = TypeVar('T')
A = TypeVar('A')

def pos_defaults(a=10,b=20):
    return a+b

def kw_defaults(*,x=30,y=40):
    return x*y

def mixed_defaults(p,q=5,*args,r=6,**kwargs):
    return p+q+sum(args)+r+len(kwargs)

def kw_only(a,*,b,c=7):
    return a+b+c

def kw_only_defaults(*,m=8,n=9):
    return m-n

def annotated(a:int,b:str='hi')->float:
    return float(a)+len(b)

def annot_kw_only(*,x:List[int]=[1,2],y:Dict[str,Any])->None:
    print(x,y)

def forward_ref(f:'FutureType')->'Result':
    return f

def outer_simple(secret=42):
    return secret

def outer_with_defaults(delta, base=100):
    return base+delta

def outer_annotated(x, mul=5):
    return mul*x

def outer_nested(outer='OUT', mid='MID'):
    return outer+mid

def kitchen_sink(pos:int,pos_def:str='def',*varargs:float,kw_only:bool=True,kw_annot:Optional[Dict]=None,**kwargs:Any)->List[str]:
    result=[pos_def]*pos
    if kw_only:
        result.extend(str(v) for v in varargs)
    if kw_annot:
        result.extend(kw_annot.keys())
    result.extend(str(v) for v in kwargs.values())
    return result

def closure_with_lambda(x, offset=10):
    return x+offset

def empty_defaults(a=(),b={}):
    return a,b

def empty_annot()->None:
    pass

def type_param_placeholder()->T:
    return T

class Frt:
    @staticmethod
    def cb(a:A) -> A:
        return a
