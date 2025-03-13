import json

def loadData() -> str:
    branch = input("Enter Prefered Branch(Enter any one from following: CSE, CSM, IT, CSD, ECE):").lower()
    fileName = open(branch + ".json",'r')
    return fileName

def findCaste() -> int:
    caste = input("Enter caste(OC, BCD, SC, ST):").upper()
    groups = {"OC" : 1, "BCD" : 2, "SC" : 3, "ST" : 4}
    return groups[caste]
    
def checkLimit(flag: int, rank: int) -> bool:
    return False if rank > limit[flag] else True
 
def printClgs():
    check = False
    rank = int(input("Enter Candidate's Rank:"))
    flag  = findCaste()
    if not checkLimit(flag, rank):
        print("Regrettably, our data is limited to ranks upto %d."%(limit[flag]))
    else:
        data = json.load(loadData())
        dictData = {}
        
        for index in range(1, len(data) + 1):
            dictData[data[str(index)][flag]] = data[str(index)][0]
            
        sorted_dict = dict(sorted(dictData.items()))
        
        
        print("\nHere is a list of colleges available for your rank:",end = "\n\n")  
        print("Closing rank \t-> \t College Name\n")
        
        for cutoff in sorted_dict:
            if rank <= int(cutoff):
                check = True
                print(cutoff,'\t\t->\t',sorted_dict[cutoff])
        if check == False:
            print("Unfortunately we could not find a suitable college for you.")
    
limit = [0,30250,38700,88090,66650]
printClgs()

