import pandas as p
import numpy as n
from scipy.stats import norm

def main():
    r = 102303684
    f = "data 2.csv"
    a = 0.05 * (r % 7)
    b = 0.3 * ((r % 5) + 1)
    
    print(f"R: {r}")
    print(f"A: {a}")
    print(f"B: {b}")
    
    try:
        d = p.read_csv(f, encoding='latin1')
    except Exception:
        return

    if 'no2' not in d.columns:
        return
        
    d['no2'] = p.to_numeric(d['no2'], errors='coerce')
    x = d['no2'].dropna().values
    
    z = x + a * n.sin(b * x)
    
    m, s = norm.fit(z)
    
    l = 1 / (2 * s**2)
    c = 1 / (s * n.sqrt(2 * n.pi))
    
    print("-" * 20)
    print(f"M: {m}")
    print(f"S: {s}")
    print(f"L: {l}")
    print(f"C: {c}")
    print("-" * 20)
    
if __name__ == "__main__":
    main()
