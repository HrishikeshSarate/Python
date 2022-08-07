def rotate(io, d, ln):
    Lfirst = io [0: d]
    Lsecond = io [d:]
    Rfirst = io [0: len( io)-d]
    Rsecond = io [len( io)-d:]

    # now concatenate two parts together
    if (ln % 2) == 0:
        print( (Rsecond + Rfirst))
    else:
        print( (Lsecond + Lfirst))


# Driver program
if __name__ == "__main__":
    io = str(input())
    ln = int(input())
    if(ln%2)==0:
        d = 2
        rotate(io, d, ln)
    else:
        d = 3
        rotate( io, d, ln)

