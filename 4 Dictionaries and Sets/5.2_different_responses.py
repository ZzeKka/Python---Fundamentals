def different_responses(filename):
    return {
        line.split()[8] for line in open(filename)
    }