import hashlib
import time
import requests

def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

def compute_checksum(filename, algorithm):
    hash_func = hashlib.new(algorithm)
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def measure_speed(filename, algorithms):
    times = {}
    for algorithm in algorithms:
        start_time = time.time()
        checksum = compute_checksum(filename, algorithm)
        times[algorithm] = (time.time() - start_time, checksum)
    return times

url = "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
filename = download_file(url)

algorithms = ['md5', 'sha1', 'sha224', 'sha256', 'sha512', 'sha3_224', 'sha3_256', 'sha3_512']

times = measure_speed(filename, algorithms)

for algorithm in sorted(times, key=times.get):
    time_taken, checksum = times[algorithm]
    print(f"{algorithm} took {time_taken:.6f} seconds - Checksum: {checksum}")

fastest = min(times, key=lambda k: times[k][0])
print(f"The fastest hash algorithm is {fastest}.")

print("Ranking the hash algorithms by speed:")
for rank, algorithm in enumerate(sorted(times, key=times.get), start=1):
    print(f"{rank}. {algorithm} ({times[algorithm][0]:.6f} seconds)")
