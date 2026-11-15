import sys,json,os;from urllib.request import*;Y=os.getenv('MAKEFUN_ENV_URL');Q=5e4;V=0,100,320,330,500,900,0;N=-33,-31,-18,-14,14,18,31,33;J=-17,-16,-15,-1,1,15,16,17;D=-17,-15,15,17;R=-16,-1,1,16;I=0,0,N,D,R,D+R,J;B=[0]*128;S=1;W=4;X=116;T=0;C=0
def P(p,s):A=abs(p);C=s&7;B=s>>4;D=C*(7-C)+B*(7-B);E=(B if p>0 else 7-B)*6 if A==1 else D*2 if A<4 else-D*4 if A==6 else 0;return(V[A]+E)*p//abs(p)
def A(s,y):
	for A in(s-y*15,s-y*17):
		if not A&136 and B[A]==y:return 1
	for C in N+J:
		A=s+C
		if not A&136 and(B[A]==y*2 and C in N or B[A]==y*6 and C in J):return 1
	for C in D+R:
		A=s+C
		while not A&136:
			E=B[A]
			if E:
				if E==y*5 or E==y*3 and C in D or E==y*4 and C in R:return 1
				break
			A+=C
	return 0
def G(o=0):
	E=[]
	for C in range(128):
		if C&136:continue
		H=B[C]
		if H*S<=0:continue
		F=abs(H)
		if F==1:
			D=16*S;L=C>>4;M=7 if S==1 else 0
			for J in(D-1,D,D+1):
				A=C+J
				if A&136:continue
				K=C|A<<7|(5<<14 if A>>4==M else 0)
				if J==D:
					if not o and B[A]==0:
						E.append(K)
						if L==(1 if S==1 else 6)and B[C+2*D]==0:E.append(C|C+2*D<<7)
				elif B[A]*S<0 and abs(B[A])<6:E.append(K)
		else:
			for D in I[F]:
				A=C+D
				while not A&136:
					G=B[A]
					if G==0:
						if not o:E.append(C|A<<7)
					else:
						if G*S<0 and abs(G)<6:E.append(C|A<<7)
						break
					if F==2 or F==6:break
					A+=D
	return E
def M(m):
	global S,W,X,T;C=m&127;A=m>>7&127;F=m>>14;D=B[C];H=abs(D);E=B[A];I=W,X,T;T-=P(D,C)
	if E:T-=P(E,A)
	G=S*F if F else D;B[A]=G;B[C]=0;T+=P(G,A)
	if H==6:W,X=(A,X)if S==1 else(W,A)
	if H==6 and abs(A-C)==2:J=A+1 if A>C else A-2;K=A-1 if A>C else A+1;B[K]=B[J];B[J]=0
	S=-S;return(E,)+I
def U(m,u):
	global S,W,X,T;C=m&127;A=m>>7&127;D=m>>14;S=-S;W=u[1];X=u[2];T=u[3];E=B[A];B[C]=S if D else E;B[A]=0
	if u[0]:B[A]=u[0]
	if abs(E)==6 and abs(A-C)==2:J=A+1 if A>C else A-2;K=A-1 if A>C else A+1;B[J]=B[K];B[K]=0
def L(o=0):
	C=[]
	for B in G(o):
		D=M(B)
		if not A((W,X)[S>0],S):C.append(B)
		U(B,D)
	return C
def O(n):return V[abs(B[n>>7&127])]
def y():
	global C;C+=1
	if C>Q:1/0
def F(d,a,b,p):
	y()
	if d==0:
		if A((W,X)[S<0],-S):return F(1,a,b,p)
		C=T*S
		if C>=b:return b
		if C>a:a=C
		B=L(1)
	else:
		B=L()
		if not B:return-20000+p if A((W,X)[S<0],-S)else 0
	B.sort(key=O,reverse=True)
	for E in B:
		G=M(E);D=-F(d-1 if d else 0,-b,-a,p+1);U(E,G)
		if D>=b:return b
		if D>a:a=D
	return a
def f(g):
	global B,S,W,X,T;B=[0]*128;T=0;E=g.split();A=112
	for D in E[0]:
		if D.isdigit():A+=int(D)
		elif D=='/':A-=24
		else:
			C='PNBRQK'.find(D.upper())+1
			if D.islower():C=-C
			B[A]=C;T+=P(C,A)
			if C==6:W=A
			if C==-6:X=A
			A+=1
	S=1 if len(E)<2 or E[1]=='w'else-1
def e(u):
	C=ord(u[0])-97+(int(u[1])-1)*16;A=ord(u[2])-97+(int(u[3])-1)*16;F='nbrq'.find(u[4])+2 if len(u)>4 else 0;M(C|A<<7|F<<14)
def s():f('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
def v(m):
	C=m&127;D=m>>7&127;A=lambda x:chr(97+(x&7))+str((x>>4)+1);B=A(C)+A(D)
	if m>>14:B+='  nbrq'[m>>14]
	return B
def r(e=64,z=[]):
	global C;C=0;A=L();w=(W,X)[S<0]
	for d in(2,-2):
		k=w|w+d<<7
		if v(k)in z:A.append(k)
	if not A:return
	A.sort(key=O,reverse=True);D=A[0];E=1
	try:
		while E<=e:
			G=-30000;J=D;K=-30000
			for I in A:
				N=M(I);B=-F(E-1,-30000,-G,1);U(I,N)
				if B>K:K=B;J=I
				if B>G:G=B
			D=J;E+=1
	except:0
	return D
def q(a,b):return json.load(urlopen(Y+a,json.dumps(b).encode()))
def main():
	if Y:
		while(g:=q('/game',{}))['status'][0]!='d':
			while g['status'][0]=='y':
				f(g['fen']);m=r(64,g['legal_moves']);g=q('/move',{'game':g['game'],'move':v(m)})
		return
	J='depth';H='fen';E='moves';s()
	for B in sys.stdin:
		B=B.strip();A=B.split();D=0;F=64
		if B=='uci':print('uciok')
		elif B=='isready':print('readyok')
		elif B=='quit':break
		elif B.startswith('position'):
			if H in A:M=A.index(H);N=A.index(E)if E in A else len(A);f(' '.join(A[M+1:N]))
			else:s()
			if E in A:
				for O in A[A.index(E)+1:]:e(O)
		elif B.startswith('go'):
			C=dict(zip(A[1::2],map(int,A[2::2])));D=1;F=C.get(J,3)
		elif'/'in B:f(B);D=1
		if D:G=r(F);print('bestmove '+(v(G)if G else'0000'))
if __name__=='__main__':main()