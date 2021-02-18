#!/usr/bin/python3
'''
The first exercise is related to basic class definition. Create a program which has a class Player, which has two attributes, teamcolor and points. Then create a main function which creates an object from this class, gives its attributes values "Blue" and "300". After this, make the program print the object data in the form "The [color] contender has [points] points!" like this:




		
>>> 
The Blue contender has 300 points!
>>> 		
'''


class Player():
	
	points = 0
	teamcolor = ""
	def tellscore(self):
		print("I am ", self.teamcolor , " , we have ", self.points, "!")
	def goal(self):
		self.points = self.points + 1
	
def main():
	team = Player()
	team.teamcolor = "Blue"
	team.points = 1
	team.goal()
	team.tellscore()
if __name__ == "__main__":
	main()