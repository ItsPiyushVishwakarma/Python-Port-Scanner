import socket
import time

print("=" * 40 )
print("     PYTHON PORT SCANNER")
print("         By Piyush")
print("=" * 40)

start_time = time.time()

target = input("Enter Target IP: ")

start_port = int(input("Enter Start Port: "))
end_port = int(input("Enter End Port: "))

print("Starting Port Scan...")

open_ports = 0

for port in range(start_port,end_port + 1):

    scanner = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    scanner.settimeout(0.1)

    result = scanner.connect_ex((target,port))   

    if result == 0:
        open_ports += 1
        print(f"Port {port} is OPEN")

    scanner.close()

end_time = time.time()

print("\n Scan Comlete!")
print(f"Open Ports Found: {open_ports}")
print(f"TIme Taken: {round(end_time - start_time, 2)} seconds")