def oddTuple(aTup: tuple)-> tuple:
    return aTup[::2]
def main()-> None:
    print(oddTuple(('I', 'am', 'a', 'test', 'tuple')))

if __name__ == "__main__":
    main()
