# See http://docs.python.org/2/library/string.html#format-specification-mini-language
# for Python string formatting mini-language

'''
    A set of simple classes and functions to allow the creation of OpenSCAD
    files using Python.  Done in a very simple OOP way; not engineered 
    in a Pythonic way.  Used as starting code for CS 314 Lab 2
'''

class Sphere:
    '''A sphere at the origin of the coordinate system.'''
    
    template = 'sphere( r = {radius}, $fa = {fa}, $fs = {fs}, $fn = {fn} );'
    
    def __init__(self, radius, fa=12, fs=2, fn=0):
        '''Initialize a sphere to the given values.  The special
        parameters fa, fs and fn have default values the same as
        in OpenSCAD'''
        # store parameters in a dictionary
        self.a = 5
        self.params = dict()
        self.params['radius'] = radius
        self.params['fa']     = fa          # Minimum angle in degrees for a fragment
        self.params['fs']     = fs          # Angle in mm
        self.params['fn']     = fn          # Resolution
        
    def __str__(self):
        ''' Return a string representation of this object.
            The equivalent of toString() in Java
        '''
        return Sphere.template.format(**self.params)
		
class Cylinder:
    '''A sphere at the origin of the coordinate system.'''
    
    template = 'color("LightSlateGrey") cylinder( h = {height}, r = {radius}, $fa = {fa}, $fs = {fs}, $fn = {fn} );'
    
    def __init__(self, height, radius, fa=12, fs=2, fn=0):

        # store parameters in a dictionary
		self.a = 6
		self.params = dict()
		self.params['height'] = height
		self.params['radius'] = radius
		self.params['fa']     = fa          # Minimum angle in degrees for a fragment
		self.params['fs']     = fs          # Angle in mm
		self.params['fn']     = fn          # Resolution
    def __str__(self):
		return Cylinder.template.format(**self.params)
		
class Cube:
    '''A cube at the origin of the coordinate system.'''
    
    template = 'cube( s = {side}, $fa = {fa}, $fs = {fs}, $fn = {fn} );'
    
    def __init__(self, side, fa=12, fs=2, fn=0):
        '''Initialize a sphere to the given values.  The special
        parameters fa, fs and fn have default values the same as
        in OpenSCAD'''
        # store parameters in a dictionary
        self.a = 5
        self.params = dict()
        self.params['side'] = side
        self.params['fa']     = fa          # Minimum angle in degrees for a fragment
        self.params['fs']     = fs          # Angle in mm
        self.params['fn']     = fn          # Resolution
        
    def __str__(self):
        ''' Return a string representation of this object.
            The equivalent of toString() in Java
        '''
        return Cube.template.format(**self.params)

def difference( objList ):
    '''
        Take the difference between the first object in a list
        and the remaining items.  Returns a string.
    '''
    # First make sure we're dealing with strings
    objListStrings = []
    for obj in objList:
        if not isinstance(obj,str):
            obj = str(obj)
        objListStrings.append(obj)
    contents = "".join(objListStrings)
    return 'difference(){{ {} }}'.format(contents)

	
def union( objList ):
	'''
		Union the list of objects
	'''
	objListStrings = []
	for obj in objList:
		if not isinstance(obj,str):
			obj = str(obj)
		objListStrings.append(obj)
	contents = "".join(objListStrings)
	return 'union(){{{}}}'.format(contents)
	
def intersection( objList ):
	objListStrings = []
	for obj in objList:
		if not isinstance(obj,str):
			obj = str(obj)
		objListStrings.append(obj)
	contents = "".join(objListStrings)
	return 'intersection(){{{}}}'.format(contents)

def translate(obj, x, y, z ):
    '''
        Translate an object by the given amounts.
        Returns a string.
    '''
    # if it isn't a string yet, turn it into one
    if not isinstance(obj,str):
        obj = str(obj)
    # now wrap it in the translation code
    return 'translate(v=[{0},{1},{2}]){{ {3} }}'.format(x, y, z, obj)

def rotate(d, x, y, z ):
	'''
	rotate object by the given amount and returns a string
	'''
	return 'rotate(a={0}, v=[{1},{2},{3}])'.format(d, x, y, z)

def scale(x, y , z):
	'''scale object by given vector'''
	return 'scale(v=[{1},{2},{3}])'.format(x, y, z)

def save(pathToNewFile, obj):
    with open(pathToNewFile,'w') as fout:
        fout.write(str(obj))
        