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
    f = open("./src/cities.csv")
    fw = open("./src/cities.out.csv", "w")

    # 2. read data.
    # https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects
    # https://docs.python.org/3/library/stdtypes.html?highlight=split#str.split
    # https://docs.python.org/3/library/stdtypes.html?highlight=split#str.strip
    # https://docs.python.org/3/library/stdtypes.html?highlight=split#str.rstrip
    # https://docs.python.org/3/library/stdtypes.html?highlight=split#str.join
    # https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
    # 2.1. loop data.
    for line in f:
        line_ = line.strip()
        if not len(line_):
            continue

        # 2.2. split line.
        splitted = line_.split(",")
        # 2.3. strip column.
        list_ = []
        for col in splitted:
            stripped = col.strip()
            try:
                float(stripped)
                list_.append(stripped)
            except:
                if '"' not in stripped:
                    list_.append("\""+stripped+"\"")
                else:
                    list_.append(stripped)

        # 2.4. write out file.
        fw.write(",".join(list_) + "\n")
    # 3. close file object.
    f.close()
    fw.close()


def hw_200():
    """# 작성조건
1. `hw_200.csv` 파일을 읽으세요.
2. Height 컬럼의 평균(mean)을 구한 뒤, 평균 이상에 해당되는 데이터만 추출하여 `hw_200.out.csv` 파일을 작성하세요.
# 참고 사이트
https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions"""
    # code goes here
    # 1. open csv file.
    f = open("./src/hw_200.csv")
    fw = open("./src/hw_200.out.csv", "w")

    # 2. read data.
    # 2.1. loop data.
    output = []
    list_height = []
    sum_height = 0
    mean_height = 0
    for line in f:
        line_ = line.strip()
        if not len(line_):
            continue

        # 2.2. split line.
        splitted = line_.split(",")

        # 2.3. strip column data.
        stripped = []
        for col in splitted:
            stripped.append(col.strip())
        output.append(stripped)

        # 2.4. get height, calculate mean of list_height
        try:
            height = float(splitted[1])
            list_height.append(height)
            sum_height += height
        except:
            continue
    mean_height = sum_height / len(list_height)

    # 3. filter data, then write a file.
    fw.write(",".join(output[0]) + "\n")
    # using list slicing
    for line in output[1:]:
        height = float(line[1])
        if height >= mean_height:
            fw.write(",".join(line) + "\n")

    # using list comprehension
    # for x in [line for line in output[1:] if float(line[1]) >= mean_height]:
    #     fw.write(",".join(x) + "\n")

    # 4. close file objects.
    f.close()
    fw.close()


if __name__ == "__main__":
    cities()
    hw_200()
