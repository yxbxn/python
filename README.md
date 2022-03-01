# PIDA.ipynb
- SQL 서버에서 받아온 데이터를 가공하여 csv 형태로 출력시켜주기 위한 코드
- 피부 타입 설문테스트의 결과 1,2,3,2.5... 단순 선택지 정보만 나열됨
- 나열된 선택지 정보를 실제 선택지와 매핑시키기 위한 코드
- 설문에 응답한 사람의 최종 피부 타입별 점수 또한 출력시키기 위한 코드

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
