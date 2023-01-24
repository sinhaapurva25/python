def fun(s):
    # return True if s is a valid email, else return False
    idx_at_the_rate = s.find('@')
    idx_dot = s.find('.')
    # print(idx_at_the_rate, idx_dot)
    if idx_at_the_rate > -1 and idx_dot > -1:
        username = s[:idx_at_the_rate]
        websitename = s[idx_at_the_rate+1:idx_dot]
        extension  = s[idx_dot+1:]
        # print(username,websitename,extension)
        if username.isalnum() or username.find('_') > -1 or username.find('-') > -1:
            if websitename.isalnum():
                if extension.isalpha() and len(extension) <=3:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)