def cities():
    """# 작성조건
1. `cities.csv` 파일을 읽으세요.
2. 각 필드별로 빈 공백을 제거한 후, `cities.out.csv`파일을 작성하세요.
3. 문자타입의 컬럼은 반드시 따옴표를 붙이세요.
# 참고 사이트
https://docs.python.org/3/library/functions.html#built-in-functions
https://stackoverflow.com/questions/4843173/how-to-check-if-type-of-a-variable-is-string
https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals"""
    # code goes here

    # 1. open csv file.
    # https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

    # 2. read data.
    # https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects
    # 2.1. loop data.
    # https://docs.python.org/3/library/stdtypes.html?highlight=split#str.rstrip
    # 2.2. split line.
    # https://docs.python.org/3/library/stdtypes.html?highlight=split#str.split
    # 2.3. strip column.
    # https://docs.python.org/3/library/stdtypes.html?highlight=split#str.strip
    # https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
    # 2.4. write out file.
    # https://docs.python.org/3/library/stdtypes.html?highlight=split#str.join

    # 3. close file object.

    pass


def hw_200():
    """# 작성조건
1. `hw_200.csv` 파일을 읽으세요.
2. Height 컬럼의 평균(mean)을 구한 뒤, 평균 이상에 해당되는 데이터만 추출하여 `hw_200.out.csv` 파일을 작성하세요.
# 참고 사이트
https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions"""
    # code goes here
    # 1. open csv file.
    # 2. read data.
    # 2.1. loop data.
    # 2.2. split line.
    # 2.3. strip column data.
    # 2.4. get height, calculate mean of list_height.
    # 3. filter data, then write a file.
    # 4. close file objects.

    pass


if __name__ == "__main__":
    cities()
    hw_200()
