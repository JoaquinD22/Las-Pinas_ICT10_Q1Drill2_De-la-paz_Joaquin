from pyscript import document

def analyze_message(event):
    name = document.getElementById("info1").value.strip()
    age = document.getElementById("info2").value.strip()
    school = document.getElementById("info3").value.strip()

    message = f"Name: {name}, Age: {age}, School: {school}"
    print(message)
    document.getElementById("message1").innerHTML = message

    message2 = f"This person's name is {name}, and they're {age} years old. This person is currently studying in {school}, which is a very very okay school, and they're a big and true Ado fan!!!!!!! (ADO WORLD DOMINATION)"
    print(message2)
    document.getElementById("message2").innerHTML = message2
