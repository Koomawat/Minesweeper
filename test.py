import random

def main():

    #listt = []

    #listt.append((1,2))
    #listt.append((3,4))

    #test = random.choice(listt)

    #print(test[1])

    #topRightCoords = [(1,-1), (1,0), (0,-1)]
                    #   SW,     S,      W

    #for x,y in topRightCoords:
    #    print(x, y)

    lst = permute([1,0,0])
    print(lst)

def permute(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #here we need a global wise list, each time we just append to the result
        rslt=[]
        
        def dfs(temp, elements):
            #gather rslt
            if len(elements)==0:
                rslt.append(temp[:]) #still remember to use temp[:]
            for e in elements:
                temp.append(e)
                #backtrack
                next_elements=elements[:]
                next_elements.remove(e)
                
                dfs(temp, next_elements)
                temp.pop()
                
                
        dfs([],nums) #first is the current result
        return rslt

if __name__ == "__main__":
    main()