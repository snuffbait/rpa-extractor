#made by verya 4:31 pm 09/09/2026

import os,sys,zlib,pickle,shutil

verya1=('.png','.webp','.jpg','.jpeg','.ogg','.mp3','.opus','.m4a')

def verya2():
    verya3=sys.argv[1:]
    for verya4 in verya3:
        verya5=os.path.join(os.path.dirname(os.path.abspath(verya4)) or '.','extracted')
        os.makedirs(verya5,exist_ok=True)
        verya6=[]
        if os.path.isdir(verya4):
            for verya7,verya8,verya9 in os.walk(verya4):
                for verya10 in verya9:
                    verya6.append(os.path.join(verya7,verya10))
        else:
            verya6.append(verya4)
        for verya11 in verya6:
            verya12=verya11.lower()
            if verya12.endswith('.rpa'):
                try:
                    verya13=open(verya11,'rb')
                    verya14=verya13.readline().decode('utf-8','ignore').strip().split()
                    verya15=verya14[0] if verya14 else ''
                    verya16=0
                    verya17=0
                    if verya15=='RPA-3.0' or verya15=='RPA-3.2':
                        verya17=int(verya14[1],16)
                        verya16=int(verya14[2],16)
                    elif verya15=='RPA-2.0':
                        verya17=int(verya14[1],16)
                    verya13.seek(verya17)
                    verya18=pickle.loads(zlib.decompress(verya13.read()))
                    for verya19 in verya18:
                        if not verya19.lower().endswith(verya1):continue
                        verya20=verya18[verya19][0]
                        if len(verya20)==3:
                            verya21,verya22,verya23=verya20
                        else:
                            verya21,verya22=verya20
                            verya23=b''
                        if type(verya23)==str:verya23=verya23.encode('latin-1')
                        if verya16!=0:
                            verya21=verya21^verya16
                            verya22=verya22^verya16
                        verya13.seek(verya21)
                        verya24=verya23+verya13.read(verya22-len(verya23))
                        try:
                            open(verya5+os.sep+os.path.basename(verya19),'wb').write(verya24)
                        except:
                            pass
                    verya13.close()
                except:
                    pass
            elif verya12.endswith(verya1):
                try:
                    shutil.copy(verya11,os.path.join(verya5,os.path.basename(verya11)))
                except:
                    pass
    os.system('pause') if os.name=='nt' else input()

verya2()