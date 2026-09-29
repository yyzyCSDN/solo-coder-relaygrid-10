from __future__ import annotations

def transferable_kw(tie_ampacity_a: float,kv_ll: float,power_factor: float,source_headroom_kw: float,receiving_need_kw: float):
    if tie_ampacity_a < 0 or kv_ll <= 0: raise ValueError("invalid tie capacity")
    if not 0 <= power_factor <= 1: raise ValueError("power factor out of range")
    if source_headroom_kw < 0 or receiving_need_kw < 0: raise ValueError("negative transfer limit")
    thermal=1.7320508075688772*kv_ll*tie_ampacity_a*power_factor
    return max(0.0,min(thermal,source_headroom_kw,receiving_need_kw))

def rank_ties(ties):
    return sorted(ties,key=lambda x:(-x[1],x[0]))
