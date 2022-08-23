import gzip
import argparse

def process(filepath):
    print("QueryId,EntityId")
    res = {}
    with gzip.GzipFile(filepath, mode="r") as stream:
        for line in stream:
            line = line.split()
            if res.get(int(line[0]), None) is None:
                res[int(line[0])] = []
            res[int(line[0])].append((int(line[2]), int(line[3])))
    for key in sorted(res.keys()):
        for docid, _ in sorted(res[key], key=lambda x: x[1])[:100]:
            key = str(key)
            docid = str(docid)
            key = "0"*(3 - len(key)) + key
            docid = "0"*(7 - len(docid)) + docid
            print(f"{key},{docid}")



if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Process results file")
    parser.add_argument('file')
    args = parser.parse_args()
    process(args.file)