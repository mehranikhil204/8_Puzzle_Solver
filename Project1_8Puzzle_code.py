##########################################################################################
############################ Project-1 8-Puzzle ##########################################
############################### NIKHIL MEHRA #############################################
############################ UID : 116189941 #############################################
############################### Python 2.7 ###############################################

################################################################################
# Class Name - PuzzleBoard8
# Arguments for object Initialization - x, pid and sid
# x - Initial Puzzle Configuration in datatype list
# pid - Parent Id of the Node in datatype integer
# sid - Node Id in datatype integer 
# Method of class PuzzleBoard8
# zeroPosition() - To Determine the position of zero in our configuration
# checkGoal() -  To check whether our current configuration is goal configuration or not
# checkUp() - To determine if we can move up or not
# moveUp() - For moving upwards in the current configuration
# checkDown() - To determine if we can move down or not
# moveDown() - For moving downwards in the current configuration
# checkLeft() - To determine if we can move left or not
# moveLeft() - For moving leftwards in the current configuration
# checkRight() - To determine if we can move right or not
# moveRight() - For moving rightwards in the current configuration
# getParentId() - To get parent Id of the node
# getId() - To get Id of the node
# getNodeRow() - To get the current configuration of the node row-wise
# getNodeColumn() - To get the current configuration of the node column-wise
################################################################################

class PuzzleBoard8(object):
    
    def __init__(self, x, pid, sid): # Object Initialization
        self.y = {} # Dictionary 'y' for storing the Initial configuration
        self.goal = {(0,0):1, (0,1):2, (0,2):3, (1,0):4, (1,1):5, (1,2):6, (2,0):7, (2,1):8, (2,2):0} # Variable 'goal' for storing the goal configuration
        self.y[(0,0)] = x[0] 
        self.y[(0,1)] = x[1]
        self.y[(0,2)] = x[2]
        self.y[(1,0)] = x[3]
        self.y[(1,1)] = x[4]
        self.y[(1,2)] = x[5]
        self.y[(2,0)] = x[6]
        self.y[(2,1)] = x[7]
        self.y[(2,2)] = x[8]
        self.z = self.y.copy() # Coying variable y in z for future manipualation
        self.parentid = pid # Assiging pid to parentid
        self.sid = sid # Assiging sid to sid
    
    # To Determine the position of zero in our configuration
    # Returns a tuple containing the position of zero
    def zeroPosition(self): 
        #print(self.y)
        for i in self.y.keys(): # Looping through the keys in the dictionary
            if self.y[i] == 0: # If the value corresponding to the particular key is zero
                return i # Then returns the key i.e. location of the 'zero' in the configuration
        
    # To check whether our current configuration is goal configuration or not
    # Returns True or False corresponding to the matching of the configuration
    def checkGoal(self):    
        if self.goal == self.y: # If the current configuration is same as goal configuration  
            return True # Then returns True
        else:
            return False # Else returns False
            
    # To determine if we can move up or not
    # Returns True or False         
    def checkUp(self):  
        x,y = self.zeroPosition()
        if x == 0: # If row index of the position of 'zero' is 0  
            return False # Then we cannot move upwards hence returns False
        else:
            return True # Else returns True
         
    # For moving upwards in the current configuration
    # Returns list of the updated configuration
    def moveUp(self):
        x,y = self.zeroPosition() # row and column index of the position of zero
        swap = self.y[(x-1,y)] # Move upwards by decreasing the value of row index by one
        self.z[(x,y)] = swap # Swapping the values
        self.z[(x-1,y)] = 0
        l1 = [self.z[(0,0)],self.z[(0,1)],self.z[(0,2)],self.z[(1,0)],self.z[(1,1)],self.z[(1,2)],self.z[(2,0)],self.z[(2,1)],self.z[(2,2)]]
        self.z = self.y.copy()
        return l1   
            
    # To determine if we can move up or not
    # Returns True or False         
    def checkDown(self):
        x,y = self.zeroPosition()
        if x == 2: # If row index of the position of 'zero' is 2
            return False # Then we cannot move downwards hence returns False
        else:
            return True # Else returns True
            
    # For moving downwards in the current configuration
    # Returns list of the updated configuration
    def moveDown(self):  
        x,y = self.zeroPosition() # row and column index of the position of zero
        swap = self.y[(x+1,y)] # Move downwards by increasing the value of row index by one
        self.z[(x,y)] = swap # Swapping the values
        self.z[(x+1,y)] = 0
        l1 = [self.z[(0,0)],self.z[(0,1)],self.z[(0,2)],self.z[(1,0)],self.z[(1,1)],self.z[(1,2)],self.z[(2,0)],self.z[(2,1)],self.z[(2,2)]]
        self.z = self.y.copy()
        return l1       
            
    # To determine if we can move left or not
    # Returns True or False             
    def checkLeft(self):
        x,y = self.zeroPosition()
        if y == 0: # If column index of the position of 'zero' is 0
            return False # Then we cannot move leftwards hence returns False
        else:
            return True # Else returns True
            
    # For moving leftwards in the current configuration
    # Returns list of the updated configuration            
    def moveLeft(self): 
        x,y = self.zeroPosition() # row and column index of the position of zero
        swap = self.y[(x,y-1)] # Move leftwards by decreasing the value of column index by one
        self.z[(x,y)] = swap # Swapping the values
        self.z[(x,y-1)] = 0
        l1 = [self.z[(0,0)],self.z[(0,1)],self.z[(0,2)],self.z[(1,0)],self.z[(1,1)],self.z[(1,2)],self.z[(2,0)],self.z[(2,1)],self.z[(2,2)]]
        self.z = self.y.copy()
        return l1        
     
    # To determine if we can move right or not
    # Returns True or False          
    def checkRight(self):   
        x,y = self.zeroPosition()
        if y == 2: # If column index of the position of 'zero' is 2
            return False # Then we cannot move rightwards hence returns False
        else:
            return True # Else returns True
            
    # For moving righwards in the current configuration
    # Returns list of the updated configuration
    def moveRight(self): 
        x,y = self.zeroPosition() # row and column index of the position of zero
        swap = self.y[(x,y+1)] # Move rightwards by increasing the value of column index by one
        self.z[(x,y)] = swap # Swapping the values
        self.z[(x,y+1)] = 0
        l1 = [self.z[(0,0)],self.z[(0,1)],self.z[(0,2)],self.z[(1,0)],self.z[(1,1)],self.z[(1,2)],self.z[(2,0)],self.z[(2,1)],self.z[(2,2)]]
        self.z = self.y.copy()
        return l1 
    
    # To get parent Id of the node
    # Returns an integer
    def getParentId(self):
        return self.parentid
        
    # To get Id of the node
    # Returns an integer
    def getId(self):
        return self.sid
    
    # To get the current configuration of the node row-wise   
    # Returns the node in list format
    def getNodeRow(self):
        return [self.z[(0,0)],self.z[(0,1)],self.z[(0,2)],self.z[(1,0)],self.z[(1,1)],self.z[(1,2)],self.z[(2,0)],self.z[(2,1)],self.z[(2,2)]]   
        
    # To get the current configuration of the node column-wise
    # Returns node in list format
    def getNodeColumn(self):
        return [self.z[(0,0)],self.z[(1,0)],self.z[(2,0)],self.z[(0,1)],self.z[(1,1)],self.z[(2,1)],self.z[(0,2)],self.z[(1,2)],self.z[(2,2)]]
        
    def __str__(self):
        return '\t'+str(self.y[(0,0)])+' '+str(self.y[(0,1)])+' '+str(self.y[(0,2)])+'\n\t'+str(self.y[(1,0)])+' '+str(self.y[(1,1)])+' '+str(self.y[(1,2)])+'\n\t'+str(self.y[(2,0)])+' '+str(self.y[(2,1)])+' '+str(self.y[(2,2)])+'\n'

################################################################################
# Function Name - BFS (Breadth-First-Search)
# Arguments - config - Initial Configuration
# Returns path configurations and visited(explored) configurations
# Algorithm - Determines children nodes for each corresponding parent node, through
# four actions namely: 'UP','DOWN','LEFT' and 'RIGHT'. All the children nodes are 
# explored breadth-wise. If any node matches with our goal-configuration, then the
# solution has been determined. Print out the solution using the back-tracking alogrithm.
################################################################################

def BFS(config): 
    flag = 0 
    frontier = [PuzzleBoard8(config, 0, 1)] # Varaible for storing all the upcoming nodes
    visited = [] # Variable for storing all the visited nodes
    summary = [] # Variable for storing the whole summary of the program
    
    while len(frontier) != 0: # While frontier is not empty
        flag = flag + 1
        moves = ['UP','DOWN','LEFT','RIGHT'] # Four available actions
        currentSet = frontier.pop() # Current configuration, being popped from the 'frontier' list
        summary.append(currentSet.getNodeRow())
        visited.append(currentSet) # Current configuration is simultaneously added to the 'visited' list
        nextSet = None # Variable for storing the next configuration i.e. the child configuration
        if currentSet.checkGoal() == True: # Check whether the current configuration matches with the goal configuration
            path = [visited[-1]] # Goal Configuration is added to the final path
            # Backtracking
            while(path[0].getId() != 1): # While the node Id is not 1 i.e. Initial Configuration Id 
                for pattern in visited: # Looping on all the nodes in visited
                    if pattern.getId() == path[0].getParentId(): # Matching the parent Id of the goal node with the node Id of its parent
                        path = [pattern] + path # Adding its parent into the path
                        break
            print 'Answer to the given Pattern is : '
            for pattern in path: # Loop for printing the path
                print pattern
            return path, visited # Returning True i.e. the solution has been found
                
        else: # If the current node does not matches with the goal configuration
            for move in moves: # Looping over the moves
                if move == 'UP' and currentSet.checkUp() == True: # Check if we can move up
                    nextSet = currentSet.moveUp() # Then next set is stored with the current set moved up
                elif move == 'DOWN' and currentSet.checkDown() == True: # Check if we can move down
                    nextSet = currentSet.moveDown() # Then next set is stored with the current set down up
                elif move == 'LEFT' and currentSet.checkLeft() == True: # Check if we can move left
                    nextSet = currentSet.moveLeft() # Then next set is stored with the current set moved left
                elif move == 'RIGHT' and currentSet.checkRight() == True: # Check if we can move right
                    nextSet = currentSet.moveRight() # Then next set is stored with the current set moved right        
                if nextSet != None and not(nextSet in summary): # when the next set is not present in the summary
                    frontier = [PuzzleBoard8(nextSet, currentSet.getId(), len(visited)+len(frontier)+1)] + frontier # Adding the next child node into the queue
                nextSet = None

################################################################################
# Function Name - ifSolvable
# Arguments - node - Initial Configuration
# Returns boolean, True if the solution is solvable else False otherwise
# Algorithm - Determines if the current configuration is solvable or not. If the number 
# of inversions are odd then it is not solvable.
################################################################################ 
               
def ifSolvable(node):
    cnode = node[:]
    zindex = cnode.index(0) # Finding the index of 0
    cnode.pop(zindex) # Removing the zero from the configuration
    count = 0
    for i in range(0,len(cnode)-1): # Looping through all the elements in the initial configuration
        for j in range(i,len(cnode)): 
            if cnode[j] < cnode[i]: # If a smaller value is present after the current element 
                count = count + 1 # Then the count is increased by one
    if count%2 == 0: # If the value of count is even, then the configuration is solvable 
        return True
    else:
        print 'The configuration is not solvable'
        return False # Else if the value of count is odd, then the configuration is not solvable
                 
input1 = raw_input('Enter starting node row-wise e.g."1,2,3,4,5,6,7,8,0": ') # User Input
start_node = input1.split(',') 
start_node_list = []
for i in start_node:
    start_node_list.append(int(i)) # Convert the user input into usable format
    
if ifSolvable(start_node_list): # If the function is solvable, i.e. ifSolvable returns True
       
    path, visited = BFS(start_node_list) # Calling the Breadth-First-Search (BFS) function
    
    my_file = open('Nodes.txt','w+') # Opening Nodes.txt
    # It creates .txt file if not present
    my_file.truncate() # Remove any previous values present
    for node in visited: 
        for i in node.getNodeColumn():
            my_file.write(str(i) + '\t')
        my_file.write('\n')
    my_file.close()

    my_file = open('NodesInfo.txt','w+') # Opening NodesInfo.txt
    # It creates .txt file if not present
    my_file.truncate() # Remove any previous values present
    for node in visited:
        l1 = [node.getId(), node.getParentId(), node.getParentId()]
        for i in l1:
            my_file.write(str(i) + '\t')
        my_file.write('\n')
    my_file.close()

    my_file = open('NodePath.txt','w+') # Opening NodePath.txt
    # It creates .txt file if not present
    my_file.truncate() # Remove any previous values present
    for node in path:
        for i in node.getNodeColumn():
            my_file.write(str(i) + '\t')
        my_file.write('\n')
    my_file.close()
    
else:
    my_file = open('Nodes.txt','w+') # It creates .txt file if not present
    my_file.truncate() # Remove any previous values present
    my_file.close()    
    my_file = open('NodesInfo.txt','w+') # It creates .txt file if not present
    my_file.truncate() # Remove any previous values present
    my_file.close()
    my_file = open('NodePath.txt','w+') # It creates .txt file if not present
    my_file.truncate() # Remove any previous values present   
    my_file.close()     
