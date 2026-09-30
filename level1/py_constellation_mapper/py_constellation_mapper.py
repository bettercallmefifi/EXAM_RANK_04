def constellation_mapper(start: list[tuple[int, int]], dim: int) -> list[str]:
    grille = [['.'] * dim for _ in range(dim)]
    for ligne , col in start:
        if ligne in range(dim) and col in range(dim):
            grille[ligne][col] = '*'
    rst = []
    for ligne in grille:
        rst.append(''.join(ligne))
    return rst
