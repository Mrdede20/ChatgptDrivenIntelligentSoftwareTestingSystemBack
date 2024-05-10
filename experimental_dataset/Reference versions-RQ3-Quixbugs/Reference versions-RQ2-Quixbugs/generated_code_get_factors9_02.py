
def get_factors(n):
    def factor_helper(n, factor):
        if n == 1:
            return []
        elif n % factor == 0:
            return [factor] + factor_helper(n//factor, factor)
        else:
            return factor_helper(n, factor+1)
        
    return factor_helper(n, 2)
