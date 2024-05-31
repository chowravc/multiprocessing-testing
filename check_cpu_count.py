import multiprocessing as mp

if __name__ == '__main__':
    
    cpu_count = mp.CPU_count()
    print(f"Number of CPU cores: {cpu_count}")