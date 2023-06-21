
from tkinter import * #tkinter 사용을 위해 임포트
import numpy as np #numpy 사용을 위해 임포트
import matplotlib.pyplot as plt #그래프 사용을 위해 임포트

#Data1 버튼이 눌릴시 리스트를 생성
def data1():
    file1=open("data1.txt",'r')  # data1.txt 파일 읽기
    global gan_loss1,val_mse1,psnr1,mse1,epoch1
    gan_loss1=[] #gan_loss1이라는 빈리스트 생성
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
        file1.close() # file1를 닫는다

#Data2 버튼이 눌릴시 리스트를 생성
def data2():
    file2=open("data2.txt",'r') # data2.txt 파일 읽기
    global gan_loss2,val_mse2,psnr2,mse2,epoch2
    gan_loss2=[] #빈리스트 생성
    val_mse2=[]
    psnr2=[]
    mse2=[]
    epoch2=[]
    # data2.txt에서 데이터 추출
    for i2 in file2.readlines(): #파일의 모든 라인을 읽어서 각각 줄을 요소로 갖는 리스트로 리턴
        a2 = i2.split() # 한줄에 있는것들이 빈칸마다 split됨
        epoch2.append(int(a2[0].lstrip('epoch')))  # epoch 값을 추출하여 epoch2 리스트에 추가
        gan_loss2.append(float(a2[4].rstrip(';'))) #[4]번째 GAN Loss 값에서 ; 문자는 떼어서 gan_loss2 리스트에 저장하겠다
        val_mse2.append(float(a2[8].rstrip(';')))  #[8]번째 Val MSE 값에서 ; 문자는 떼어서 val_mse2 리스트에 저장하겠다
        psnr2.append(float(a2[11].rstrip(';'))) # [11]번째 PSNR 값에서 ; 문자는 떼어서 psnr2 리스트에 저장하겠다
        mse2.append(float(a2[14].rstrip(';'))) # [14]번째 MSE 값에서 ; 문자는 떼어서 mse2 리스트에 저장하겠다
    file2.close() #열려있는 파일 닫기
    
#그래프를 그리는 함수 몇 번째 그래프인지/y축/사용할 데이터1,2
def plotting(num,name,Data1,Data2): 
    
    plt.figure(num*2-1) # 첫 번째 그래프생성
        
    plt.plot(epoch1, Data1, label='data1') # epoch1과 Data1을 사용하여 data1이라는 그래프를 그리겠다.
    plt.plot(epoch2, Data2, label='data2') # epoch2와 Data2를 사용하여 data2라는 그래프를 그리겠다.
    plt.xlabel('epochs') # x축의 이름을 설정
    plt.ylabel(name) # y축의 이름을 설정
    plt.title("Comparison of Training") # 그래프 이름 설정
    plt.legend() # 범례 설정
    plt.grid(True) # 그래프 격자 허용
    
    plt.figure(num*2) # 두 번째 그래프생성
    plt.subplot(2,1,1) #figure을 2행 1열로 나눠서 첫번째에 해당하는것을 그린다
    plt.plot(epoch1, Data1) 
    plt.xlabel('epochs')
    plt.ylabel(name)
    plt.title("data1")
    plt.grid(True)
    
    plt.subplot(2,1,2) #figure을 2행 1열로 나눠서 두번째에 해당하는것을 그린다
    plt.plot(epoch2, Data2)
    plt.xlabel('epochs')
    plt.ylabel(name)
    plt.title("data2")
    plt.grid(True)

def plotting_data1():
    plotting(1, "gan_loss", gan_loss1, gan_loss2)

def plotting_data2():
    plotting(2, "PSNR", psnr1, psnr2)

def plotting_data3():
    plotting(3, "val_mse", val_mse1, val_mse2)

def plotting_data4():
    plotting(4, "MSE", mse1, mse2)
        
#파일 읽어 들이기 (개인정보불러오기)
def Data_Read():   
            f2=open('myInfo.txt','r')
            data=f2.readlines()
            f2.close()
            
            Name=data[0]
            Number=data[1]
            Grade=data[2]
            Major=data[3]
            
            t1.insert(1.0,'성명 : '+ Name)
            t1.insert(2.0,'학번 : '+Number)
            t1.insert(3.0,'학년 : '+Grade)
            t1.insert(4.0,'전공 : '+Major)

#Entry박스에서 입력된 내용 저장하기 (개인정보저장)
def Data_Save(): 
      
         # 데이터 읽기
         Name = e1.get()
         Number = e2.get()       
         Grade = e3.get()
         Major = e4.get()
        
         # myInfo.txt 파일에 저장
         f1 = open('myInfo.txt', 'w')
         f1.write(Name+'\n'+Number+'\n'+Grade+'\n'+Major+'\n')
         f1.close()
            
         # Entry 내용 전체 지우기
         e1.delete(0, END)
         e2.delete(0, END)
         e3.delete(0, END)
         e4.delete(0, END)
     
#윈도우 설정                     
root = Tk()
blank_space =" "
root.geometry("1100x650+100+100")
root.title(20*blank_space+"Term Project")

frame1=Frame(root)
frame1.pack(side="left", fill="both", expand=True)
window1=Frame(frame1)
window1.pack(side="left", fill="both", expand=True)
window2=Frame(frame1)
window2.pack(side="right", fill="both", expand=True)

window3=Frame(root)
window3.pack(side="right", fill="both", expand=True)

L1=Label(window1, text="개인정보 입력",fg="blue")
L1.grid(row=0,columnspan=2, pady=5)
L2=Label(window1, text="성명")
L2.grid(row=1,padx=5, pady=5)
L3=Label(window1, text="학번")
L3.grid(row=2,padx=5, pady=5)
L4=Label(window1, text="학년")
L4.grid(row=3,padx=5, pady=5)
L5=Label(window1, text="전공")
L5.grid(row=4,padx=5, pady=5)

#성명 학번 학년 전공을 입력하는 Entry박스 생성
e1 = Entry(window1,relief="solid", bd=1)
e2 = Entry(window1,relief="solid", bd=1)
e3 = Entry(window1,relief="solid", bd=1)
e4 = Entry(window1,relief="solid", bd=1)

e1.grid(row=1, column=1,padx=5, pady=5)
e2.grid(row=2, column=1,padx=5, pady=5)
e3.grid(row=3, column=1,padx=5, pady=5)
e4.grid(row=4, column=1,padx=5, pady=5)

#프레임 버튼 생성
B1 = Button(window1, text='개인정보 저장', command=Data_Save, width=18, height=1,relief="solid", bd=1)
B1.grid(row=20, column=0, rowspan=2, columnspan=2, pady=10)

B2=Button(window1, text='개인정보\n불러오기', command=Data_Read, width=18, height=2,relief="solid", bd=1)
B2.grid(row=22, column=0,  rowspan=2, columnspan=2, pady=10)

B3=Button(window1, text='Data1', command=data1, width=18, height=1,relief="solid", bd=1)
B3.grid(row=24, column=0,  rowspan=2, columnspan=2, pady=10)

B4=Button(window1, text='Data2', command=data2, width=18, height=1,relief="solid", bd=1)
B4.grid(row=26, column=0,  rowspan=2, columnspan=2, pady=10)

L7=Label(window2, text="개인정보 요약",fg="blue")
L7.grid(row=0,column=2,columnspan=2,pady=5)

t1 = Text(window2,height=11, width=20,relief="solid", bd=1)
t1.grid(row=1,column=2,columnspan=2,rowspan=12,padx=10, pady=10)

B5=Button(window2, text='Gan Loss Plot', command=plotting_data1, width=18, height=1,relief="solid", bd=1)
B5.grid(row=20, column=2, rowspan=2, columnspan=2, pady=10)

B6=Button(window2, text='PSNR Plot', command=plotting_data2, width=18, height=1,relief="solid", bd=1)
B6.grid(row=22, column=2, rowspan=2, columnspan=2, pady=10)

B7=Button(window2, text='Val MSE Plot', command=plotting_data3, width=18, height=1,relief="solid", bd=1)
B7.grid(row=24, column=2, rowspan=2, columnspan=2, pady=10)

B7=Button(window2, text='MSE Plot', command=plotting_data4, width=18, height=1,relief="solid", bd=1)
B7.grid(row=26, column=2, rowspan=2, columnspan=2, pady=10)


def data_processing_and_save():
    title_save = ["Gan Loss", "Val_mse", "PSNR", "Mse"]
    save1 = [gan_loss1,val_mse1,psnr1,mse1]
    save2 = [gan_loss2,val_mse2,psnr2,mse2]
    
    with open('DataProcessing.txt', 'w') as file_save:   
        t2.insert(1.0, "[data1.txt 파일의 최대값, 최소값, 평균값]\n")
        file_save.write("[data1.txt 파일의 최대값, 최소값, 평균값]\n")
        for i in range(len(title_save)):
            #파일에다가 작성
            file_save.write(title_save[i] + ': \n')
            file_save.write('최대값 : ' + str(max(save1[i])) + '\n')
            file_save.write('최소값 : ' + str(min(save1[i])) + '\n')
            file_save.write('평균 : ' + str(np.mean(save1[i])) + '\n\n')
            #위젯에다가 작성
            t2.insert('end', title_save[i] + ': \n')
            t2.insert('end', '최대값 : ' + str(max(save1[i])) + '\n')
            t2.insert('end', '최소값 : ' + str(min(save1[i])) + '\n')
            t2.insert('end', '평균 : ' + str(np.mean(save1[i])) + '\n\n')
        #파일에다가 작성
        file_save.write("=========================================\n")
        file_save.write("[data2.txt 파일의 최대값, 최소값, 평균값]\n")
        #위젯에다가 작성
        t2.insert(22.0,"=========================================\n")
        t2.insert(23.0, "[data2.txt 파일의 최대값, 최소값, 평균값]\n")
        for i in range(len(title_save)):
            #파일에다가 작성
            file_save.write(title_save[i] + ': \n')
            file_save.write('최대값 : ' + str(max(save2[i])) + '\n')
            file_save.write('최소값 : ' + str(min(save2[i])) + '\n')
            file_save.write('평균 : ' + str(np.mean(save2[i])) + '\n\n')
            #위젯에다가 작성
            t2.insert('end', title_save[i] + ': \n')
            t2.insert('end', '최대값 : ' + str(max(save2[i])) + '\n')
            t2.insert('end', '최소값 : ' + str(min(save2[i])) + '\n')
            t2.insert('end', '평균 : ' + str(np.mean(save2[i])) + '\n\n')

L8=Label(window3, text="데이터",fg="blue")
L8.grid(row=0,column=0,columnspan=30,pady=5)
t2 = Text(window3,height=22, width=43,relief="solid", bd=1)
t2.grid(row=1,column=0,columnspan=30,padx=5 ,pady=5)

B8=Button(window3, text='Data Processing & Save', command=data_processing_and_save,width=38, height=1,relief="solid", bd=1)
B8.grid(row=30, column=2, rowspan=2, columnspan=2, pady=25)

#한림로고 배치
img = PhotoImage(file='hallym_logo.gif',master=window3)
Hallym_Logo = Label(window3, image=img)
Hallym_Logo.place(x=390,y=500)

root.mainloop()
