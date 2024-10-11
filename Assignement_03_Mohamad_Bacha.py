def CountDigits(number):
    if number == 0:
        return 0
    else:
        return 1 + CountDigits(abs(number)//10)
          
def FindMax(List):
    if len(List)==1:
        print(List[0])
    else:
        m=List[0]
        for i in List:
            if i > m:
                m=i
    return m   

def getMultiline(html):
    print("Please enter your html code(NB: press enter twice to finish): ")
    while True:
        Line=input()
        if Line == "":
            break
        html.append(Line)
    CountTags(html)                 
            
               
def CountTags(html):
    html_tags = ['<!DOCTYPE html>', '<html>', '<head>', '<title>', '<meta>', '<link>', '<style>', '<script>', '<body>', '<h1>', '<h2>', '<h3>', '<h4>', '<h5>', '<h6>', '<p>', '<a>', '<img>', '<div>', '<span>', '<ul>', '<ol>', '<li>', '<table>', '<tr>', '<td>', '<th>', '<form>', '<input>', '<button>', '<label>', '<select>', '<option>', '<textarea>', '<br>', '<hr>', '<footer>', '<header>', '<section>', '<article>', '<aside>', '<nav>', '<figure>', '<figcaption>', '<details>', '<summary>', '<time>', '<mark>', '<progress>', '<meter>', '<blockquote>', '<cite>', '<data>', '<abbr>', '<address>', '<bdi>', '<bdo>', '<del>', '<ins>', '<s>', '<u>', '<small>', '<strong>', '<em>', '<kbd>', '<sub>', '<sup>', '<code>', '<var>', '<samp>', '<pre>', '<iframe>', '<canvas>', '<svg>', '<video>', '<audio>', '<source>', '<track>', '<map>', '<area>', '<picture>', '<template>', '<slot>', '<noscript>', '<script>', '<style']
    common_elements = []
    count_elements={}
    for i in html:
        if i in html_tags:
            common_elements.append(i) 
    for i in common_elements:
        if i in count_elements:
            count_elements[i]+=1
        else:
            count_elements[i]=1    
    print(count_elements)        



def DisplayMenu():
    print( "The List is:\n" + "1- Count Digits\n" + "2- Find Max\n" + "3- Count Tags\n" + "4- Quit\n")
    choice=int(input("Please choose from the list: "))
    while (choice!=4):
        if choice==1:
            number =int(input("Please input a number: "))
            if number==0:
                print("The digit is 1")
            else:
                CountDigits(number)
                result=CountDigits(number)
                print("The digits of", number , "is" , result)
                DisplayMenu()
            
        elif choice==2:
            List=[]
            N=int(input("Please enter how many numbers you want to enter in this list: "))
            for i in range(N):
                Integer=int(input("Please enter a number: "))
                List.append(Integer)
            FindMax(List)
            N=FindMax(List)
            print("The maximum value of your list is" , N )
            DisplayMenu()

        elif choice==3:
            CountTags()
            html=[]
            getMultiline(html)
            DisplayMenu()

        elif choice==4:
            break
    else:
        print("Invalid input ")  
        DisplayMenu()    

DisplayMenu()     