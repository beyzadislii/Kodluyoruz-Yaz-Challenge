metin=input("Metninizi girin ")
metin=metin.lower()

counter_a=0
for a in metin:
    if a=="a":
        counter_a=counter_a+1
counter_q=0
for a in metin:
    if a=="q":
        counter_q=counter_q+1
counter_w=0
for a in metin:
    if a=="w":
        counter_w=counter_w+1

counter_e=0
for a in metin:
    if a=="e":
        counter_e=counter_e+1
counter_r=0
for a in metin:
    if a=="r":
        counter_r=counter_r+1
counter_t=0
for a in metin:
    if a=="t":
        counter_t=counter_t+1
counter_y=0
for a in metin:
    if a=="y":
        counter_y=counter_y+1
counter_u=0
for a in metin:
    if a=="u":
        counter_u=counter_u+1
counter_o=0
for a in metin:
    if a=="o":
        counter_o=counter_o+1
counter_p=0
for a in metin:
    if a=="p":
        counter_p=counter_p+1
counter_s=0
for a in metin:
    if a=="s":
        counter_s=counter_s+1
counter_d=0
for a in metin:
    if a=="d":
        counter_d=counter_d+1
counter_f=0
for a in metin:
    if a=="f":
        counter_f=counter_f+1
counter_g=0
for a in metin:
    if a=="g":
        counter_g=counter_g+1
counter_h=0
for a in metin:
    if a=="h":
        counter_h=counter_h+1
counter_j=0
for a in metin:
    if a=="j":
        counter_j=counter_j+1
counter_k=0
for a in metin:
    if a=="k":
        counter_k=counter_k+1
counter_l=0
for a in metin:
    if a=="l":
        counter_l=counter_l+1
counter_i=0
for a in metin:
    if a=="i":
        counter_i=counter_i+1
counter_z=0
for a in metin:
    if a=="z":
        counter_z=counter_z+1
counter_x=0
for a in metin:
    if a=="x":
        counter_x=counter_x+1
counter_c=0
for a in metin:
    if a=="c":
        counter_c=counter_c+1
counter_v=0
for a in metin:
    if a=="v":
        counter_v=counter_v+1
counter_b=0
for a in metin:
    if a=="b":
        counter_b=counter_b+1
counter_n=0
for a in metin:
    if a=="n":
        counter_n=counter_n+1
counter_m=0
for a in metin:
    if a=="m":
        counter_m=counter_m+1
liste=[counter_q,counter_w,counter_e,counter_r,counter_t,counter_y,counter_u,counter_o,counter_p,counter_a,counter_s,counter_d,counter_f,counter_g,counter_h,counter_j,counter_k,counter_l,counter_i,counter_z,counter_x,counter_c,counter_v,counter_b,counter_n,counter_m]
print(f"En fazla tekrar eden harf {max(liste)} kere tekrar etti.")
if max(liste)==counter_a:
    print("En fazla tekrar eden eleman a")
if max(liste)==counter_q:
    print("En fazla tekrar eden eleman q")
if max(liste)==counter_w:
    print("En fazla tekrar eden eleman w")
if max(liste)==counter_e:
    print("En fazla tekrar eden eleman e")
if max(liste)==counter_r:
    print("En fazla tekrar eden eleman r")
if max(liste)==counter_t:
    print("En fazla tekrar eden eleman t")
if max(liste)==counter_y:
    print("En fazla tekrar eden eleman y")
if max(liste)==counter_u:
    print("En fazla tekrar eden eleman u")
if max(liste)==counter_o:
    print("En fazla tekrar eden eleman o")
if max(liste)==counter_p:
    print("En fazla tekrar eden eleman p")
if max(liste)==counter_s:
    print("En fazla tekrar eden eleman s")
if max(liste)==counter_d:
    print("En fazla tekrar eden eleman d")
if max(liste)==counter_f:
    print("En fazla tekrar eden eleman f")
if max(liste)==counter_g:
    print("En fazla tekrar eden eleman g")
if max(liste)==counter_h:
    print("En fazla tekrar eden eleman h")
if max(liste)==counter_j:
    print("En fazla tekrar eden eleman j")
if max(liste)==counter_k:
    print("En fazla tekrar eden eleman k")
if max(liste)==counter_l:
    print("En fazla tekrar eden eleman l")
if max(liste)==counter_i:
    print("En fazla tekrar eden eleman i")
if max(liste)==counter_z:
    print("En fazla tekrar eden eleman z")
if max(liste)==counter_x:
    print("En fazla tekrar eden eleman x")
if max(liste)==counter_c:
    print("En fazla tekrar eden eleman c")
if max(liste)==counter_v:
    print("En fazla tekrar eden eleman v")
if max(liste)==counter_b:
    print("En fazla tekrar eden eleman b")
if max(liste)==counter_n:
    print("En fazla tekrar eden eleman n")
if max(liste)==counter_m:
    print("En fazla tekrar eden eleman m")