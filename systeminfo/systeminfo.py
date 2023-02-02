import platform
# import psutil
import socket
import timeit


def cpu_strength_score():
    """Computes a CPU strength score using timeit"""
    # A simple numerical task to compute the CPU strength score
    score = timeit.timeit(stmt="[i**2 for i in range(1000)]", number=10000)
    return score


def main():
    """Main function to display system information"""
    print("Machine name: ", platform.node())
    print("Operating system name: ", platform.system())
    print("Operating system version: ", platform.release())
    # print("Number of CPUs: ", psutil.cpu_count())
    # print("Amount of memory: ", psutil.virtual_memory().total / (1024 ** 3), "GB")
    print("IP address: ", socket.gethostbyname(socket.gethostname()))
    print("CPU strength score: ", cpu_strength_score())


if __name__ == '__main__':
    main()
