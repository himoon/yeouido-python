def dep():
    """dep.csv와 member.csv를 조인하여 depmember.csv를 만든다. dep-result.csv 참고"""
    fdep = open("dep.csv")
    fmember = open("member.csv")

    # dep dictionary
    header_dep = fdep.readline().strip().split(",")
    list_dep = []
    for row in fdep:
        data = row.strip().split(",")
        zipped = zip(header_dep, data)
        list_dep.append(dict(zipped))

    # member dictionary
    header_member = fmember.readline().strip().split(",")
    list_member = []
    for row in fmember:
        data = row.strip().split(",")
        zipped = zip(header_member, data)
        list_member.append(dict(zipped))

    # result list
    result = []
    result.append(["DEPNO", "DEPNM", "EMPNO", "EMPNAME"])  # insert header
    for dep in list_dep:
        depno = dep["DEPNO"]
        depnm = dep["DEPNM"]
        for member in list_member:
            if member["DEPNO"] == depno:
                row = [depno, depnm, member["EMPNO"], member["EMPNAME"]]
                result.append(row)

    # write csv file
    fw = open("dep-result.csv", "w")
    for line in result:
        fw.write(",".join(line)+"\n")

    # close file handler
    fdep.close()
    fmember.close()
    fw.close()


if __name__ == "__main__":
    dep()
