import sys
import argparse

class Primer:
    def __init__(self, name, seq):
        self.name = name
        self.seq = seq

    def __repr__(self):
        return "(%s, %s)" % (self.name, self.seq)

def read_fasta(filename):
    name = None
    seq = ""
    primers = []
    with open(filename) as file:
        for line in file:
            if line.startswith("#"):
                continue
            if line.startswith(">"):
                if name:
                   primers.append(Primer(name,seq))
                name = line[1:-1].split("|")[0]
                seq = ""
            else:
                seq += line[:-1]
        primers.append(Primer(name,seq))
        return primers

def make_pair(p1, p2):
    out = p1.name + "_&_" + p2.name + "\t" + p1.seq + "\t" + p2.seq + "\n"
    return out

def print_pairs(primers, outfile, selfprimer):
    with open(outfile, "w") as fo:
        for primerA in primers:
            for primerB in primers:
                if not selfprimer:
                    if primerA == primerB:
                        continue
                out = make_pair(primerA, primerB)
                fo.write(out)
                
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--primer", help="name of file containing primers", required=True)
    parser.add_argument("-o", "--outfile", help="name of output file", required=True)
    parser.add_argument("-s", "--selfprimer", help="specify this if a primer should also be paired with itself", action="store_true", default=False)
    args = parser.parse_args()

    primers = read_fasta(args.primer)
    print_pairs(primers, args.outfile, args.selfprimer)

if __name__ == "__main__":
    main()



