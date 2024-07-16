# Python Script, API Version = V17
import glob
import os
os.chdir(r"D:\~\geometry_examples_for_fem_cfd\wing-with-winglet-1.snapshot.4")
#############################################################
# Works correctly if the leading edge has at least one point
# Will not work on a “clean” arc
#############################################################
abs_path = r"D:\~\geometry_examples_for_fem_cfd\wing-with-winglet-1.snapshot.4"   # path
model = "Wing_winglet_big.scdoc"    # model

def open_model():
    importOptions = ImportOptions.Create()    # settings are required
    # Choose a model
    DocumentOpen.Execute(os.path.join(abs_path, model),  importOptions)

def close_model():
    DocumentHelper.CloseDocument()

def sectionZ(planeZ):
    def decorMessage(mess):
        print('{0} {1} {2}'.format('#' * len(mess), (mess), ('#' * len(mess))))

    """
    Step 1
    Section by plane
    """
    datumPlane = DatumPlaneCreator.Create(Point.Create(0, 0, planeZ), Direction.DirZ).CreatedPlanes[0]  # create a plane
    surfSel = Selection.Create(GetRootPart().Bodies[0])                                                 # select the target body in the tree
    datumSel = Selection.Create(datumPlane)                                                             # select the plane created earlier
    SplitBody.Execute(surfSel, datumSel)                                                                # slicing
    for edge in GetRootPart().Bodies[0].Edges:                                                          # loop for extracting section curves
        if round(edge.Shape.StartPoint.Z, 2) == planeZ and round(edge.Shape.EndPoint.Z, 2) == planeZ:
            Copy.ToClipboard(Selection.Create(edge))
            result = Paste.FromClipboard()                                                              # there can be several curves in a section
    decorMessage('1/5-DONE!')

    """
    Step 2
    extract 3 pairs of points on lead edge and trail edge
    """
    from itertools import chain

    def removeDuplicates(listofElements):
        # Create an empty list to store unique elements
        uniqueList = []
        # Iterate over the original list and for each element
        # add it to uniqueList, if its not already there.
        for elem in listofElements:
            if elem not in uniqueList:
                uniqueList.append(elem)
        # Return the list of unique elements
        return uniqueList

    x = []  # initial list of coord points x
    y = []  # initial list of coord points y

    for point in GetRootPart().Curves:                      # extract ALL points from ALL section curves
        x_start = round(point.GetStartPoint().Point.X, 4)   # begin
        y_start = round(point.GetStartPoint().Point.Y, 4)   # begin

        x_mid = point.GetMidPoint().Point.X # middle
        y_mid = point.GetMidPoint().Point.Y # middle

        x_end = round(point.GetEndPoint().Point.X, 4) # end
        y_end = round(point.GetEndPoint().Point.Y, 4) # end

        x.append(x_start)
        #    x.append(x_mid)
        x.append(x_end)

        y.append(y_start)
        #    y.append(y_mid)
        y.append(y_end)

    #    coord = [x, y]
    #    coo = zip(x,y)
    # print x, y

    temp_y_nose = []
    temp_y_tail = []

    x_nose = x[x.index(min(x))]  # x-min coord
    x_tail = x[x.index(max(x))]  # x-max coord

    my_dict = {}

    for (ind, elem) in enumerate(x):
        if elem in my_dict:
            my_dict[elem].append(ind)
        else:
            my_dict.update({elem: [ind]})

    for key, value in my_dict.iteritems():
        if len(value) > 1 and key == x_nose:
            print("key x_nose (%s) has indices (%s)" % (key, value))
            for i in value:
                temp_y_nose.append(y[i])
                print(y[i])

    for key, value in my_dict.iteritems():
        if len(value) > 1 and key == x_tail:
            print("key x_tail (%s) has indices (%s)" % (key, value))
            for i in value:
                temp_y_tail.append(y[i])
                print(y[i])
    print(temp_y_tail)

    y_n = removeDuplicates(temp_y_nose)
    y_t = removeDuplicates(temp_y_tail)
    print(x_nose, y_n)
    print(x_tail, y_t)
    x_points = []
    y_points = []
    x_points.append(x_nose)
    x_points.append(x_tail)
    x_points.append(x_tail)

    y_points.append(y_n)
    y_points.append(y_t)
    y_points = list(chain.from_iterable(y_points))
    print(x_points, y_points)

    with open('temp_front_end.dat', 'w') as f: # file for head and tail points
        f.write('temp_front_end\n')
        for i, j in zip(x_points, y_points):
            f.write(str(i) + "\t" + str(j) + "\n")

    decorMessage('2/5-DONE!')
    #    print '{0} {1}'.format(x_start, y_start)
    #    print '{0} {1}'.format(x_mid, y_mid)
    #    print '{0} {1}'.format(x_end,y_end)

    """
    Step 3
    Define array of vertical lines
    """
    x0 = x_nose
    yUp = 25                #  in meters arbitrary
    yDown = -25             # in meters arbitrary
    b = x_tail - x_nose     # chord length
    datumSel = Selection.Create(GetRootPart().DatumPlanes[0])   # select the previously constructed plane
    ViewHelper.SetSketchPlane(datumSel, None)                   # activate sketch mode
    for i in range(1, 16):
        param = b / 16
        print(param * i)
        SketchLine.Create(Point2D.Create(M(x0 + param * i), M(yUp)), Point2D.Create(M(x0 + param * i), M(yDown))) # build a linear array of segments

    decorMessage('3/5-DONE!')

    """
    Step 4
    Extract middle points od airfoil
    """

    all_c = GetRootPart().Curves        # all curves
    vertical_lines = all_c[-1:-16:-1]   # vertical lines (there are fifteen of them) pay attention to the index (16), they are the last in the list
    profil_curves = all_c[-16::-1]      # other curves, they are at the beginning of the list

    vertical_linesSel = Selection.Create(vertical_lines)    # select vertical lines
    profil_curvesSel = Selection.Create(profil_curves)      # select section curves

    with open('temp_n_mid_points.dat', 'w') as f:           # file for intermediate points
        for i in range(len(vertical_lines)):
            for j in range(len(profil_curves)):
                test = GeometryHelper.CurveCurveIntersect(vertical_lines[i], profil_curves[j])
                for point in test.IntersectionPoints:
                    DatumPoint.Create(GetRootPart(), "pt_" + str(i) + "_" + str(j), point)
                    coord = point.X, point.Y
                    f.write('{} {}\n'.format(point.X, point.Y))
                #print(coord) 
    decorMessage('4/5-DONE!')

    """
    Step 5
    merge file into one txt file
    """
       
    read_files = glob.glob("*.dat")

    with open("1_result_z={}.txt".format(planeZ), "wb") as outfile:
        for f in read_files:
            with open(f, "rb") as infile:
                outfile.write(infile.read())

# comment this to check file layout  
    os.remove('temp_front_end.dat')
    os.remove('temp_n_mid_points.dat')
    print("File Removed!")
    decorMessage('5/5-DONE!')
    
def sectionY(planeY):
    def decorMessage(mess):
        """
     output decoration
     """
        print('{0} {1} {2}'.format('#' * len(mess), (mess), ('#' * len(mess))))

    """
    Step 1
    Section by plane
    """
    datumPlane = DatumPlaneCreator.Create(Point.Create(0, planeY, 0 ), Direction.DirY).CreatedPlanes[0] # create a plane
    surfSel = Selection.Create(GetRootPart().Bodies[0])                                                 # select the target body in the tree
    datumSel = Selection.Create(datumPlane)                                                             # select the plane created earlier
    SplitBody.Execute(surfSel, datumSel)                                                                # splitting
    for edge in GetRootPart().Bodies[0].Edges:                                                          # loop for extracting section curves
        if round(edge.Shape.StartPoint.Y, 2) == planeY and round(edge.Shape.EndPoint.Y, 2) == planeY:
            Copy.ToClipboard(Selection.Create(edge))
            result = Paste.FromClipboard()                                                              # there may be several curves in the section
    decorMessage('1/5-DONE!')

    """
    Step 2
    extract 3 pairs of points on lead edge and trail edge
    """
    from itertools import chain

    def removeDuplicates(listofElements):
        # Create an empty list to store unique elements
        uniqueList = []
        # Iterate over the original list and for each element
        # add it to uniqueList, if its not already there.
        for elem in listofElements:
            if elem not in uniqueList:
                uniqueList.append(elem)
        # Return the list of unique elements
        return uniqueList

    x = []  # initial list of coord points x
    z = []  # initial list of coord points y

    for point in GetRootPart().Curves: # извлекаем ВСЕ точки из ВСЕХ кривых сечения
        x_start = round(point.GetStartPoint().Point.X, 4) # начало
        z_start = round(point.GetStartPoint().Point.Z, 4) # начало

        x_mid = point.GetMidPoint().Point.X # середина
        z_mid = point.GetMidPoint().Point.Z # середина

        x_end = round(point.GetEndPoint().Point.X, 4) # конец
        z_end = round(point.GetEndPoint().Point.Z, 4) # конец

        x.append(x_start)
        #    x.append(x_mid)
        x.append(x_end)

        z.append(z_start)
        #    y.append(y_mid)
        z.append(z_end)

    #    coord = [x, y]
    #    coo = zip(x,y)
    # print x, y

    temp_z_nose = []
    temp_z_tail = []

    x_nose = x[x.index(min(x))]  # x-min coord
    x_tail = x[x.index(max(x))]  # x-max coord

    my_dict = {}

    for (ind, elem) in enumerate(x):
        if elem in my_dict:
            my_dict[elem].append(ind)
        else:
            my_dict.update({elem: [ind]})

    for key, value in my_dict.iteritems():
        if len(value) > 1 and key == x_nose:
            print("key x_nose (%s) has indices (%s)" % (key, value))
            for i in value:
                temp_z_nose.append(z[i])
                print(z[i])

    for key, value in my_dict.iteritems():
        if len(value) > 1 and key == x_tail:
            print("key x_tail (%s) has indices (%s)" % (key, value))
            for i in value:
                temp_z_tail.append(z[i])
                print(z[i])
    print(temp_z_tail)

    z_n = removeDuplicates(temp_z_nose)
    z_t = removeDuplicates(temp_z_tail)
    print(x_nose, z_n)
    print(x_tail, z_t)
    x_points = []
    z_points = []
    x_points.append(x_nose)
    x_points.append(x_tail)
    x_points.append(x_tail)

    z_points.append(z_n)
    z_points.append(z_t)
    z_points = list(chain.from_iterable(z_points))
    print(x_points, z_points)

    with open('temp_front_end.dat', 'w') as f: # file for head and tail points
        f.write('temp_front_end\n')
        for i, j in zip(x_points, z_points):
            f.write(str(i) + "\t" + str(j) + "\n")

    decorMessage('2/5-DONE!')
    #    print '{0} {1}'.format(x_start, y_start)
    #    print '{0} {1}'.format(x_mid, y_mid)
    #    print '{0} {1}'.format(x_end,y_end)

    """
    Step 3
    Define array of vertical lines
    """
    x0 = x_nose
    yUp = 50        # in meters arbitrary
    yDown = -50     # in meters arbitrary
    b = x_tail - x_nose # chord length
    datumSel = Selection.Create(GetRootPart().DatumPlanes[0])   # select the previously constructed plane
    ViewHelper.SetSketchPlane(datumSel, None)                   # activate sketch mode
    for i in range(1, 16):
        param = b / 16
        print(param * i)
    #    SketchLine.Create(Point2D.Create(M(x0 ), M(yUp)), Point2D.Create(M(x0), M(yDown))) #  a linear array of segments 
        SketchLine.Create(Point2D.Create(M(-x0-param * i ), M(yUp)), Point2D.Create(M(-x0-param * i), M(yDown)))
    decorMessage('3/5-DONE!')

    """
    Step 4
    Extract middle points od airfoil
    """

    all_c = GetRootPart().Curves        # all curves 
    vertical_lines = all_c[-1:-16:-1]   # vertical lines (there are fifteen of them) pay attention to the index (16), they are the last in the list
    profil_curves = all_c[-16::-1]      # other curves, they are at the beginning of the list

    vertical_linesSel = Selection.Create(vertical_lines)    # select vertical lines
    profil_curvesSel = Selection.Create(profil_curves)      # select section curves

    with open('temp_n_mid_points.dat', 'w') as f: # file for intermediate points
        for i in range(len(vertical_lines)):
            for j in range(len(profil_curves)):
                test = GeometryHelper.CurveCurveIntersect(vertical_lines[i], profil_curves[j])
                for point in test.IntersectionPoints:
                    DatumPoint.Create(GetRootPart(), "pt_" + str(i) + "_" + str(j), point)
                    coord = point.X, point.Z
                    f.write('{} {}\n'.format(point.X, point.Z))
                #print(coord) 
    decorMessage('4/5-DONE!')

    """
    Step 5
    merge file into one txt file
    """
       
    read_files = glob.glob("*.dat")

    with open("1_result_y={}.txt".format(planeY), "wb") as outfile:
        for f in read_files:
            with open(f, "rb") as infile:
                outfile.write(infile.read())

    # comment out to check file layout  
    os.remove('temp_front_end.dat')
    os.remove('temp_n_mid_points.dat')
    print("File Removed!")
    decorMessage('5/5-DONE!')

"""
manually enter a list of commands to execute.
loop if you want?
"""
#open_model()
#section(0) # set the Z coordinate for the section
#sectionZ(31.92)
sectionY(1.5)
#close_model() #comment out for tests
# the result should contain 33 lines (30 + 1 + 2), according to the number of points along X
    
