import socket
import time

# from djitellopy import tello


drone1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
drone1.setsockopt(socket.SOL_SOCKET, 2, 'wlp3s0'.encode())

# drone1 = tello.Tello()
# drone1.connect()
# print(drone1.get_battery())


drone2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
drone2.setsockopt(socket.SOL_SOCKET, 2, 'enp2s0'.encode())

drone1.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
drone2.sendto('command'.encode(), 0, ('192.168.10.1', 8889))

drone1.sendto('takeoff'.encode(), 0, ('192.168.10.1', 8889))
drone2.sendto('takeoff'.encode(), 0, ('192.168.10.1', 8889))

time.sleep(2)

drone1.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
drone2.sendto('command'.encode(), 0, ('192.168.10.1', 8889))

drone1.sendto('land'.encode(), 0, ('192.168.10.1', 8889))
drone2.sendto('land'.encode(), 0, ('192.168.10.1', 8889))
