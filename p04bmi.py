#2025.4.30
import numpy as np
import sklearn as sns
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

from p04bmiclass import MyDecisionTree
from p04functions import fit_decision_tree,predict_decision_tree
np.random.seed(42)

height = np.random.normal(170,10,1000)
weight = np.random.normal(65,15,1000)
bmi = weight/(height/100)**2
X=np.vstack((height,weight)).T
y = bmi
#데이터를 train 용과 test 용으로 나눔
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

# 함수를 이용한 머신러닝
'''
# 학습 훈련 train
tree_model = fit_decision_tree(X_train,y_train)
# test 데이터로 예측
y_pred = predict_decision_tree(tree_model,X_test)
# 평가: 예측된 결과와 실제 결과 비교

'''

# 2.자체제작 클래스를 이용한 머신러닝

tree = MyDecisionTree(3)
tree.fit(X_train,y_train)
y_pred = tree.predict(X_test)


# 3. 남이 만들어놓은 클래스(decisiontreeregressor)를 이용한 머신러닝
'''
from sklearn.tree import DecisionTreeRegressor
tree = DecisionTreeRegressor()
tree.fit(X_train,y_train)
y_pred = tree.predict(X_test)
mse = mean_squared_error(y_pred,y_test)
print(f'평균제곱오차(mse):{mse:.3f}')
'''
# 일부 출력
for i in range(5):
    print(f"실제 BMI: {y_test[i]:.2f} | 예측 BMI: {y_pred[i]:.2f}")