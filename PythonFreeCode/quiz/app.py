from Question import Question

question_prompts = [
    "What is the capital of France?\n(a) Berlin\n(b) Madrid\n(c) Paris\n\n",
    "What is 2 + 2?\n(a) 3\n(b) 4\n(c) 5\n\n"
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "b")  
]