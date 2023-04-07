import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 332487463 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    
    alpha = 1 - p
    
    m = max(x)
    n = len(x)
    
    def f(q):
        return (2 * n * m - 2 * np.log(1 - q) - n) / (2 * 72 * n)
    
    
    
    return f(0), f(p)
