def different_ips(filename):
    for line in filename:
        return {line.split()[0] for line in open(filename)}