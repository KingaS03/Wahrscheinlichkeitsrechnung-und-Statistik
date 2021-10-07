from IPython.display import display, Latex, Markdown

class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     rf"""**Frage 1:** Was ist der Erwartungswert der statistischen Variable $X$ mit den Werten $x_1 = 0, x_2 = 2, x_3 = 4, x_4 = 7$ und enstprechenden Wahrscheinlichkeiten $p_1 = \frac{1}{8}, p_2 = \frac{1}{4}, p_3 = \frac{3}{8}, p_4 = \frac{1}{4}$? Geben Sie die Antwort auf zwei Nachkommastellen abgerundet an: """,
     rf"""**Frage 2:** Was ist der Erwartungswert der neuen Variable $Y = X+3$? 

(a) Der Erwartungswert ist derselbe wie bei $X$, nämlich $E(X+3) = E(X)$. 

(b) Der Erwartungswert wird um 3 Einheiten kleiner, nämlich $E(X+3) = E(X) - 3$. 

(c) Der Erwartungswert wird um 3 Einheiten grösser, nämlich $E(X+3) = E(X) + 3$. 

Tragen Sie den Buchstabe der richtigen Antwort ein: """,
     rf"""**Frage 3:** Was ist der Erwartungswert der neuen Variable $Z = \frac{1}{2}X$? 

(a) Der Erwartungswert ist derselbe wie bei $X$, nämlich $E\left(\frac{1}{2}X\right) = E(X)$. 

(b) Der Erwartungswert ändert sich um einen Faktor von $\frac{1}{2}$ ab, nämlich $E\left(\frac{1}{2}X\right) = \frac{1}{2} E(X)$. 

(c) Der Erwartungswert ändert sich um einen Faktor von $2$ ab, nämlich $E\left(\frac{1}{2}X\right) = 2 E(X)$. 

Tragen Sie den Buchstabe der richtigen Antwort ein: """
]

questions = [
     Question(question_prompts[0], "3.75"),
     Question(question_prompts[1], "c"),
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