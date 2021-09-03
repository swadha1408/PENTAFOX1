import itertools


def main():
    time_table, buffer = [], 0
    subjects = ["Cs", "Math", "Physics", "IT", "CyberSecurity"]
    perm_set = itertools.permutations(subjects)
    for day in perm_set:
        if buffer % 4 == 0:
            time_table.append(day)
        buffer += 1
    print("Total of 5 subjects with 1 hour dedicated for each subject per day")
    print("Time Table for 5 days: ", time_table)

    #timeTable.append(perm_set[:5])
    #print(timeTable)


if __name__ == "__main__":
    main()
