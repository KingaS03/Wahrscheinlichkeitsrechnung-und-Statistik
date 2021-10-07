from IPython.display import display, Latex, Markdown

class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
       rf"""**Frage 4:** Was ist die Varianz der statistischen Variable $X$ mit den Werten $x_1 = 0, x_2 = 2, x_3 = 4, x_4 = 7$ und enstprechenden Wahrscheinlichkeiten $p_1 = \frac{1}{8}, p_2 = \frac{1}{4}, p_3 = \frac{3}{8}, p_4 = \frac{1}{4}$? Geben Sie die Antwort auf zwei Nachkommastellen abgerundet an: """,
     rf"""**Frage 5:** Was ist die Varianz der Variable $X+3$? 

(a) Die Varianz ist dieselbe wie bei $X$, nämlich $V(X+3) = V(X)$. 

(b) Die Varianz wird um 3 Einheiten kleiner, nämlich $V(X+3) = V(X) - 3$. 

(c) Die Varianz wird um 3 Einheiten grösser, nämlich $V(X+3) = V(X) + 3$. 

Tragen Sie den Buchstabe der richtigen Antwort ein: """,
     rf"""**Frage 6:** Was ist die Varianz der neuen Variable $\frac{1}{2}X$? 

(a) Die Varianz ändert sich um einen Faktor von $\frac{1}{2}$ ab, nämlich $V\left(\frac{1}{2}X\right) = \frac{1}{2} V(X)$. 

(b) Die Varianz ändert sich um einen Faktor von $\frac{1}{4}$ ab, nämlich $V\left(\frac{1}{2}X\right) = \frac{1}{4} E(X)$. 

(c) Die Varianz ändert sich um einen Faktor von $4$ ab, nämlich $V\left(\frac{1}{2}X\right) = 4 E(X)$. 

(d) Die Varianz ändert sich um einen Faktor von $2$ ab, nämlich $V\left(\frac{1}{2}X\right) = 2 E(X)$. 

(e) Die Varianz ist dieselbe wie bei $X$, nämlich $V\left(\frac{1}{2}X\right) = V(X)$. 

Tragen Sie den Buchstabe der richtigen Antwort ein: """
]

questions = [
     Question(question_prompts[0], "5.19"),
     Question(question_prompts[1], "a"),
     Question(question_prompts[2], "b")
]

def run_quiz(questions):
    for question in questions:
        display(Markdown(question.prompt))
        answer = input()
        if answer == question.answer:
            display(Markdown(f'Richtige Antwort. Gut gemacht!'))
        else:
            display(Markdown(f'Falsche Antwort. Die richtige Antwort ist: '+'$'+question.answer+'$.'))
            
run_quiz(questions)