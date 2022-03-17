def solution(sizes):
    w=[max(size[0],size[1]) for size in sizes]
    h=[min(size[0],size[1]) for size in sizes]
    w.sort(reverse=True)
    h.sort(reverse=True)
    return w[0]*h[0]