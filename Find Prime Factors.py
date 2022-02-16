def primefactors(n):
  f = 2
  Prime_factors = []
  while n ** 0.5 > f:
      if n % f != 0:
          f = f + 1
      elif n % f == 0:
          Prime_factors.append(f)
          n = int(n / f)
          f = f + 1
  Prime_factors.append(n)
  return Prime_factors
