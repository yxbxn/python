# 단층 퍼셉트론과 신경망 - 22.02.22
- 단층 퍼셉트론에 해당하는 AND,NAND,OR 게이트를 구현
- 단층 퍼셉트론으로 구현할 수 없는 XOR 게이트
- 다층 퍼셉트론으로 구현하는 XOR 게이트

# 다층 퍼셉트론과 신경망 - 22.02.23
- 다양한 활성화 함수(시그모이드, ReLU, 계단, 소프트맥스, 항등함수)
- 3층 퍼셉트론 이해하기
- 소프트맥스 함수에서 오버플로우 문제해결하기

# 손글씨 데이터로 구현하는 신경망의 순전파(forward propagation) - 22.02.24
- MNIST 데이터로 구현하는 신경망 순전파(추론 과정)
- Batch 처리의 장점
- 정규화 및 성능평가(Accuracy)

# 손실함수의 종류와 활성화 함수의 의미 - 22.02.25
- 손실함수는 신경망이 가중치를 찾기 위한 기준 지표
- 손실함수는 오차제곱합, 교차엔트로피오차
- 활성화 함수의 존재 의미는 입력값을 비선형으로 도출하기 위함
- 비선형 활성화 함수과 은닉층을 쌓아 비선형적 모델의 복잡도를 올려 다양한 문제 해결가능

# 신경망 학습(미니배치, 편미분, 경사하강법, 기울기) - 22.02.26
- 활성화 함수를 사용하는 이유? 입력값에 대한 출력값을 비선형으로 나타내 비선형 문제를 해결하고, 복잡도를 높이기 위해
- 매개변수의 편미분된 기울기를 바탕으로 손실함수가 줄어드는 방향으로 매개변수를 갱신
- 편미분으로 기울기 산출, 해석학적 미분 대신 수치 미분 방식과 중심차분을 이용

# 2층 신경망의 학습 알고리즘 구현 - 22.02.27
- 미니배치로 수만개의 학습데이터 중 일부를 무작위로 뽑고 학습
- 미니배치 -> 기울기 산출 -> 매개변수 갱신의 과정을 반복함
- SGD(Stochastic Gradient Descent) 확률적 경사하강법으로 매개변수를 갱신
- epoch의 개념, 오차역전파의 장점

# 계산 그래프로 이해하는 오차 역전파 - 22.02.28
- 오차역전파는 매개변수의 기울기를 수치 미분보다 빠르게 계산하는 방법
- 계산 그래프의 국소적 계산을 기반으로 국소적 미분을 오른쪽에서 왼쪽으로 전달
- 연쇄법칙(합성함수의 미분은 구성함수들의 미분 곱)의 원리를 이용해 역전파 구현
- 곱셈노드의 역전파는 입력신호는 뒤바꿔 내보내고, 덧셈노드는 그대로 흘려보냄

# 역전파를 포함한 신경망의 다양한 계층 구현 - 22.03.01
- ReLU 활성화 함수 계층 순전파와 역전파 포함하여 구현(True/False 활용)
- 새로운 나눗셈노드, exp노드로 Sigmoid 계층 구현
- 순전파의 출력값을 이용해 간소화하는 Sigmoid 계층 구현
- 행렬곱 Affine 계층 구현, 스칼라값 1차원,2차원배열(Batch) 순으로 확장해 구현

# 역전파를 포함한 신경망 학습 전과정 구현 - 22.03.03
- Softmax-with-Loss 계층의 구현과 역전파, softmax는 정규화하는 역할
- Softmax-with-Loss 계층의 역전파는 y-t로 항등함수-오차제곱합(SSE) 조합과 동일함
- 신경망 학습 전과정은 계층(Affine,ReLU,Softmax 등)을 정의하면 간단함. 계층을 순차적으로 추가
- 2층 신경망의 경우 Affine1-ReLU-Affine2-Softmax-with-Loss 계층의 적용으로 구현가능함

# 1,2,3차원 배열의 경사하강법 - 22.03.03
- 경사하강법을 이용해 매개변수에 대한 함수의 변화량을 구해 손실함수의 최솟값을 찾아감
- 1,2,3차원 배열을 모두 포용할 수 있는 경사하강법 코드 구현
- 모든 배열을 탐색해 하나의 원소를 목표변수로 나머지 변수를 고정시키고 편미분하는 방식

# 다양한 매개변수 갱신방법 - 22.03.04
- 비등방성 함수에서 비효율적인 지그재그 움직임이 나타나는 SGD
- 물체의 속도를 이용해 하강시키면서 SGD의 단점을 해결하는 Momentum
- 적정한 학습률을 위해 매개변수 별로 적응적으로 학습률을 조정하는 AdaGrad
P. 매개변수 갱신 History를 시각화하여 Momentum의 효율성 확인, AdaGrad는 확인하지 못함
P. 매개변수 갱신과정을 시각화하고자 하였으나 SGD의 지그재그 움직임이 나타나지 않음

# 다양한 매개변수 갱신방법 - 22.03.05
- 매개변수 갱신 History를 시각화하여 Momentum과 AdaGrad의 갱신과정 확인함
- SGD의 지그재그 움직임 확인함. plot 시각화 시, plot("o-") 이용해 시각화 과정 추적

# 다양한 매개변수 갱신방법 - 22.03.06
- MNIST 데이터를 활용해 다양한 매개변수 갱신방법 적용 후, 비교 및 시각화

# 가중치의 초깃값 - 22.04.14
- 가중치 초깃값 설정에 따라 은닉층 활성화값의 분포가 고르게 분포
- 가중치 초깃값의 오류로 활성화 값이 편향되면 표현력이 제한
