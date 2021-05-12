#imports------------------------------------------------
import pandas as pd
import numpy as np

import time

import imblearn #para o desbalanceamento
from imblearn.over_sampling import SMOTE

from sklearn.model_selection import train_test_split #para separação em treino e teste

from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics

import warnings
warnings.filterwarnings('ignore')
#-------------------------------------------------------


start = time.time()
#Carregando csv
print('Carregando csv...')
df = pd.read_csv('dados/training_sample.csv')

#Oversampling --------------------------------------------
# Seed para reproduzir o mesmo resultado
seed = 100

# Separa X e y
X = df.iloc[:, 1:-1]  
y = df.iloc[:, -1] 

# Cria o balanceador SMOTE
smote_bal = SMOTE(random_state = seed)

# Aplica o balanceador
X_over, y_over = smote_bal.fit_resample(X, y)
#Oversampling --------------------------------------------

#Undersampling --------------------------------------------
df_class_0 = df[df.ordered == 0]
df_class_1 = df[df.ordered == 1]
count_class_0, count_class_1 = df['ordered'].value_counts()
min_count = min(count_class_0, count_class_1)

df_test_under = pd.concat([df_class_0.sample(min_count), df_class_1.sample(min_count)],
                              axis=0)

X_under = df_test_under.iloc[:, 1:-1].fillna(0)
y_under = df_test_under.iloc[:, -1].fillna(0)
#Undersampling --------------------------------------------

# Divisão em Dados de Treino e Teste - usando dados do oversampling.
cols_remove = ['basket_add_detail', 'sign_in', 'device_mobile', 'device_tablet']
cols = list(set(list(X_over.columns)) - set(list(cols_remove)))

#70% treino - 30% teste
X_train, X_test, y_train, y_test = train_test_split(X_over[cols], y_over, test_size = 0.3, random_state = 42)

#Rodando só melhor versão obtida no jupyter notebook
# {'max_depth': 5,
						#  'max_features': 'auto',
						#  'min_samples_leaf': 5,
						#  'min_samples_split': 2,
						#  'n_estimators': 150}

model = GradientBoostingClassifier(max_depth=5,
									max_features='auto', 
									min_samples_leaf=5,
									min_samples_split= 2,
									n_estimators=150, 
									random_state=0)
						
print('Fitting...')
model.fit(X_train, y_train)

print('Predict...')
pred = model.predict(X_test)

print('Métrica:')
print('\nMatriz de confusão:\n',metrics.confusion_matrix(y_test,pred))
print('\nMétricas de Classificação\n', metrics.classification_report(y_test, pred))

print('\n\nTempo de execução:', time.time() - start)