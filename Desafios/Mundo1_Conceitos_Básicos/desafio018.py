# SENO, COSSENO E TANGENTE DE ÃNGULO
'''from math import sin, cos, tan, degrees, radians
ang = float(input('Digite o ângulo do triângulo: '))
s = sin(radians(ang))
c = cos(radians(ang))
t = tan(radians(ang))

print(f'O ângulo de °{ang} tem os seguintes valores:\n Seno: {s:.2f} \n Cosseno: {c:.2f} \n Tangente: {t:.2f}')'''

from math import sin, cos, tan, radians
ang = float(input('\33[34mQual o ângulo do triângulo? '))
print(f'Com o ângulo sendo \33[1;34m{ang} \33[m \33[34mtemos: '
      f'\n \33[34mSENO: \33[1;34m{sin(radians(ang)):.2f} '
      f'\n \33[34mCOSSENO: \33[1;34m{cos(radians(ang)):.2f} '
      f'\n \33[34mTANGENTE: \33[1;34m{tan(radians(ang)):.2f}')
