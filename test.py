def balanceable_rec(L, R, weights):
    print("L =", L, "  R =", R, "  weights =", weights)

    if L == 0 or L == R or L in weights:
        return True

    if len(weights) == 0:
        return False

    w = weights.pop(0)
    if balanceable_rec(L + w, R, weights[:]):
        return True
    if balanceable_rec(L, R, weights[:]):
        return True
    if balanceable_rec(L, R + w, weights[:]):
        return True

    return False
