#!/usr/bin/env python
from secret import flag
from Crypto.Hash import SHA256
from Crypto.Util.number import *
from Crypto.Cipher import AES
from Crypto.PublicKey import DSA
message = b"We1c0me to My DSA~"

key = DSA.generate(2048)
g = key.g
p = key.p
q = key.q
x = key.x

y = pow(g,x,p)

def pad(mes):
    return mes+b'\x00'*(16-(len(mes)%16))

def sign(m, sk):
    k = getRandomInteger(210)
    r = pow(g, k, p) % q
    h = int(SHA256.new(m).hexdigest(),16)
    s = (pow(k,-1, q) * (h + sk * r)) % q
    return (r,s)

def verify(m, sig, pk):
    r, s = sig
    if not (0 < r < q) or not (0 < s < q):
        return False
    h = int(SHA256.new(m).hexdigest(),16)
    w = pow(s,-1, q)
    u1 = (w * h) % q
    u2 = (w * r) % q
    v = ( (pow(g, u1, p) * pow(pk, u2, p)) % p ) % q
    
    return v == r

f = open("result.txt",'w')
for i in range(19):
    s = sign(message, x)
    f.write(str(s)+'\n')
    assert(verify(message,s,y))


hash = SHA256.new(long_to_bytes(x)).hexdigest()
key, iv =int(hash[:32],16),int(hash[32:],16)
Cry = AES.new(key=long_to_bytes(key),iv=long_to_bytes(iv),mode=AES.MODE_CBC)
Cip = Cry.encrypt(pad(flag))
print("y = %d"%y)
print("g = %d"%g)
print("p = %d"%p)
print("q = %d"%q)
print(Cip)

# cipher = b'\x95\xf7\xa4\xec\xd9X\x83\x8b\x07\x80\xfe\x13\x1f\xb7\xbc\xdb>D\xd9\x81\xea \xde\xa4\xe2\x1dqbVh\x05\x7fSql\xcb\xbc>\xa7\x97\xc43\xf5\x9b\x007$\xc9'
# y = 10865252628977982718403069421818763814235837963131657427013029838115823600026336301447650009296905255642313560614829551414305461349368310042639287174589738371871741669394848449628044522285747368712081660541770583698167114808057698350786229602723897528207412571691070008591305998686441545245935074526540367888505082808339119240505754542244988927696478960460825964816624418555049437463940360457911924601327318567655697900820622946726145105652407044994786590422434786210702091749354399109010238703002733213717843576865823660052640934212789357807787991082174138275574313009398721223181931145132115294972007801753173408741
# g = 10878177066786201817104669144134368086712364755276065919108711478199751092510166851087043647216283625336810425197547358392780958373012106267072258504608165416441218758023152298309265892294553201074526777067230246439537417511861809178218169256652718105178190531196938563066075049513162080607898394164761142987189540919834231524565226906188464783536188862914987217998962718991606850419980530798524804129840222467271485055647515909053842052939260751746609937602730547514994036006926590348766594949197409442317049666999374778475862558340612771396592183794892824814325810064157857169327255025279120759002239011771662085338
# p = 20384762745031920484342583090217007578889531799944456287350542020280428183544133614297677240387166875661657848083207276915863377102624811969097780972047544492418067487713520174772431897063705267454857523565989648021927658166607167532208110984841922116249828872341082286532560521732253899817674270499471088325222125596455980431820124332946754612276146984417926433629287154223788213445218119081147675710811509544642585633492685907180108137818208905518403931854775047349966947896551628689905814775976869615951137482223176231926274859815993780667146033144320174578733368829000886681042308444467510423523202661128031456749
# q = 16059555483679266293519046196529336235978742561121132269882524559139
