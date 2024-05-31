import os

if __name__ == '__main__':
    
    cpu_count = os.cpu_count()
    print(f"Number of CPU cores: {cpu_count}")
