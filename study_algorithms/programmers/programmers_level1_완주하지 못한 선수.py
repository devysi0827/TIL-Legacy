def solution(participant, completion):
    participant.sort()
    completion.sort()
    i = 0
    while i<len(participant)-1:
        if participant[i] != completion[i]:
            return participant[i]
        i += 1
    return participant[-1]

participant=['marina', 'josipa', 'nikola', 'vinko', 'filipa']
completion= ['marina', 'josipa', 'nikola', 'filipa']
print(solution(participant, completion))