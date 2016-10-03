
def yy (n):
    for i in range(n):
        yield i

a = yy(10)
print(a)

for i in a:
    print (i)

'''#content > div > div.article > div:nth-child(2) > table:nth-child(2) > tbody > tr > td:nth-child(2) > div > a
   //*[@id="content"]/div/div[1]/div[2]/table[1]/tbody/tr/td[2]/div/a/span '''