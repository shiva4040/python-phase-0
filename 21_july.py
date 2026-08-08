import numpy as np
import random
import matplotlib.pyplot as plt
# total_stu = 100;
# boy = 60;
# boy_play_cricket = 30
# prob_of_a_student_to_play_cricket = boy_play_cricket/boy
# print(prob_of_a_student_to_play_cricket)

# desease  =  0.01
# healty = 1 - 0.01 
# pos_if_desease = 0.99
# pos_if_healty = 0.05
# # total probability of positive test
# total_pos =  pos_if_desease*desease +  pos_if_healty*healty
# # bayes theorem
# final= pos_if_desease*desease/total_pos
# print(final)

# normal form or gaussian distribution
 
# data = np.random.normal(loc = 170, scale = 10, size= 1000)
# print(data)
# print("mean : ",np.mean(data))
# print("std : ",np.std(data))
# plt.hist(data, bins=30)
# plt.xlabel("height")
# plt.ylabel("frequency")
# plt.title("gaussian distribution")
# plt.show()
# Mini: Implement Gaussian PDF from scratch. Plot it for different mean/std values.
def gaussian(x,mean,std):
    return (1/(std*np.sqrt(2* np.pi))) * np.exp(-0.5 *((x-mean)/std)**2)
x = np.linspace(100,420,1000)
y1 = gaussian(x,180,10)
y2 = gaussian(x,180,20)
y3 = gaussian(x,300,30)
y4 = gaussian(x,390,10)

plt.plot(x,y1 ,label="mean = 180 , std = 10")
plt.plot(x,y2, label="mean = 180 , std = 20")
plt.plot(x,y3,label="mean = 300 , std = 30")
plt.plot(x,y4,label="mean = 390 , std = 10")
plt.xlabel("x")
plt.ylabel("prob desity")
plt.title("gaussian distribution")
plt.legend()
plt.show()