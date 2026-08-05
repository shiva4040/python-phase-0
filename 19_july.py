import matplotlib.pyplot as plt
# # loss
# price = 1000
# pridict = 994
# loss = (price -pridict)**2
# print(loss)

# minimize loss

# actual = 1000
# pridict_price = [993,943,994,959]
# for i in pridict_price:
#     loss = (actual - i)**2
#     print(f"pridicted = {i} \n loss = {loss} ")

# Gradient

# for L(w)=w2
# gradient = dL/dw = 2w
# def grad(w):
#     return 2*w
# print(grad(3))
# print(grad(5))
# print(grad(5.4))
# print(grad(45))

#Learning Rate (Step Size)

# formula = w = w-lr*gradient
# w = 14
# lr = 0.1
# grad = 2*w
# new_weight = w - lr *grad
# print(new_weight)

#One Gradient Descent Step

# w = 12
# lr = 0.1
# grad = w*2
# loss = w**2
# print("Before")
# print("Weight:", w)
# print("Loss:", loss)
# w = w-lr*grad
# print("After")
# print("weight:",w)
# print("loss:",w**2)

# by loop

# w = 12
# lr = 0.1
# for i in range(10):
#     grad = 2*w
#     loss = w**2
#     print("step : ",i+1)
#     print("weight : ",w)
#     print("loss : ",loss)
#     w = w-lr*grad    

# Mini: Implement gradient descent to find minimum of f(x) = x^2 from scratch. Plot the path.

def grad(w):
    return 2*w
w = 4
lr = 0.1
weights =[]
losses = []
for i in range(11):
    loss = w**2
    gradeint = grad(w)
    weights.append(w)
    losses.append(loss)
    print(f"Step {i+1} : weight: {w:.2f} ,loss: {loss:.2f}")
    w = w-lr*gradeint

plt.plot(weights,losses,marker = 'o')
plt.grid(True)
plt.xlabel("weights")
plt.ylabel("losses")
plt.title("Gradient Descent on f(x)=x²")
plt.show()