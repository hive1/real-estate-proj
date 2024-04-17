import math

# Find the averages of input lists, most likely containing string characters
# Remember to ignore the values associated with '-'
def findAvg(coll: list) -> int:
    total = 0
    count = 0

    for elem in coll:

        # Isolates whatever information is behind the space
        try:
            number = float(elem.split()[0])
            total += number
            count += 1

        except ValueError:
            continue

    return total/count
         
def main():
    ex = ['2.5 baths', '2.5 baths', '1.5 baths', '2.5 baths', '2.5 baths', 
          '1 bath', '2.5 baths', '1 bath', '8 baths', '2.5 baths', '1 bath', 
          '2.5 baths', '3.5 baths', '9 baths', '2.5 baths', '3 baths', '5.5 baths', 
          '2.5 baths', '5.5 baths', '3.5 baths', '— baths', '— baths', '— baths', 
          '— baths', '— baths', '— baths', '— baths']
    
    print(findAvg(ex))


if __name__ == '__main__':
    main()
