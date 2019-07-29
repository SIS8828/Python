'''
conda envlist # 가상환경list 확인명령.
conda create –n tf_cpupython=3.6
# 가상환경(tf_cpu) 생성하기.
conda activate tf_cpu# 가상환경에접속하기.
pip install tensorflow# 텐서플로우설치하기.
deactivate #가상환경접속종료하기.
conda remove –n tf_cpu–all # 가상환경삭제/제거하기.
'''

import tensorflow as tf

print(tf.__version__)

hello = tf.constant('hello,tensorflow')

sess = tf.Session()

print(sess.run(hello))

