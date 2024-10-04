
import numpy 
import numpy as np
import math 
import random
from math import *
import colorama
from colorama import Fore
from tqdm import tqdm

class model():
    
    def __init__(self ,   fitness_function  , num_of_parameters   , initialize_iteration  , PFA_iteration , alpha =1  , beta=1 , converging_threshold = 0.001  , lb =-1, ub=1 ):
        

        self.fitness_function = fitness_function
        self.num_of_param     = num_of_parameters
        
        self.IT   = initialize_iteration
        self.IT2  = PFA_iteration
        self.alpha= alpha
        self.beta = beta
        self.conv = converging_threshold
        self.lb = lb
        self.ub = ub


    
    def fit(self):
        self.Conv_curve = [ ]
        sol = numpy.zeros(self.num_of_param)
        self.best_sol= numpy.random.rand(self.num_of_param)
        self.best_fit = self.fitness_function(sol )
        Dict = {}
        Loss={}
        mem=0
        
        """  --  initialize -- """
        it=0 

        self.best_fit = 9*10**100
        
        sol_ = np.random.normal( self.lb , self.ub  , (self.IT , self.num_of_param) )

        while it<self.IT or mem<2 :
            it+=1
            sol = sol_[it-1]
            self.fitness = self.fitness_function(sol)
            if self.fitness < self.best_fit :
                self.Conv_curve.append(self.fitness)
                mem+=1
                self.best_fit=self.fitness
                self.best_sol=sol
                Dict[str(mem)]=sol
                Loss[str(mem)]=self.fitness
                # print("Solution :",sol)
                # print("fitness = ",self.fitness)
                
        self.num_of_mem = len(Dict)
            
        self.best_sol=Dict[str(self.num_of_mem)]
        self.best_fit=self.fitness_function(Dict[str(self.num_of_mem)])
        
        # for i in Dict :
        #     print(i , Dict[i])
        

        
        position={}
        
        position["0"]=Dict[str(self.num_of_mem-1)]
        position["1"]=Dict[str(self.num_of_mem)]
        
        
        self.Conv_curve.append(self.best_fit)
        
        for it in  tqdm(range(1,self.IT2), desc= 'optimization' , ncols= 100  ,colour='blue'): 
            r1_ = np.random.uniform(0, 1, (  self.num_of_mem , self.num_of_param))
            r2_ = np.random.uniform(0, 1, (  self.num_of_mem , self.num_of_param))
            u1_ = np.random.uniform(-1, 1, (  self.num_of_mem , self.num_of_param))
            u2_ = np.random.uniform(-1, 1, (  self.num_of_mem , self.num_of_param))
            r3_ = np.random.uniform(0, 1, (  self.num_of_mem , self.num_of_param))




            for mem in range(2,self.num_of_mem+1):
                
                
                R1=self.alpha*r1_[mem-2]
                R2=self.beta*r2_[mem-2]
                
                D=abs(Dict[str(mem)]-Dict[str(mem-1)])
                dif = Dict[str(mem)]-Dict[str(mem-1)]
                
                A= u2_[mem-2] *exp(-2*it/self.IT2)
                position[str(it+1)] =  position[str(it)] + 2* r3_[mem-2] *(position[str(it)]-position[str(it-1)])+A
                epsilon = (1-it/self.IT2)*u1_[mem-2]*D
                sol = Dict[str(mem)]
                dpos= position[str(it+1)]-sol
                sol =  sol+R1*dif+R2*dpos+epsilon
                self.fitness=self.fitness_function(sol )
                
                if self.fitness<Loss[str(mem)]:
                    # print(it,"of",self.IT2)
                    Dict[str(mem)] = sol
                    Loss[str(mem)] = self.fitness
                
                if self.fitness< self.best_fit :
                    self.best_sol = sol
                    self.best_fit = self.fitness
                    self.Conv_curve.append(self.fitness)
                    print(self.best_fit )


                position[str(it)] = self.best_sol
            position[str(it+1)] = self.best_sol
        
        if abs(self.Conv_curve[-2]-self.Conv_curve[-1]) > self.conv :
            
            print( Fore.RED + '  warning :  Converging threshold is not satisfied ' )