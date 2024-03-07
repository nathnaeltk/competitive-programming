count, url = "1234 discuss.leetcode.com".split(' ')
print(f'count: {count} url: {url}')

lasttwoparsofurl = url.split('.')[-2:]
print(f'lasttwoparsofurl: {lasttwoparsofurl}')