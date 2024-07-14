
import random

nucleotides = "GCAT"
phred_quality = """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

def fastq_generator(amount: int, length: int):
    head =  0
    mid = length//3 
    tail = length - length//4
    
    while amount > 0:
        amount -= 1
        line1 = f"@Sequence {amount+1}"
        line2 = "".join(random.choice(nucleotides) for position in range(length))
        line3 = "+"
        line4 = "".join(random.choice(phred_quality[:10+len(phred_quality)//4]) for position in range(mid)) + "".join(random.choice(phred_quality[len(phred_quality)//4:length - len(phred_quality)//4]) for position in range(mid, tail)) + "".join(random.choice(phred_quality[length - len(phred_quality)//4:]) for position in range(tail, length))

        print(line1)
        print(line2)
        print(line3)
        print(line4)

fastq_generator(10, 100)
