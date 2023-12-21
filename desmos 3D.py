import cmath
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox 
from mpl_toolkits.mplot3d import Axes3D
import ast

# Hàm số mặc định
def func(x, y):
    return np.sin(x)+np.sin(y)

# Tạo hình 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Tạo dữ liệu mặc định
x = y = np.linspace(-10, 10, 200)  # Mở rộng phạm vi của trục x và y
X, Y = np.meshgrid(x, y)
Z = func(X, Y)

# Vẽ đồ thị 3D ban đầu
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='k')

# Hàm được gọi khi người dùng thay đổi hàm số
def update_function(text):
    global surf
    try:
        # Sử dụng lambda để định nghĩa hàm số
        user_func = lambda x, y: eval(text)
        Z = user_func(X, Y)
        
        surf.remove()
        surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='k')
        ax.set_box_aspect([np.ptp(arr) for arr in [X, Y, Z]])  # Giữ tỷ lệ tự nhiên giữa các trục
        plt.draw()
    except Exception as e:
        print(e)

# Hộp văn bản để nhập hàm số
axbox = plt.axes([0.1, 0.01, 0.65, 0.05])
text_box = TextBox(axbox, 'Hàm số: z =',initial="np.sin(x)+np.sin(y)")
text_box.on_submit(update_function)

plt.show()