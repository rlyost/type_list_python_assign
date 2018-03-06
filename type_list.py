#input 1
# l = ['magical unicorns',19,'hello',98.98,'world']
#output
#"The list you entered is of mixed type"
#"String: magical unicorns hello world"
#"Sum: 117.98"

# input 2
# l = [2,3,1,7,4,12]
#output
#"The list you entered is of integer type"
#"Sum: 29"

# input 3
l = ['magical','unicorns']
#output 
#"The list you entered is of string type"
#"String: magical unicorns"


count = 0
newstr = ""
for x in l:
    if type(x) == int or type(x) == float:
        count = count + x
    if type(x) == str:
        newstr = newstr + " " + x
if len(newstr) > 0:
    if count > 0:
        print "The list you entered is of mixed type"
        print "String:",newstr
        print "Sum:", count
    else:
        print "The list you entered is of string type"
        print "String:",newstr
else:
    if count > 0:
        print "The list you entered is of integer type"
        print "Sum:", count



