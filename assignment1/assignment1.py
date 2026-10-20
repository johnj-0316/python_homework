# Task 1
def hello() -> str:
    return "Hello!"

# Task 2
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Task 3
def calc(
        num1: int | float,
        num2: int | float,
        op: str = "multiply"
    ) -> int | float | str:
    try:
        match op:
            case "add":
                return num1 + num2
            case "subtract":
                return num1 - num2
            case "multiply":
                return num1 * num2
            case "divide":
                return num1 / num2
            case "modulo":
                return num1 % num2
            case "int_divide":
                return num1 // num2
            case "power":
                return num1 ** num2
            case _:
                return "Invalid operator!"
    except ZeroDivisionError as e:
        return "You can't divide by 0!"
    except Exception as e:
        return "You can't multiply those values!"

# Task 4
def data_type_conversion(value, type) -> float | str | int:
    try:
        match type:
            case "float":
                return float(value)
            
            case "str":
                return str(value)
            
            case "int":
                return int(value)
            
            case _:
                return "Invalid name!"
            
    except Exception as e:
        return f"You can't convert {value} into a {type}."
    
# Task 5
def grade(*args) -> str:
    try:
        grade_sum = sum(args)
        grade_avg = grade_sum / len(args)
        
        if grade_avg >= 90:
            return "A"
        elif grade_avg >= 80:
            return "B"
        elif grade_avg >= 70:
            return "C"
        elif grade_avg >= 60:
            return "D"
        else:
            return "F"
        
    except Exception as e:
        return "Invalid data was provided."
    
# Task 6
def repeat(string: str, count: int) -> str:
    res = ""
    
    for num in range(count):
        res += string
        
    return res    

# Task 7
def student_scores(return_type: str, **kwargs) -> float | str:
    sum = 0
    max = float("-inf")
    best = ""
    
    for name, score in kwargs.items():
        if score > max:
            max = score
            best = name
        
        sum += score
        
    avg = sum / len(kwargs.items())
    
    if return_type.lower() == "best":
        return best
    elif return_type.lower() == "mean":
        return avg
    else:
        return "Invalid return type!"
    
# Task 8
def titleize(string: str) -> str:
    LITTLE_WORDS = {"a", "on", "an", "the", "of", "and", "is", "in"}
    
    words = string.split(" ")
    
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word not in LITTLE_WORDS:
            words[i] = word.capitalize()
            continue
        
    return " ".join(words)

# Task 9
def hangman(secret: str, guess: str) -> str:
    ans = ""
    guesses = set(guess)
    
    for char in secret:
        if char in guesses:
            ans += char
        else:
            ans += "_"
            
    return ans

# Task 10        
def pig_latin(phrase: str) -> str:
    VOWELS = {"a", "e", "i", "o", "u"}
    
    words = phrase.split(" ")
    pig_latin = []
    
    for string in words:
        if string.startswith("qu"):
            pig_latin.append(f"{string[2:]}quay")
            continue
        
        if string[0] in VOWELS:
            pig_latin.append(f"{string}ay")
            continue
        
        new_str = ""
        
        for i, char in enumerate(string):
            if string[i] == "q" and string[i + 1] == "u":
                new_str += char
                new_str += string[i + 1]
                continue
            
            if char not in VOWELS:
                new_str += char
            else:
                break
            
        pig_latin.append(f"{string[len(new_str):]}{new_str}ay")
        
    return " ".join(pig_latin)
