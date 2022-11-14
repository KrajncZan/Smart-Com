import dns.resolver

def A():
    result = dns.resolver.resolve('www.youtube.com', 'A')
    for ipval in result:
        print('IP', ipval.to_text())

def CNAME():
    result = dns.resolver.resolve('www.youtube.com', 'CNAME')
    for cnameval in result:
        print('CNAME target address:', cnameval.target)

def MX():
    result = dns.resolver.resolve('mail.google.com', 'NS')
    #print(result)
    for exdata in result:
        print('MX Record:', exdata.to_text())
A()
print("-" * 20)
CNAME()
print("-" * 20)
#MX()
