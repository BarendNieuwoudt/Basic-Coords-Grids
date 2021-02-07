class BasicGrid:
	
	def __init__(self, width, height):
		self.coordinates = []
		self.width = width
		self.height = height
		self.grid = ''
		self.generateGrid()
	
	def addCoordinate(self, Coordinate):
		self.coordinates.append(Coordinate)
		# only regenerate the grid if something changed.
		self.generateGrid(self)
		
	def getCoordinateAt(self, x, y):
		# Return a coordinate object if one exists for X and Y
		for coord in self.coordinates:
			if coord.getX() == x and coord.getY() == y:
				return coord
		return None
		
	def show(self):
		# Display the Grid
		print(self.grid)
		
	# Display this grid, where 0,0 is in the top left corner.
	def generateGrid(self, printAxisValues = True):
		self.grid = ''
		x, y = 0, 0
		
		# Print headers for the x axis
		if printAxisValues:
			self.grid += '   '
			
			# Print numbers from 0 to max width
			for x in range(self.width):
				self.grid += str(x % 10) + ' '

			self.grid += '\n  -'

			# Print line underneath all the x coordinates
			for x in range(self.width):
				self.grid += '--'

			self.grid += '\n'

		# Print the Grid Data
		for y in range(self.height):
			
			if printAxisValues:
				# Print Border on the left of the grid
				self.grid += str(y % 10) + '| '
			
			for x in range(self.width):
				coord = self.getCoordinateAt(x, y)
				x += 1
				if coord is None:
					self.grid += '. '
				else:
					self.grid += coord.getIcon() + ' '
			
			if printAxisValues:
				# Print border on the right of the grid
				self.grid += '|'
			
			self.grid += '\n'
			y += 1
		
		if printAxisValues:
			# Print line underneath the grid.
			self.grid += '  -'
			for x in range(self.width):
				self.grid += '--'
		