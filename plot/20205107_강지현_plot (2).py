import numpy as np #numpy 사용을 위해 임포트
import matplotlib.pyplot as plt #그래프 사용을 위해 임포트

file1 = open("data1.txt", 'r') # data1.txt 파일 읽기
gan_loss1 = [] #gan_loss1이라는 빈리스트 생성
val_mse1 = [] #val_mse1이라는 빈리스트 생성
psnr1 = [] #psnr1이라는 빈리스트 생성
mse1 = [] #mse1이라는 빈리스트 생성
epoch1 = [] #epoch1이라는 빈리스트 생성

# data1.txt에서 데이터 추출
for i1 in file1.readlines(): #파일의 모든 라인을 읽어서 각각 줄을 요소로 갖는 리스트로 리턴
    a1 = i1.split() # 한줄에 있는것들이 빈칸마다 split됨
    epoch1.append(int(a1[0].lstrip('epoch')))  # epoch 값을 추출하여 epoch1 리스트에 추가
    gan_loss1.append(float(a1[4].rstrip(';')))  #[4]번째 GAN Loss 값에서 ; 문자는 떼어서 gan_loss1 리스트에 저장하겠다 만약 ; 없으면 그냥 나옴
    val_mse1.append(float(a1[8].rstrip(';')))  #[8]번째 Val MSE 값에서 ; 문자는 떼어서 val_mse1 리스트에 저장하겠다
    psnr1.append(float(a1[11].rstrip(';')))  # [11]번째 PSNR 값에서 ; 문자는 떼어서 psnr1 리스트에 저장하겠다
    mse1.append(float(a1[14].rstrip(';')))  # [14]번째 MSE 값에서 ; 문자는 떼어서 mse1 리스트에 저장하겠다

file1.close() #열려있는 파일 닫기

file2 = open("data2.txt", 'r') # data2.txt 파일 읽기
gan_loss2 = [] #빈리스트 생성
val_mse2 = []
psnr2 = []
mse2 = []
epoch2 = []

# data2.txt에서 데이터 추출
for i2 in file2.readlines(): #파일의 모든 라인을 읽어서 각각 줄을 요소로 갖는 리스트로 리턴
    a2 = i2.split() # 한줄에 있는것들이 빈칸마다 split됨
    epoch2.append(int(a2[0].lstrip('epoch')))  # epoch 값을 추출하여 epoch2 리스트에 추가
    gan_loss2.append(float(a2[4].rstrip(';'))) #[4]번째 GAN Loss 값에서 ; 문자는 떼어서 gan_loss2 리스트에 저장하겠다
    val_mse2.append(float(a2[8].rstrip(';')))  #[8]번째 Val MSE 값에서 ; 문자는 떼어서 val_mse2 리스트에 저장하겠다
    psnr2.append(float(a2[11].rstrip(';'))) # [11]번째 PSNR 값에서 ; 문자는 떼어서 psnr2 리스트에 저장하겠다
    mse2.append(float(a2[14].rstrip(';'))) # [14]번째 MSE 값에서 ; 문자는 떼어서 mse2 리스트에 저장하겠다

file2.close() #열려있는 파일 닫기

# Training 비교 그래프
plt.figure(1) #figure 생성
plt.plot(epoch1, gan_loss1, label='data1')  # epoch1과 gan_loss1을 사용하여 Training 그래프를 그림
plt.plot(epoch2, gan_loss2, label='data2')  # epoch2과 gan_loss2를 사용하여 Training 그래프를 그림
plt.xlabel('epochs')  # x축 레이블 설정
plt.ylabel('GAN Loss')  # y축 레이블 설정
plt.title("Comparison of Training")  # 그래프 제목 Comparison of Training으로 설정
plt.legend()  # 범례 표시
plt.grid(True)  # 그리드 격자 표시

# data1 GAN Loss 그래프
plt.figure(2) #figure 생성
plt.subplot(2, 1, 1) #figure을 2행 1열로 나눠서 첫번째에 해당하는것을 그린다
plt.plot(epoch1, gan_loss1)  # epoch1과 gan_loss1을 사용하여 data1의 GAN Loss 그래프를 그림
plt.xlabel('epochs')  # x축 레이블 설정
plt.ylabel('GAN Loss')  # y축 레이블 설정
plt.title("data1")  # 그래프 제목 설정
plt.grid(True)  # 그리드 격자 표시

# data2 GAN Loss 그래프
plt.subplot(2, 1, 2) #figure을 2행 1열로 나눠서 두번째에 해당하는것을 그린다
plt.plot(epoch2, gan_loss2)  # epoch2과 gan_loss2를 사용하여 data2의 GAN Loss 그래프를 그림
plt.xlabel('epochs')  # x축 레이블 설정
plt.ylabel('GAN Loss')  # y축 레이블 설정
plt.title("data2")  # 그래프 제목 설정
plt.grid(True)  # 그리드 격자 표시

# data1 Validation MSE 그래프
plt.figure(3) #figure 생성
plt.subplot(3, 1, 1) #figure을 3행 1열로 나눠서 첫번째에 해당하는것을 그린다
plt.plot(epoch1, val_mse1)  # epoch1과 val_mse1을 사용하여 data1의 Validation MSE 그래프를 그림
plt.xlabel('epochs')  # x축 레이블 설정
plt.ylabel('Val MSE')  # y축 레이블 설정
plt.title("data1")  # 그래프 제목 설정
plt.grid(True)  # 그리드 표시

# data2 Val MSE 그래프
plt.subplot(3, 1, 2) #figure을 3행 1열로 나눠서 두번째에 해당하는것을 그린다
plt.plot(epoch2, val_mse2)  # epoch2과 val_mse2를 사용하여 data2의 Val MSE 그래프를 그림
plt.xlabel('epochs')  # x축 레이블 설정
plt.ylabel('Val MSE')  # y축 레이블 설정
plt.title("data2")  # 그래프 제목 설정
plt.grid(True)  # 그리드 격자 표시

# Val MSE 비교 그래프
plt.subplot(3, 1, 3) #figure을 3행 1열로 나눠서 세번째에 해당하는것을 그린다
plt.plot(epoch1, val_mse1, label='data1')  # epoch1과 val_mse1을 사용하여 data1의 Val MSE 그래프를 그림
plt.plot(epoch2, val_mse2, label='data2')  # epoch2과 val_mse2를 사용하여 data2의 Val MSE 그래프를 그림
plt.xlabel('epochs')  # x축 레이블 설정
plt.ylabel('Val MSE')  # y축 레이블 설정
plt.title("Val MSE 비교")  # 그래프 제목 설정
plt.legend()  # 범례 표시
plt.grid(True)  # 그리드 격자 표시

# data1 PSNR 그래프
plt.figure(4) #figure 생성
plt.subplot(2, 1, 1) #figure을 2행 1열로 나눠서 첫번째에 해당하는것을 그린다
plt.plot(epoch1, psnr1)  # epoch1과 psnr1을 사용하여 data1의 PSNR 그래프를 그림
plt.xlabel('epochs')  # x축 레이블 설정
plt.ylabel('PSNR')  # y축 레이블 설정
plt.title("data1")  # 그래프 제목 설정
plt.grid(True)  # 그리드 격자 표시

# data2 PSNR 그래프
plt.subplot(2, 1, 2) #figure을 2행 1열로 나눠서 두번째에 해당하는것을 그린다
plt.plot(epoch2, psnr2)  # epoch2과 psnr2를 사용하여 data2의 PSNR 그래프를 그림
plt.xlabel('epochs')  # x축 레이블 설정
plt.ylabel('PSNR')  # y축 레이블 설정
plt.title("data2")  # 그래프 제목 설정
plt.grid(True)  # 그리드 격자 표시

# data1 MSE 그래프
plt.figure(5) #figure 생성
plt.subplot(2, 1, 1) #figure을 2행 1열로 나눠서 첫번째에 해당하는것을 그린다
plt.plot(epoch1, mse1)  # epoch1과 mse1을 사용하여 data1의 MSE 그래프를 그림
plt.xlabel('epochs')  # x축 레이블 설정
plt.ylabel('MSE')  # y축 레이블 설정
plt.title("data1")  # 그래프 제목 설정
plt.grid(True)  # 그리드 격자 표시

# data2 MSE 그래프
plt.subplot(2, 1, 2) #figure을 2행 1열로 나눠서 두번째에 해당하는것을 그린다
plt.plot(epoch2, mse2)  # epoch2과 mse2를 사용하여 data2의 MSE 그래프를 그림
plt.xlabel('epochs')  # x축 레이블 설정
plt.ylabel('MSE')  # y축 레이블 설정
plt.title("data2")  # 그래프 제목 설정
plt.grid(True)  # 그리드 표시

# 그래프 출력
plt.show()
 