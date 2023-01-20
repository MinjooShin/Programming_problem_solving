def strreverse(str):
    tmp_list = list(str)
    for i in range(int(len(str)/2)):
        tmp= tmp_list[i]
        tmp_list[i]=tmp_list[len(str)-1-i]
        tmp_list[len(str)-1-i]=tmp
    result = ''.join(tmp_list)
    return result

def solution(skill, skill_trees):
    answer = 0
    skill=strreverse(skill)
    print(skill)
    for r in range (len(skill_trees)):
        skill_trees[r]=strreverse(skill_trees[r])
        print(answer)
        print(skill_trees[r],"")
        
        tmp = -1
        for i in range (len(skill)):
            if ( tmp != -1 and skill_trees[r].find(skill[i]) == -1):
                tmp = -2
                break
            if ( tmp > skill_trees[r].find(skill[i])):
                continue
            tmp = skill_trees[r].find(skill[i])
        
        if (tmp == skill_trees[r].find(skill[len(skill)-1])): answer=answer+1 
        """
        for s in range (len(skill_trees[r])):
            if(skill_trees[r][s]==skill[i]):
                s=s-1
                i=i+1
            if(i==len(skill)):
                answer=answer+1
                break;
        """
    return answer
