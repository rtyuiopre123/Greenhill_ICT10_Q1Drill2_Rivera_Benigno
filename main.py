from pyscript import display, document

def generate_profile(e):
    # collect inputs
    name = document.getElementById('name').value
    age = document.getElementById('age').value
    school = document.getElementById('school').value

    # formatted multiline string with escape characters
    profile_message = f"""
    📘 Student Profile
    Name:\t {name}
    Age:\t {age}
    School:\t {school}

    📝 Notes:
    \"{name}\" is currently {age} years old and studies at {school}.
    
    This information was gathered through input fields and displayed
    using a multiline string in Python via PyScript.
    """

    # clear old output
    display("", target="output")

    # show result
    display(profile_message, target="output")
