def maxProfitAssignment(difficulty, profit, worker):
    jobs = sorted(zip(difficulty, profit))
    res = i = best = 0
    for ability in sorted(worker):
        while i < len(jobs) and ability >= jobs[i][0]:
            best = max(jobs[i][1], best)
            i += 1
            print(jobs,best)
        res += best
    return res

#Main Program
diff = [2,4,6,8,10]
pro = [10,20,30,40,50]
w = [4,5,6,7]
print(maxProfitAssignment(diff, pro, w))
