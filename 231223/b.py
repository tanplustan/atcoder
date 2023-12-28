A, M, L, R = map( int, input().split() )
distance = R - L
mod = ( A - L ) % M
total = ((distance - mod) // M) + 1
print(total)