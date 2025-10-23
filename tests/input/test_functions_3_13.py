# tests/version_aware_make_function_3_9_13.py (decompiled from Python 3.13)
from __future__ import annotations
from typing import List, Dict, Optional, Any, Callable

def pos_defaults(a=10, b=20):
    return a + b

def kw_defaults(*, x=30, y=40):
    return x * y

def mixed_defaults(p, q=5, *args, r=6, **kwargs):
    return p + q + sum(args) + r + len(kwargs)

def kw_only(a, *, b, c=7):
    return a + b + c

def kw_only_defaults(*, m=8, n=9):
    return m - n

def annotated(a: int, b: str = 'hi') -> float:
    return float(a) + len(b)

def annot_kw_only(*, x: List[int] = [1, 2], y: Dict[str, Any]) -> None:
    print(x, y)

def forward_ref(f: 'FutureType') -> 'Result':
    return f

def outer_simple():
    secret = 42
    def inner():
        return secret
    return inner

def outer_with_defaults(base=100):
    def inner(delta):
        return base + delta
    return inner

def outer_annotated():
    mul: int = 5
    def inner(x: int) -> int:
        return mul * x
    return inner

def outer_nested():
    outer = 'OUT'
    def mid():
        mid = 'MID'
        def inner():
            return outer + mid
        return inner
    return mid()

def kitchen_sink(pos: int, pos_def: str = 'def', *varargs: float, kw_only: bool = True, kw_annot: Optional[Dict] = None, **kwargs: Any) -> List[str]:
    result = [pos_def] * pos
    if kw_only:
        result.extend(str(v) for v in varargs)
    if kw_annot:
        result.extend(kw_annot.keys())
    result.extend(str(v) for v in kwargs.values())
    return result

def closure_with_lambda():
    offset = 10
    return lambda x: x + offset

def empty_defaults(a=(), b={}):
    return a, b

def empty_annot() -> None:
    pass

# Note: type_param_placeholder[T]() uses PEP 695 (Python 3.12+), but in 3.13
# it emits MAKE_FUNCTION with flag 0x10. PR #581 safely ignores unknown flags.
def type_param_placeholder[T]():
    return T
