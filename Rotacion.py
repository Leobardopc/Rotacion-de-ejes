import numpy as np

def rot_x(x, y, z, theta):
    '''
    Rota un vector (x, y, z) alrededor del eje X.

    Parametros:
        x, y, z (float): coordenadas del vector
        theta (float): ángulo de rotacion en radianes

    Retorna:
        np.array: vector rotado
    '''
    R = np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta),  np.cos(theta)]
    ])
    v = np.array([x, y, z])
    return R @ v

def rot_y(x, y, z, theta):
    '''
    Rota un vector (x, y, z) alrededor del eje Y.

    Parametros:
        x, y, z (float): coordenadas del vector
        theta (float): ángulo de rotacion en radianes

    Retorna:
        np.array: vector rotado
    '''
    R = np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    v = np.array([x, y, z])
    return R @ v

def rot_z(x, y, z, theta):
    '''
    Rota un vector (x, y, z) alrededor del eje Z.

    Parameters:
        x, y, z (float): coordenadas del vector
        theta (float): ángulo de rotacion en radianes

    Retorna:
        np.array: vector rotado
    '''
    R = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0, 0, 1]
    ])
    v = np.array([x, y, z])
    return R @ v

def rotar(x, y, z, theta, axis):
    '''
    Rota un vector (x, y, z) en torno al eje indicado.

    Parameters:
        x, y, z (float): coordenadas del vector
        theta (float): ángulo de rotacion en radianes
        axis (string): eje de rotación ('x', 'y' o 'z').

    Retorna:
        np.array: vector rotado
    '''
    if axis == 'x':
        return rot_x(x, y, z, theta)
    elif axis == 'y':
        return rot_y(x, y, z, theta)
    elif axis == 'z':
        return rot_z(x, y, z, theta)
    else:
        raise ValueError("El eje debe ser 'x', 'y' o 'z'.")

v = (0, 0, 1.5)   # Dar los datos para vector inicial
theta = np.pi/2 # 90 grados

print("Rotación en X:", rotar(*v, theta, 'x'))
print("Rotación en Y:", rotar(*v, theta, 'y'))
print("Rotación en Z:", rotar(*v, theta, 'z'))