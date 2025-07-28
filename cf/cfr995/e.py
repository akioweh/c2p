from sys import stdin, stdout

# noinspection PyShadowingBuiltins
input = stdin.readline


def read_ints():
    return map(int, input().split())


T = int(input())

for _ in range(T):
    n_customers, max_neg_reviews = read_ints()
    a_s = list(read_ints())
    b_s = list(read_ints())
    a_s.sort()
    b_s.sort()

    idx_a = 0
    idx_b = 0

    cur_sales = n_customers
    cur_neg = 0
    best_rev = 0
    prev_type, prev_price = False, 0
    while idx_a < n_customers or idx_b < n_customers:
        if idx_a == n_customers:
            cur_price = b_s[idx_b]
            idx_b += 1
            neg_review = False
        elif idx_b == n_customers:
            cur_price = a_s[idx_a]
            idx_a += 1
            neg_review = True
        else:  # merge sort
            cur_a, cur_b = a_s[idx_a], b_s[idx_b]
            if cur_a <= cur_b:
                idx_a += 1
                cur_price = cur_a
                neg_review = True
            else:
                idx_b += 1
                cur_price = cur_b
                neg_review = False

        if cur_neg <= max_neg_reviews and (neg_review != prev_type or cur_price != prev_price):
            prev_rev = cur_price * cur_sales
            if prev_rev > best_rev:
                best_rev = prev_rev

        prev_type, prev_price = neg_review, cur_price

        cur_neg += 1 if neg_review else -1
        if not neg_review:
            cur_sales -= 1

    stdout.write(f'{best_rev}\n')
