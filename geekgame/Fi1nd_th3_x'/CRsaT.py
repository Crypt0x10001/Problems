from Crypto.Util.number import *
from libnum import* 
from secret import flag

p = getPrime(512)
q = getPrime(512)
r = getPrime(512)
e = getPrime(32)
n = p*q*r
phi = (p-1)*(q-1)*(r-1)
d = inverse(e,phi)
dP = d%((q-1)*(r-1))
dQ = d%((p-1)*(r-1))
dR = d%((p-1)*(q-1))
m = s2n(flag.encode())
c = pow(m,e,n)

print('p=',p)
print('q=',q)
print('r=',r)
print('dP=',dP)
print('dQ=',dQ)
print('dR=',dR)
print('c=',c)

'''
p= 13014610351521460822156239705430709078128228907778181478242620569429327799535062679140131416771915929573454741755415612880788196172134695027201422226050343
q= 12772373441651008681294250861077909144300908972709561019514945881228862913558543752401850710742410181542277593157992764354184262443612041344749961361188667
r= 12128188838358065666687296689425460086282352520167544115899775800918383085863282204525519245937988837403739683061218279585168168892037039644924073220678419
dP= 116715737414908163105708802733763596338775040866822719131764691930369001776551671725363881836568414327815420649861207859100479999650414099346914809923964116101517432576562641857767638396325944526867458624878906968552835814078216316470330511385701105459053294771612727181278955929391807414985165924450505855941
dQ= 44209639124029393930247375993629669338749966042856653556428540234515804939791650065905841618344611216577807325504984178760405516121845853248373571704473449826683120387747977520655432396578361308033763778324817416507993263234206797363191089863381905902638111246229641698709383653501799974217118168526572365797
dR= 60735172709413093730902464873458655487237612458970735840670987186877666190533417038325630420791294593669609785154204677845781980482700493870590706892523016041087206844082222225206703139282240453277802870868459288354322845410191061009582969848870045522383447751431300627611762289800656277924903605593069856921
c= 93063188325241977486352111369210103514669725591157371105152980481620575818945846725056329712195176948376321676112726029400835578531311113991944495646259750817465291340479809938094295621728828133981781064352306623727112813796314947081857025012662546178066873083689559924412320123824601550896063037191589471066773464829226873338699012924080583389032903142107586722373131642720522453842444615499672193051587154108368643495983197891525747653618742702589711752256009
'''


