from pyscript import display, document # type: ignore

def compute_ave(e):
    #when you put in a value this will convert the input into float
    Score1 = float(document.getElementById("score1").value)
    Score2 = float(document.getElementById("score2").value)

    #formula to compute the average
    average = (Score1 + Score2) / 2

    #the code here determines whether u pass or not
    if average >= 75:
        result = "You Passed :D"
    else:
        result = "You Failed D:"

    #the code here displays the result and whether you passed or not for you to see :)
    display(average, target="ave")
    display(result, target="result")